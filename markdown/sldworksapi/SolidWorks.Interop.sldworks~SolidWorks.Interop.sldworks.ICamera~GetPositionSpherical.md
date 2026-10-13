---
title: "GetPositionSpherical Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "GetPositionSpherical"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.html"
---

# GetPositionSpherical Method (ICamera)

Gets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetPositionSpherical( _
   ByRef L As System.Double, _
   ByRef A1 As System.Double, _
   ByRef A2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim L As System.Double
Dim A1 As System.Double
Dim A2 As System.Double

instance.GetPositionSpherical(L, A1, A2)
```

### C#

```csharp
void GetPositionSpherical(
   out System.double L,
   out System.double A1,
   out System.double A2
)
```

### C++/CLI

```cpp
void GetPositionSpherical(
   [Out] System.double L,
   [Out] System.double A1,
   [Out] System.double A2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `L`: Distance from target
- `A1`: Longitude about target
- `A2`: Latitude about target

## VBA Syntax

See [Camera::GetPositionSpherical](ms-its:sldworksapivb6.chm::/sldworks~Camera~GetPositionSpherical.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.html)
[ICamera::GetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.html)
[ICamera::GetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity.html)
[ICamera::GetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.html)
[ICamera::SetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionCartesian.html)
[ICamera::SetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionEntity.html)
[ICamera::SetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionSpherical.html)
[ICamera::LockCameraPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.html)
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
