---
title: "eDTime Class"
project: ""
interface: "eDTime"
member: ""
kind: "class"
source: "emodeltoolkit/eDTime/eDTime_Class.htm"
---

# eDTime Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains the date and time that the file will expire or not open.

#### Header file code

```vb
class ED_API eDTime
{
static eDTime GetCurrentTime();

eDTime();
eDTime( time_t time );
//nMonth : 1=Jan
eDTime( int nYear, int nMonth, int nDay, int nHour, int nMin, int nSec,int nDST = -1 );

bool IsValid() const;
time_t GetTime() const;
};
```
