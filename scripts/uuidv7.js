#!/usr/bin/env node
/**
 * uuidv7.js — UUIDv7 generator (RFC 9562) for Node.js environments
 * Author: Quang Cuong Huynh
 *
 * Usage:
 *   node scripts/uuidv7.js           # generate 1
 *   node scripts/uuidv7.js 5         # generate 5
 *   node scripts/uuidv7.js --json    # JSON array
 *   node scripts/uuidv7.js --ts      # with parsed timestamp
 *
 * Import in code:
 *   const { uuidv7 } = require('./scripts/uuidv7.js');
 */
const crypto = require('crypto');

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

function parseTimestamp(uid) {
  const ms = parseInt(uid.replace(/-/g,'').slice(0,12), 16);
  return new Date(ms).toISOString();
}

module.exports = { uuidv7, parseTimestamp };

if (require.main === module) {
  const args   = process.argv.slice(2);
  const n      = parseInt(args.find(a => !a.startsWith('--')) || '1');
  const showTs = args.includes('--ts');
  const asJson = args.includes('--json');

  const results = Array.from({ length: n }, () => uuidv7());

  if (asJson) {
    const out = showTs
      ? results.map(u => ({ uuid: u, timestamp: parseTimestamp(u) }))
      : results;
    console.log(JSON.stringify(out, null, 2));
  } else {
    results.forEach(u => {
      if (showTs) console.log(`${u}  [${parseTimestamp(u)}]`);
      else console.log(u);
    });
  }
}
