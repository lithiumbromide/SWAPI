---
title: "GetPositionCartesian Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "GetPositionCartesian"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.html"
---

# GetPositionCartesian Method (ICamera)

Gets the Cartesian coordinates for the camera position.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetPositionCartesian( _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.GetPositionCartesian(X, Y, Z)
```

### C#

```csharp
void GetPositionCartesian(
   out System.double X,
   out System.double Y,
   out System.double Z
)
```

### C++/CLI

```cpp
void GetPositionCartesian(
   [Out] System.double X,
   [Out] System.double Y,
   [Out] System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate relative to the model origin
- `Y`: y coordinate relative to the model origin
- `Z`: z coordinate relative to the model origin

## VBA Syntax

See [Camera::GetPositionCartesian](ms-its:sldworksapivb6.chm::/sldworks~Camera~GetPositionCartesian.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.html)
[ICamera::GetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity.html)
[ICamera::GetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.html)
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.html)
[ICamera::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.html)
[ICamera::LockCameraPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.html)
[ICamera::SetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionCartesian.html)
[ICamera::SetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionEntity.html)
[ICamera::SetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionSpherical.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
