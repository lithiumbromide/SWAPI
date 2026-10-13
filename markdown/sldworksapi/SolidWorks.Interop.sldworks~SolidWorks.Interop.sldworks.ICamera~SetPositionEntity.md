---
title: "SetPositionEntity Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "SetPositionEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionEntity.html"
---

# SetPositionEntity Method (ICamera)

Sets the entity to which the camera is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPositionEntity( _
   ByVal Point As MathPoint, _
   ByVal PercentPosition As System.Double, _
   ByVal PositionEntity As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim Point As MathPoint
Dim PercentPosition As System.Double
Dim PositionEntity As System.Object

instance.SetPositionEntity(Point, PercentPosition, PositionEntity)
```

### C#

```csharp
void SetPositionEntity(
   MathPoint Point,
   System.double PercentPosition,
   System.object PositionEntity
)
```

### C++/CLI

```cpp
void SetPositionEntity(
   MathPoint^ Point,
   System.double PercentPosition,
   System.Object^ PositionEntity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: Pointer to the [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object indicating the camera position
- `PercentPosition`: Camera point distance along the entity
- `PositionEntity`: Entity for the camera position

## VBA Syntax

See [Camera::SetPositionEntity](ms-its:sldworksapivb6.chm::/sldworks~Camera~SetPositionEntity.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.html)
[ICamera::GetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.html)
[ICamera::GetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity.html)
[ICamera::GetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.html)
[ICamera::SetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionCartesian.html)
[ICamera::SetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionSpherical.html)
[ICamera::LockCameraPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.html)
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
