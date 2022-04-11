import cmath
import string

z = complex(input())

ans = cmath.sqrt(z.real**2 + z.imag**2)

ans2 = cmath.phase(complex(z.real, z.imag))

print(ans.real)
print(ans2)
