---
title: "CreatePlaneByNormal Method (IMathUtility)"
project: ""
interface: "IMathUtility"
member: "CreatePlaneByNormal"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreatePlaneByNormal.html"
---

# CreatePlaneByNormal Method (IMathUtility)

Creates an infinite mathematical plane as defined by the specified origin and normal.

## Syntax

### Visual Basic

```vb
Function CreatePlaneByNormal( _
   ByVal Origin As MathPoint, _
   ByVal Normal As MathVector _
) As MathPlane
```

### C#

```csharp
MathPlane CreatePlaneByNormal(
   MathPoint Origin,
   MathVector Normal
)
```

### JScript

```
function CreatePlaneByNormal(
   Origin : MathPoint,
   Normal : MathVector
) : MathPlane;
```

### Managed Extensions for C++

```
MathPlane* CreatePlaneByNormal(
   MathPoint* Origin,
   MathVector* Normal
)
```

### C++/CLI

```cpp
MathPlane^ CreatePlaneByNormal(
   MathPoint^ Origin,
   MathVector^ Normal
)
```

### Parameters

- `Origin`: [IMathPoint](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)
- `Normal`: [IMathVector](Interop.dsAutomation~Interop.dsAutomation.IMathVector.html)

### Return Value

[IMathPlane](Interop.dsAutomation~Interop.dsAutomation.IMathPlane.html)

## See Also

[IMathUtility Interface](Interop.dsAutomation~Interop.dsAutomation.IMathUtility.html)
[IMathUtility Members](Interop.dsAutomation~Interop.dsAutomation.IMathUtility_members.html)
[IMathUtility::CreatePlaneByUV Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreatePlaneByUV.html)
[IMathUtility::CreateXYPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateXYPlane.html)
[IMathUtility::CreateYZPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateYZPlane.html)
[IMathUtility::CreateZXPlane Method](Interop.dsAutomation~Interop.dsAutomation.IMathUtility~CreateZXPlane.html)

## Availability

DraftSight V1R1.4
