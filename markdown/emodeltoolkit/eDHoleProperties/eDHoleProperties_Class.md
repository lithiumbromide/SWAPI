---
title: "eDHoleProperties Class"
project: ""
interface: "eDHoleProperties"
member: ""
kind: "class"
source: "emodeltoolkit/eDHoleProperties/eDHoleProperties_Class.htm"
---

# eDHoleProperties Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains hole axis and diameter data.

NOTE: Because the eDrawings format contains solids and surfaces made from tessellated triangles with no inherent hole topology, you add hole properties to configurations that contain geometry that is displayed as a hole when highlighted.

#### Header file code

```vb
class eDHoleProperties
{
public:

eDHoleProperties( const eDPt3d &axisstart, const eDPt3d &axisend, double holediameter )
: point0( axisstart ), point1( axisend ), diameter( holediameter ) {}

};
```
