# Analysis of Algorithms I (MC458) - Test 6

- [Questions](./Enunciado.pdf)
- [Answers](./Resposta.pdf)
- [Turn in](./Entrega.pdf)

### Question 1

For building the new railroad between the cities of **Otlas** and **Abacoros**, Xitoró's construction
company needs $t_i \ge 0$ rail segments of length $2^i$ for every $i = 0, \dots , k$.
Chorãozinho's steel mill, however, supplies rails in **only one** length $M \ge 2^k$.
Xitoró obtains the required lengths by cutting these $M$-length rails.

Xitoró has hired you to determine the **minimum number** of length-$M$ rails he must buy from
Chorãozinho **and** how they must be cut.

Design an **efficient greedy algorithm** that solves the problem optimally, presenting each of the
steps that justify the correctness of your algorithm according to the greedy-paradigm method
studied in class.  Also give its time complexity.

*Input.* The $k+1$ values $t_i$ for $i = 0,\dots ,k$ and the length $M$ used by the steel mill this week.

---

### Question 2

Let $S = (s_1, s_2, \dots, s_n)$ be a sequence of $n$ positive integers.
The **imbalance** of $S$, denoted $D(S)$, is the difference between its largest and its smallest
elements.

Given a positive integer $k$ and a sequence
$P = (p_1, p_2, \dots , p_n)$ of positive integers, note that one can build $2^n$ new sequences of
length $n$ by **adding or subtracting** the value $k$ to every element of $P$.

Example: with $P=(4,1,10)$ and $k=2$, some of the eight possible sequences are
$P_1=(2,3,12)$, $P_2=(6,3,8)$, $P_3=(2,-1,8)$, $P_4=(6,-1,12)$,
whose imbalances are $D(P_1)=10$, $D(P_2)=5$, $D(P_3)=9$, $D(P_4)=13$.
Have fun constructing the remaining four sequences and computing their imbalances.

Design an **efficient greedy algorithm** that receives **only** the sequence $P$ and outputs a value
of $k$ for which one can build a sequence of **minimum imbalance** from $P$, presenting each of
the steps that justify the correctness of your algorithm according to the greedy-paradigm method
studied in class.  Also give its time complexity.

Example: for the input $P=(4,1,10)$, one possible answer is $k=4$
(the optimum may not be unique).

---

### Question 3

Given a positive integer $n$, we want to express it in the form

$$
    n = t_0 \cdot 3^{0} + t_1 \cdot 3^{1} + t_2 \cdot 3^{2} + \cdots + t_k \cdot 3^{k},
$$

where $t_i \in \lbrace -1, 0, 1 \rbrace$ for every $i = 0, 1, \dots, k$.

Design an **efficient greedy algorithm** that, given $n$, finds the **smallest possible $k$**
for which such an expression exists and prints the corresponding coefficients
$t_0, t_1, \dots , t_k$.  Present each of the steps that justify the correctness of your
algorithm according to the greedy-paradigm method studied in class, and state its time complexity.

Example: for input $n = 2016$, a correct output is $[0, 0, -1, 0, 1, -1, 0, 1]$ because

$$
  2016 = 0 \cdot 3^{0} + (-1) \cdot 3^{2} + 0 \cdot 3^{3}
        + 1 \cdot 3^{4} + (-1) \cdot 3^{5} + 0 \cdot 3^{6} + 1 \cdot 3^{7}
        = -9 + 81 - 243 + 2187.
$$
