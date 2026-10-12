---
title: "eDBody Class"
project: ""
interface: "eDBody"
member: ""
kind: "class"
source: "emodeltoolkit/eDBody/eDBody_Class.htm"
---

# eDBody Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains shells, curves, and marker points.

#### Header file code

```vb
class eDBody : public eDObject
{
public:

eDOutcome AddBinaryData (const char* data, int dataLength);

eDOutcome CreateShellList( const eDAppearance &appearance, eDShellList *& shelllist ); //Creates one or more shells

eDOutcome CreateCurveList( const eDAppearance &appearance, eDCurveList *& curvelist ); //Creates one or more curves

eDOutcome CreateMarkerList( const eDAppearance &appearance, eDMarkerList *& markerlist ); //Creates one or more 3D marker points

eDOutcome SetTransform( const eDTransform3d &transform ); //Sets the 3D transform

};
```
