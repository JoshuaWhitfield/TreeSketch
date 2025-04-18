#!/usr/bin/env node

import { Interpreter } from './interpreter.js';
import readline from 'readline';

const interpreter = new Interpreter();
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  prompt: 'web-crawler> '
});

rl.prompt();

rl.on('line', (line) => {
  try {
    interpreter.execute(line.trim());
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
  rl.prompt();
}).on('close', () => {
  console.log('Exiting web crawler CLI');
  process.exit(0);
});