---
title: "SetTargetPointEntity Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "SetTargetPointEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity.html"
---

# SetTargetPointEntity Method (ICamera)

Gets the target point on the entity for the camera.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTargetPointEntity( _
   ByVal Point As MathPoint, _
   ByVal PercentTarget As System.Double, _
   ByVal TargetPointEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim Point As MathPoint
Dim PercentTarget As System.Double
Dim TargetPointEntity As System.Object

instance.SetTargetPointEntity(Point, PercentTarget, TargetPointEntity)
```

### C#

```csharp
void SetTargetPointEntity(
   MathPoint Point,
   System.double PercentTarget,
   System.object TargetPointEntity
)
```

### C++/CLI

```cpp
void SetTargetPointEntity(
   MathPoint^ Point,
   System.double PercentTarget,
   System.Object^ TargetPointEntity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: Pointer to the [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object indicating the target point for the camera
- `PercentTarget`: Target point distance along the entity
- `TargetPointEntity`: Entity for the target point

## VBA Syntax

See [Camera::SetTargetPointEntity](ms-its:sldworksapivb6.chm::/sldworks~Camera~SetTargetPointEntity.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity.html)
[ICamera::TargetPointBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.html)
[ICamera::TargetPointPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
