---
title: "eDCamera Class"
project: ""
interface: "eDCamera"
member: ""
kind: "class"
source: "emodeltoolkit/eDCamera/eDCamera_Class.htm"
---

# eDCamera Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Represents a camera.

#### Header file code

```vb
class eDCamera
{
public:

eDCamera();

eDCamera(
const eDPt3d &position,
const eDPt3d &target,
const eDPt3d &up,
double width,
double height,
eDCameraProjection projection = eDCameraOrthographic
);

};
```
