---
title: "GetTargetPointEntity Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "GetTargetPointEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity.html"
---

# GetTargetPointEntity Method (ICamera)

Gets the target point on the entity for the camera.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTargetPointEntity( _
   ByRef Point As MathPoint, _
   ByRef PercentTarget As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim Point As MathPoint
Dim PercentTarget As System.Double
Dim value As System.Object

value = instance.GetTargetPointEntity(Point, PercentTarget)
```

### C#

```csharp
System.object GetTargetPointEntity(
   out MathPoint Point,
   out System.double PercentTarget
)
```

### C++/CLI

```cpp
System.Object^ GetTargetPointEntity(
   [Out] MathPoint^ Point,
   [Out] System.double PercentTarget
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object indicating the target point for the camera
- `PercentTarget`: Target point distance along the entity

### Return Value

Entity for the target point

## VBA Syntax

See [Camera::GetTargetPointEntity](ms-its:sldworksapivb6.chm::/sldworks~Camera~GetTargetPointEntity.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::SetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity.html)
[ICamera::TargetPointBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.html)
[ICamera::TargetPointPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
