Timing with Python

```python
import datetime
now = datetime.datetime.now()
```

```python
next_week = now + datetime.timedelta(days=7)
in_six_days = now + datetime.timedelta(days=6)
```


```python
sub_ends = now + datetime.timedelta(days=6, hours=20)
ends_this_week = sub_ends < next_week # True
```

```python
ends_later_than_next_week = sub_ends > next_week # False
ends_in_about_seven_days = in_six_days < sub_ends and sub_ends < next_week
```


```python
sub_ends_2 = now + datetime.timedelta(days=7, hours=2)
next_week_min = next_week.replace(hour=0, minute=0, second=0, microsecond=0)
next_week_max = next_week.replace(hour=23, minute=59, second=59, microsecond=59)
```