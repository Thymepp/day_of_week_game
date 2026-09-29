# Doomsday Algorithm (Day of the Week)

Date format below is **day/month** (e.g. `14/3` = 14 March).

## Weekday numbers

| # | Day |
|---|-----|
| 1 | Mon |
| 2 | Tue |
| 3 | Wed |
| 4 | Thu |
| 5 | Fri |
| 6 | Sat |
| 7 (or 0) | Sun |

## Formulas

Let `year = 100·c + A`, where `c` is the century number and `A` is the last two digits.

**Century anchor**

```
C = (5c + c//4 + 2) mod 7
```

**Doomsday of the year**

```
Doom = (A//12 + A mod 12 + (A mod 12)//4 + C) mod 7
```

`//` is integer division. The result is a weekday number from the table above.

### Century anchors (quick check)

| Years | c | C | Day |
|-------|---|---|-----|
| 1800s | 18 | 5 | Fri |
| 1900s | 19 | 3 | Wed |
| 2000s | 20 | 2 | Tue |
| 2100s | 21 | 0 | Sun |

## Doomsday dates (same weekday every year)

| Date (d/m) | Note |
|------------|------|
| 3/1 (common year) or 4/1 (leap year) | January |
| 28/2 (common year) or 29/2 (leap year) | last day of February |
| 14/3 | Pi day |
| 4/4 | even months: 4/4, 6/6, 8/8, 10/10, 12/12 |
| 6/6 | |
| 8/8 | |
| 10/10 | |
| 12/12 | |
| 9/5 and 5/9 | "9-to-5" |
| 11/7 and 7/11 | "7-Eleven" |

## Steps

1. Compute `C` from the century.
2. Compute `Doom` from the last two digits of the year.
3. Pick the doomsday date in the target month.
4. `weekday = (Doom + (day − doomsday_day)) mod 7`

## Example: 29/9/2026

- `c = 20`, so `C = (100 + 5 + 2) mod 7 = 2`
- `A = 26`, so `Doom = (2 + 2 + 0 + 2) mod 7 = 6` (Sat)
- September doomsday is `5/9`, and `29 − 5 = 24`
- `(6 + 24) mod 7 = 2`, which is **Tuesday** ✅
