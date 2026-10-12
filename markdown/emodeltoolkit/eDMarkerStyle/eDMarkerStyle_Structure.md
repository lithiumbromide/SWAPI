---
title: "eDMarkerStyle Structure"
project: ""
interface: ""
member: ""
kind: "topic"
source: "emodeltoolkit/eDMarkerStyle/eDMarkerStyle_Structure.htm"
---

# eDMarkerStyle Structure

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents 3D marker point styles.

#### Header file code

```vb
struct eDMarkerStyle
{
enum Style
{
eDCircle,
eDCircleWithDot,
eDCircleWithPlus,
eDCircleWithTimes,
eDCircleWithCircle,
eDSolidCircle,
eDDot,
eDPlus,
eDTimes,
eDSplat,
eDBox,
eDBoxWithDot,
eDBoxWithTimes,
eDSolidBox,
eDDiamond,
eDDiamondWithDot,
eDDiamondWithPlus,
eDSolidDiamond,
eDTriangleUp,
eDTriangleUpWithDot,
eDSolidTriangleUp,
eDTriangleUpV,
eDSolidTriangleUpV,
eDTriangleDown,
eDTriangleDownWithDot,
eDSolidTriangleDown,
eDTriangleDownV,
eDSolidTriangleDownV,
eDTriangleLeft,
eDTriangleLeftWithDot,
eDSolidTriangleLeft,
eDTriangleLeftV,
eDSolidTriangleLeftV,
eDTriangleRight,
eDTriangleRightWithDot,
eDSolidTriangleRight,
eDTriangleRightV,
eDSolidTriangleRightV,
eDLetterY,
eDLetterZ,
eDCircleLetterY,
eDCircleLetterZ,
eDVerticalBar,
eDHorizontalBar,
eDSlantRight,
eDSlantLeft,
eDWidePlus,
eDSolidWidePlus,
eDWideTimes,
eDSolidWideTimes,
eDPound
};

Style style;

eDMarkerStyle( Style s = eDDot ) : style( s ) {}

};
```
