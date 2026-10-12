---
title: "eDColorRBG Class"
project: ""
interface: "eDColorRBG"
member: ""
kind: "class"
source: "emodeltoolkit/eDColorRBG/eDColorRBG_Class.htm"
---

# eDColorRBG Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains three values between 0.0 and 1.0 that represent color data.

#### Header file code

```vb
class eDColorRGB
{
public:

eDColorFloat R;

eDColorFloat G;

eDColorFloat B;

eDColorRGB( float Red = -1, float Green = -1, float Blue = -1 )
: R( Red ), G( Green ), B( Blue ) {}

bool IsValid() const { return R.IsValid() && G.IsValid() && B.IsValid(); }; //Ensures that value is red, green, or blue

};
```
