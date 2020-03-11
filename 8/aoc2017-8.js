const fs = require('fs');
const _ = require('lodash');

const { each, lt, lte, gt, gte, isEqual, subtract, add, set, negate, max, values } = _;

const puzzleInput = fs.readFileSync('/Users/sschwa12/code/aoc2017/8/aoc2017-8.data', 'utf-8')
  .split('\n')
  .map(ln => ln.split(' '));

const INSTRUCTIONS = {
  dec: subtract,
  inc: add,
};

const COMPARATORS = {
  '<': lt,
  '<=': lte,
  '>': gt,
  '>=': gte,
  '==': isEqual,
  '!=': negate(isEqual),
};

const runInstructions = () => {
  const registers = _(puzzleInput).map(ln => [ln[0], 0]).fromPairs().value();
  let maxValue = Number.MIN_SAFE_INTEGER;
  each(puzzleInput, ln => {
    const [register, instruction, strAmount, , compareWith, sign, strNum] = ln;
    const amount = Number(strAmount);
    const num = Number(strNum);
    if (COMPARATORS[sign](registers[compareWith], num)) {
      const registerValue = registers[register];
      if (registerValue > maxValue) {
        maxValue = registerValue;
      }
      set(registers, register, INSTRUCTIONS[instruction](registerValue, amount));
    }
  });
  return [max(values(registers)), maxValue];
};

const [p1, p2] = runInstructions();
console.log('part1', p1, 'part2', p2);
