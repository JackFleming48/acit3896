When we say:<br>
log<sub>4</sub>(1024)<br>
It means if we start at one how many times to end up at 1024?<br>
1x4x4x4x4x4 = 1024<br>
so 5 times!<br>

In a broader definition:<br>
If you wanna go from 1 to X, by multiplying by B, how many multiplications does it take?<br>

**Review**<br>
1. Logarithms are reverse exponentiation (but they are not roots)
   - and they are the important reverse-exponentiation for algorithms
2. (The other reverse is the root, we don't really care much)
3. The logarithm asks "how many times do I need to multiply by this base, to get from 1 to this other number?"
4. All of the math works out fine with fractions/floats, so don't stress.
5. The notation is that the base goes in the subscript, and the result goes like a function argument
   - log<sub>b</sub>(big_number) = ????
6. Multiplying up is the same as dividing down
    - Getting to X from 1 by multiplying by 2, is the same as getting to 1 from X by dividing by 2
7. We saw some patterns.
8. We learned how to change base (for calculators)
9. In comp sci, if someone doesn't tell you the base, 99.9% chance that the base is 2.

1x4x4x4x4x4 = 1024<br>
This is very similar to doing this<br>
1024 /4 /4 /4 /4 /4 = 1<br>
So say we want to know how many times to cut 1024 in half to get to one?<br>
log<sub>2</sub>(1024)<br>
<br>
In a computer science context, if you are doing logs and noone tells you the base:
- **ASSUME IT IS BASE 2**
<br>
If you want to do:<br>
log<sub>b</sub>X = log<sub>q</sub>X<br>
on a calculator you need a scaling factor that makes b scale to q.<br>
A simple way to do this is:<br>
log<sub>q</sub>X / log<sub>b</sub>X<br>

In plain english:
1. Type in the X
2. press log
3. Type in the B
4. press log
<br>
**Same with log and ln (log natural)**