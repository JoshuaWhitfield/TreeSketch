// Interpreter implementation
import { CommandRouter } from './router.js';
import { Lexer } from './lexer.js';
import { Parser } from './parser.js';

export class Interpreter {
  constructor() {
    this.router = new CommandRouter();
  }

  execute(input) {
    const lexer = new Lexer(input);
    const tokens = lexer.tokenize();
    
    const parser = new Parser(tokens);
    const command = parser.parse();
    
    return this.router.route(command);
  }
}