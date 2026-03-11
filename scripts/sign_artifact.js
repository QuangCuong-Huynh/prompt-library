#!/usr/bin/env node
/**
 * sign_artifact.js — Universal Artifact Signature generator (JavaScript/Node.js)
 * Author:    Quang Cuong Huynh (Registered IP Authority)
 * Authority: Registered — Quang Cuong Huynh
 *
 * Mirrors sign_artifact.py for Node.js / Claude Code / frontend toolchain environments.
 *
 * Usage:
 *   node scripts/sign_artifact.js --path docs/myfile.md
 *   node scripts/sign_artifact.js --batch --dir personas/
 *   node scripts/sign_artifact.js --path docs/myfile.md --dry-run
 *   node scripts/sign_artifact.js --generate-uuid          # just print a UUIDv7
 *   node scripts/sign_artifact.js --generate-hash --path f  # just SHA-256
 */
const fs   = require('fs');
const path = require('path');
const crypto = require('crypto');

// ─── UUIDv7 (RFC 9562) ──────────────────────────────────────────────────────
function uuidv7() {
  const ms     = BigInt(Date.now());
  const randBuf = crypto.randomBytes(10);
  const rand   = BigInt('0x' + randBuf.toString('hex'));
  const uuid_int =
    (ms << 80n)
    | (0x7n << 76n)
    | ((rand >> 62n) << 64n)
    | (0b10n << 62n)
    | (rand & 0x3FFFFFFFFFFFFFFFn);
  const h = uuid_int.toString(16).padStart(32, '0');
  return `${h.slice(0,8)}-${h.slice(8,12)}-${h.slice(12,16)}-${h.slice(16,20)}-${h.slice(20)}`;
}

// ─── SHA-256 ──────────────────────────────────────────────────────────────────
function sha256Body(filePath) {
  const raw  = fs.readFileSync(filePath, 'utf8');
  const body = raw.replace(/^---\n[\s\S]*?\n---\n/, '');
  return crypto.createHash('sha256').update(body, 'utf8').digest('hex');
}

function sha256String(s) {
  return crypto.createHash('sha256').update(s, 'utf8').digest('hex');
}

// ─── ISO-8601 timestamp ───────────────────────────────────────────────────────
function isoNow() {
  return new Date().toISOString().replace(/\.\d{3}Z$/, 'Z');
}

// ─── Frontmatter patch ────────────────────────────────────────────────────────
function patchFrontmatter(filePath, artifactId, digest) {
  let text = fs.readFileSync(filePath, 'utf8');
  let changed = false;
  if (text.includes('artifact_id: ""')) {
    text = text.replace('artifact_id: ""', `artifact_id: "${artifactId}"`);
    changed = true;
  }
  if (text.includes('sha256: ""')) {
    text = text.replace('sha256: ""', `sha256: "${digest}"`);
    changed = true;
  }
  if (changed) fs.writeFileSync(filePath, text, 'utf8');
  return changed;
}

// ─── Recursive file scan ──────────────────────────────────────────────────────
function scanDir(dir, exts = ['.md', '.yml', '.yaml']) {
  const results = [];
  function walk(d) {
    for (const entry of fs.readdirSync(d, { withFileTypes: true })) {
      const full = path.join(d, entry.name);
      if (entry.isDirectory() && entry.name !== '.git' && entry.name !== 'node_modules') {
        walk(full);
      } else if (entry.isFile() && exts.includes(path.extname(entry.name))) {
        results.push(full);
      }
    }
  }
  walk(dir);
  return results;
}

// ─── CLI ──────────────────────────────────────────────────────────────────────
const args = process.argv.slice(2);
const getArg = (flag) => { const i = args.indexOf(flag); return i !== -1 ? args[i+1] : null; };
const hasFlag = (flag) => args.includes(flag);

if (hasFlag('--generate-uuid')) {
  const n = parseInt(getArg('--n') || '1');
  for (let i = 0; i < n; i++) console.log(uuidv7());
  process.exit(0);
}

if (hasFlag('--generate-hash')) {
  const p = getArg('--path');
  if (!p) { console.error('--path required'); process.exit(1); }
  console.log(sha256Body(p));
  process.exit(0);
}

if (hasFlag('--timestamp')) {
  console.log(isoNow());
  process.exit(0);
}

const filePath  = getArg('--path');
const batchMode = hasFlag('--batch');
const dirPath   = getArg('--dir') || '.';
const dryRun    = hasFlag('--dry-run');

let targets = [];
if (filePath)   targets = [filePath];
else if (batchMode) targets = scanDir(dirPath);
else { console.log('Usage: node sign_artifact.js --path <file> | --batch [--dir <dir>] [--dry-run]'); process.exit(0); }

let signed = 0, skipped = 0;
for (const t of targets) {
  if (!fs.existsSync(t)) continue;
  const text = fs.readFileSync(t, 'utf8');
  if (!text.startsWith('---') || !text.includes('artifact_id: ""')) { skipped++; continue; }

  const uid    = uuidv7();
  const digest = sha256Body(t);

  if (dryRun) {
    console.log(`[DRY] ${t}`);
    console.log(`  artifact_id : ${uid}`);
    console.log(`  sha256      : ${digest}`);
  } else {
    const changed = patchFrontmatter(t, uid, digest);
    if (changed) {
      signed++;
      console.log(`  ✓ SIGNED  ${t}  →  ${uid.slice(0,18)}...`);
    } else {
      skipped++;
    }
  }
}

if (!dryRun) console.log(`\nSigned: ${signed} | Skipped: ${skipped} | Total: ${targets.length}`);
