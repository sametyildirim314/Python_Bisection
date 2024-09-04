![Bisection_method svg](https://github.com/user-attachments/assets/c867ba1e-2407-4e0f-8875-29ac9578753d)


The method is applicable for numerically solving the equation f(x) = 0 for the real variable x, where f is a continuous function defined on an interval [a, b] and where f(a) and f(b) have opposite signs. In this case a and b are said to bracket a root since, by the intermediate value theorem, the continuous function f must have at least one root in the interval (a, b).

At each step the method divides the interval in two parts/halves by computing the midpoint c = (a+b) / 2 of the interval and the value of the function f(c) at that point. If c itself is a root then the process has succeeded and stops. Otherwise, there are now only two possibilities: either f(a) and f(c) have opposite signs and bracket a root, or f(c) and f(b) have opposite signs and bracket a root.[5] The method selects the subinterval that is guaranteed to be a bracket as the new interval to be used in the next step. In this way an interval that contains a zero of f is reduced in width by 50% at each step. The process is continued until the interval is sufficiently small.

Explicitly, if f(c)=0 then c may be taken as the solution and the process stops. Otherwise, if f(a) and f(c) have opposite signs, then the method sets c as the new value for b, and if f(b) and f(c) have opposite signs then the method sets c as the new a. In both cases, the new f(a) and f(b) have opposite signs, so the method is applicable to this smaller interval.[6]

Iteration tasks
The input for the method is a continuous function f, an interval [a, b], and the function values f(a) and f(b). The function values are of opposite sign (there is at least one zero crossing within the interval). Each iteration performs these steps:

Calculate c, the midpoint of the interval, c = ⁠
a + b
/
2
⁠.
Calculate the function value at the midpoint, f(c).
If convergence is satisfactory (that is, c − a is sufficiently small, or |f(c)| is sufficiently small), return c and stop iterating.
Examine the sign of f(c) and replace either (a, f(a)) or (b, f(b)) with (c, f(c)) so that there is a zero crossing within the new interval.
When implementing the method on a computer, there can be problems with finite precision, so there are often additional convergence tests or limits to the number of iterations. Although f is continuous, finite precision may preclude a function value ever being zero. For example, consider f(x) = cos x; there is no floating-point value approximating x = π/2 that gives exactly zero. Additionally, the difference between a and b is limited by the floating point precision; i.e., as the difference between a and b decreases, at some point the midpoint of [a, b] will be numerically identical to (within floating point precision of) either a or b.
