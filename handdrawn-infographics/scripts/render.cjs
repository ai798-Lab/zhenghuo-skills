#!/usr/bin/env node
// Rasterize the editable SVG itself; never outline text as a hidden substitute.
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const { createHash } = require('node:crypto');
const { spawnSync } = require('node:child_process');

function loadSharp(explicit) {
  const candidates = [explicit, process.env.SHARP_MODULE, 'sharp',
    path.join(os.homedir(), '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp')].filter(Boolean);
  for (const location of candidates) {
    try { return require(location); } catch (error) {
      if (explicit === location) throw new Error(`Cannot load requested sharp module: ${error.message}`);
    }
  }
  throw new Error('sharp is unavailable; specify --sharp-module with an existing installation.');
}

function fontCheck(manifest, out) {
  const executable = ['/opt/homebrew/bin/fc-match', '/usr/local/bin/fc-match', '/usr/bin/fc-match'].find(fs.existsSync) || 'fc-match';
  const result = {};
  for (const [weight, filename] of Object.entries(manifest.fonts)) {
    const style = manifest.font_styles?.[weight] || (weight === 'bold' ? 'Bold' : 'Regular');
    const matched = spawnSync(executable, ['-f', '%{file}', `${manifest.font_family}:style=${style}`], { encoding:'utf8' });
    if (matched.error || matched.status !== 0 || !matched.stdout.trim()) {
      throw new Error('Font matching unavailable. Install/configure fontconfig before rendering; do not assume the measured font was used.');
    }
    const actual = fs.realpathSync(matched.stdout.trim());
    if (actual !== fs.realpathSync(path.resolve(out, filename))) throw new Error(`Font mismatch for ${weight}: expected ${filename}; matched ${actual}`);
    result[weight] = path.basename(actual);
  }
  return result;
}

function configureFonts(manifest, out) {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'handdrawn-fonts-'));
  const escape = value => value.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
  const dirs = [...new Set(Object.values(manifest.fonts).map(p => path.dirname(fs.realpathSync(path.resolve(out,p)))))];
  const config = path.join(tmp,'fonts.conf');
  fs.writeFileSync(config, '<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd"><fontconfig>'+
    dirs.map(dir=>`<dir>${escape(dir)}</dir>`).join('')+`<cachedir>${escape(tmp)}</cachedir></fontconfig>`);
  process.env.FONTCONFIG_FILE = config;
  process.env.FONTCONFIG_PATH = tmp;
  // Must be set before loading sharp. Core Text can silently ignore fontconfig.
  process.env.PANGOCAIRO_BACKEND = 'fontconfig';
  return tmp;
}

(async () => {
  const input = process.argv[2];
  if (!input) throw new Error('Usage: node render.cjs /path/to/manifest.json [--sharp-module /path/to/sharp]');
  const args = process.argv.slice(3); const si = args.indexOf('--sharp-module');
  const manifest = JSON.parse(fs.readFileSync(input, 'utf8'));
  const out = path.dirname(path.resolve(input));
  const fontTmp = configureFonts(manifest, out);
  try {
  const sharp = loadSharp(si >= 0 ? args[si+1] : undefined);
  const matched = fontCheck(manifest, out); const rows=[];
  fs.mkdirSync(path.join(out, 'PNG'), { recursive:true });
  for (const figure of manifest.figures) {
    if (!/^[\p{L}\p{N}_-]+$/u.test(figure.id)) throw new Error('Unsafe figure id');
    const svg=path.join(out,'SVG',figure.id+'.svg');
    const target=path.join(out,'PNG',figure.id+'.png');
    const tmp=target+'.tmp';
    // Set only the raster viewport. Some librsvg builds apply density twice to
    // millimetre dimensions; unitless dimensions at 72 dpi avoid huge intermediates.
    // All vector geometry and editable text come unchanged from the source SVG.
    const source=fs.readFileSync(svg,'utf8');
    const sourceHash=createHash('sha256').update(source).digest('hex');
    const layoutCheck=figure.svg_sha256===sourceHash ? 'matches_checked_build' : 'stale_or_unrecorded_recheck_layout';
    if(layoutCheck!=='matches_checked_build') console.warn(`Layout evidence needs refresh for ${figure.id}: SVG changed or no baseline hash. PNG will render, but old text bounds are not current validation.`);
    const rasterHeight=Math.round(figure.height*figure.png_width/960);
    const rasterSource=source.replace(/<svg\b[^>]*>/,root=>root
      .replace(/\bwidth="[^"]*"/,`width="${figure.png_width}"`)
      .replace(/\bheight="[^"]*"/,`height="${rasterHeight}"`));
    try {
      await sharp(Buffer.from(rasterSource),{density:72,limitInputPixels:150000000}).resize({width:figure.png_width})
        .flatten({background:'#ffffff'}).withMetadata({density:figure.dpi})
        .png({compressionLevel:9}).toFile(tmp);
      const meta=await sharp(tmp).metadata();
      if (meta.width!==figure.png_width || !meta.height || meta.format!=='png') throw new Error('PNG verification failed');
      fs.renameSync(tmp,target);
      rows.push({id:figure.id,width:meta.width,height:meta.height,density:meta.density,format:meta.format,
        svg_sha256:sourceHash,layout_check:layoutCheck});
    } finally { if(fs.existsSync(tmp)) fs.unlinkSync(tmp); }
  }
  fs.writeFileSync(path.join(out,'render-report.json'),JSON.stringify({font_family:manifest.font_family,font_matches:matched,font_backend:'fontconfig',figures:rows,visual_review:'required'},null,2));
  console.log(`Rendered ${rows.length} PNG files directly from editable SVG.`);
  } finally { fs.rmSync(fontTmp, { recursive:true, force:true }); }
})().catch(error=>{console.error('ERROR: '+error.message);process.exitCode=1;});
