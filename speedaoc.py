import requests
from itertools import permutations, product, combinations
from collections import defaultdict, Counter, deque
import sys

from cookie import AOC_COOKIE

class AOC:
    def __init__(self, day, year=2022, offset=0):
        self.day = day
        self.year = year
        self.submit = False
        self.offset = offset
        if 'submit' in sys.argv:
            self.submit = True
        self.part = 1
        if '2' in sys.argv:
            self.part = 2
        print('AOC %d/%d Part %d [%s]' % (self.day, self.year, self.part,
            'submission' if self.submit else 'example'))
        try:
            self._input = open('input.txt').read()
        except FileNotFoundError:
            self._input = None
        try:
            self._example = open('example.txt').read()
        except FileNotFoundError:
            self._example = None
        self.input
        self.example

    def rawdata(self):
        if self.submit:
            s = self.input
        else:
            s = self.example
        return s

    @property
    def data(self):
        if self.submit:
            s = self.input
        else:
            s = self.example
        return s.strip()

    @property
    def input(self):
        if self._input is None:
            print('Downloading input...')
            req = requests.get(f'https://adventofcode.com/{self.year}/day/{self.day}/input', 
                       headers={'cookie':'session='+AOC_COOKIE})
            self._input = req.text
            open('input.txt','w').write(self._input)
        return self._input

    @property
    def example(self):
        if self._example is None:
            print('Downloading example...')
            req = requests.get(f'https://adventofcode.com/{self.year}/day/{self.day}',
                headers={'cookie':'session='+AOC_COOKIE})
            self._example = req.text.split('<pre><code>')[self.offset+1].split('</code></pre>')[0]
            open('example.txt','w').write(self._example)
        return self._example

    def __call__(self, answer):
        print(f'You are about to submit the follwing answer:')
        print(f'>>>>>>>>>>>>>>>>> {answer}')
        if not self.submit:
            print('Example. No submission.')
            return
        input('Press enter to continue or Ctrl+C to abort.')
        data = {
          'level': str(self.part),
          'answer': str(answer)
        }

        response = requests.post(f'https://adventofcode.com/{self.year}/day/{self.day}/answer',
            headers={'cookie':'session='+AOC_COOKIE}, data=data)
        if 'You gave an answer too recently' in response.text:
            # You will get this if you submitted a wrong answer less than 60s ago.
            print('VERDICT : TOO MANY REQUESTS')
        elif 'not the right answer' in response.text:
            if 'too low' in response.text:
                print('VERDICT : WRONG (TOO LOW)')
            elif 'too high' in response.text:
                print('VERDICT : WRONG (TOO HIGH)')
            else:
                print('VERDICT : WRONG (UNKNOWN)')
        elif 'seem to be solving the right level.' in response.text:
            # You will get this if you submit on a level you already solved.
            # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
            print('VERDICT : ALREADY SOLVED')
        else:
            print('VERDICT : OK !')

