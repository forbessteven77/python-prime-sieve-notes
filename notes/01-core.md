# List primes up to a bound: implementation

## What the example does

The sieve marks multiples starting at p squared because smaller multiples are already handled. Memory grows linearly with the bound.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
30
```

Expected result:

```json
[
  2,
  3,
  5,
  7,
  11,
  13,
  17,
  19,
  23,
  29
]
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
