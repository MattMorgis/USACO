# Greedy Gift Givers

A group of NP (2 ≤ NP ≤ 10) uniquely named friends has decided to exchange gifts of money. Each of these friends might or might not give some money to some or all of the other friends (although some might be cheap and give to no one). Likewise, each friend might or might not receive money from any or all of the other friends. Your goal is to deduce how much more money each person receives than they give.

The rules for gift-giving are potentially different than you might expect. Each person goes to the bank (or any other source of money) to get a certain amount of money to give and divides this money evenly among all those to whom he or she is giving a gift. No fractional money is available, so dividing 7 among 2 friends would be 3 each for the friends with 1 left over – that 1 left over goes into the giver's "account". All the participants' gift accounts start at 0 and are decreased by money given and increased by money received.

In any group of friends, some people are more giving than others (or at least may have more acquaintances) and some people have more money than others.
Given:

- a group of friends, no one of whom has a name longer than 14 characters,
- the money each person in the group spends on gifts, and
- a (sub)list of friends to whom each person gives gifts,
  determine how much money each person ends up with.

# Program Name: gift1

# Input Format

| Line Number | Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1           | A single integer, NP                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 2..NP+1     | Line i+1 contains the name of group member i                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| NP+2..end   | NP groups of lines organized like this: The first line of each group tells the person's name who will be giving gifts. The second line in the group contains two numbers: The amount of money (in the range 0..2000) to be divided into gifts by the giverNGi (1 ≤ NGi ≤ NP), the number of people to whom the giver will give gifts If NGi is nonzero, each of the next NGi lines lists the name of a recipient of a gift; recipients are not repeated in a single giver's list. |

# Sample Input (gift1.in)

```
5
dave
laura
owen
vick
amr
dave
200 3
laura
owen
vick
owen
500 1
dave
amr
150 2
vick
owen
laura
0 2
amr
vick
vick
0 0
```

# Sample Output (gift1.out)

```
dave 302
laura 66
owen -359
vick 141
amr -150
```
