# AoC2024
Advent of Code 2024

To run the code:

```
python aoc2024.py --dir dir --day D --star S
```
with:

- dir is the input data directory name
- D is the day number
- S is the star number (1 or 2)

To run the tests:

```commandline
python test_dayXX.py 
```

in the right directory

## My difficulties

### Day 1 - Historian Hysteria

Once again, my main point was that I hadn't prepared my environment yet. Moreover, I prepared a lib but didn't remember
how to use it (read data facilities)... I need to document it!

### Day 2 - Red-Nosed Reports

Star 1: didn't understand why I couldn't right this:
```python
return min(differences) > 0 & max(differences) < 4
```
Needed to write this instead:
```python
if min(differences) > 0:
    return max(differences) < 4
return False
```

Star 2: everything prepared well for it!

### Day 3 - Mull It Over

I needed to refresh in Regex, as each year... Despite this, we are still in a day when I get the right result at the
first time.

## Summary

**TODO UPDATE!**

I am a little frustrated to stop. I feel like the 2019 AoC: I had just finished, in time, all the 2020 one, so I decided
to do it after. But I kept blocked on one day and I dropped. Here, same feeling: even if I could finish some other
stars:

- I am pretty sure that some will still resist
- I will spend all my holiday week on it

What went well: 
- my test driven development. Not perfect, I will prepare something better for next year, with less
rigidity. But it was still nice to have it.
- speaking with my husband. We had different ideas. Speaking helped us to write our code with many good tips.
- Ladies of Code leaderboard, with ladies participating. Because we weren't only Paola and me competing like in 2020,
  but also other ladies continue day after day (not enough). It is nice to be together on the same game during a month.

What went wrong:

- I need to have some hand-made functions to deal with 2D maps. Some that I perfectly know and that I can append in 
  case of necessity.
- I need to have some way, already written, to deal with graphs! And maybe this story of Depth Search First.
- my husband doing the AoC with a mechanical keyboard. I was way too stressed because of it. I mustn't be in this kind
  of competition mode! Is it so important to enjoy doing it. (Precision: it is *my* fault, not my husband's. It is OK
  for him to have a mechanical keyboard and to use it.)
- I was too slow to enjoy the reddit feed https://www.reddit.com/r/adventofcode/ because I really prefer to go on it
  when I have finished the exercises of the day.

My idea: do, quietly, the 2021 during the year, to prepare the 2023 with a good tooling.