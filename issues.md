

| Issue | Type | Line(s) | Description | Fix Approach |
| ----- | ---- | ------- | ----------- | ------------ |
| B110 | Exception Handling | 22–23 | Bare `except` block silently ignores errors using `pass`. | Catch specific exceptions and handle or log them appropriately. |
| B307 | Insecure Function | 39 | Use of `eval()` may execute arbitrary code. | Replace `eval()` with `ast.literal_eval()` for literal expressions, or use a safe, explicitly defined calculation method. |
| B324 | Weak Hashing | 44 | MD5 is unsuitable for security-sensitive password or PIN hashing. | Use a password-hashing algorithm such as Argon2id, scrypt, or PBKDF2 with a unique salt. |
| B311 | Insecure Randomness | 48 | `random.randint()` is not suitable for generating security-sensitive PINs. | Use `secrets.randbelow()` or another function from Python's `secrets` module. |
| B605 | Shell Injection Risk | 55 | `os.system()` executes a shell command built using string concatenation. | Use `subprocess.run()` with a list of arguments and `shell=False`, or avoid launching a shell. |
| B105 | Hardcoded Secret | 59 | Admin token is hardcoded in the source code. | Load the token from a secure environment variable or secret manager. |

