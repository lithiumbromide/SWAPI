---
title: "GetPositionEntity Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "GetPositionEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity.html"
---

# GetPositionEntity Method (ICamera)

Gets the entity to which the camera is attached.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPositionEntity( _
   ByRef Point As MathPoint, _
   ByRef PercentPosition As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim Point As MathPoint
Dim PercentPosition As System.Double
Dim value As System.Object

value = instance.GetPositionEntity(Point, PercentPosition)
```

### C#

```csharp
System.object GetPositionEntity(
   out MathPoint Point,
   out System.double PercentPosition
)
```

### C++/CLI

```cpp
System.Object^ GetPositionEntity(
   [Out] MathPoint^ Point,
   [Out] System.double PercentPosition
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Point`: [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object indicating the camera position
- `PercentPosition`: Camera point distance along the entity

### Return Value

Entity for the camera position

## VBA Syntax

See [Camera::GetPositionEntity](ms-its:sldworksapivb6.chm::/sldworks~Camera~GetPositionEntity.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.html)
[ICamera::GetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.html)
[ICamera::GetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.html)
[ICamera::LockCameraPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.html)
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.html)
[ICamera::SetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionCartesian.html)
[ICamera::SetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionEntity.html)
[ICamera::SetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionSpherical.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
