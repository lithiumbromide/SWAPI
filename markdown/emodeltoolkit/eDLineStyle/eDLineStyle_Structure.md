---
title: "eDLineStyle Structure"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/eDLineStyle/eDLineStyle_Structure.htm"
---

# eDLineStyle Structure

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents line styles.

#### Header file code

```vb
struct eDLineStyle
{
enum Style
{
eDSolidLine,
eDDottedLine,
eDCenterLine,
eDPhantomLine,
eDDashedLine,
eDDashDotLine,
eDHiddenLine,
eDLongDashLine
};

Style style;

float width;

eDLineStyle( Style s = eDSolidLine, float w = 0.0f )
: style( s ), width( w ) {}
};
```
