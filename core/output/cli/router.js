// Command router implementation
import * as baseCommands from './commands/base.js';
import * as crawlCommands from './commands/crawl.js';

export class CommandRouter {
  constructor() {
    this.commands = {
      ...baseCommands,
      ...crawlCommands
    };
  }

  route(command) {
    const { name, args } = command;
    if (this.commands[name]) {
      return this.commands[name](...args);
    }
    throw new Error(`Command not found: ${name}`);
  }
}