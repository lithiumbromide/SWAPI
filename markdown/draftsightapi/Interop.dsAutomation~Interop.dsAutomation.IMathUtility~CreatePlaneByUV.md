---
title: "CreatePlaneByUV Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreatePlaneByUV"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreatePlaneByUV.html"
---

# CreatePlaneByUV Method (IMathUtility)

Creates an infinite mathematical plane as defined by the specified origin and the two specified non-collinear vectors.

## Syntax

### Visual Basic

```vb
Function CreatePlaneByUV( _
   ByVal Origin As MathPoint, _
   ByVal UAxis As MathVector, _
   ByVal VAxis As MathVector _
) As MathPlane
```

### C#

```csharp
MathPlane CreatePlaneByUV(
   MathPoint Origin,
   MathVector UAxis,
   MathVector VAxis
)
```

### JScript

```
function CreatePlaneByUV(
   Origin : MathPoint,
   UAxis : MathVector,
   VAxis : MathVector
) : MathPlane;
```

### Managed Extensions for C++

```
MathPlane* CreatePlaneByUV(
   MathPoint* Origin,
   MathVector* UAxis,
   MathVector* VAxis
)
```

### C++/CLI

```cpp
MathPlane^ CreatePlaneByUV(
   MathPoint^ Origin,
   MathVector^ UAxis,
   MathVector^ VAxis
)
```

### Parameters

- `Origin`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `UAxis`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) (see **Remarks**)
- `VAxis`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html) (see **Remarks**)

### Return Value

[IMathPlane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)

## Remarks

UAxis and VAxis do not need to be unit vectors or perpendicular, but they must not be collinear.

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreatePlaneByNormal Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreatePlaneByNormal.html)
[IMathUtility::CreateXYPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateXYPlane.html)
[IMathUtility::CreateYZPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateYZPlane.html)
[IMathUtility::CreateZXPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateZXPlane.html)

## Availability

DraftSight V1R1.4
