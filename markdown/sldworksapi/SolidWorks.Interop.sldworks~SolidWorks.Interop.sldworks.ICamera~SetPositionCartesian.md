---
title: "SetPositionCartesian Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "SetPositionCartesian"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionCartesian.html"
---

# SetPositionCartesian Method (ICamera)

Sets the Cartesian coordinates for the camera position.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetPositionCartesian( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.SetPositionCartesian(X, Y, Z)
```

### C#

```csharp
void SetPositionCartesian(
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void SetPositionCartesian(
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`: x coordinate relative to the model origin
- `Y`: y coordinate relative to the model origin
- `Z`: z coordinate relative to the model origin

## VBA Syntax

See [Camera::SetPositionCartesian](ms-its:sldworksapivb6.chm::/sldworks~Camera~SetPositionCartesian.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetPosition Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.html)
[ICamera::GetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.html)
[ICamera::GetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity.html)
[ICamera::GetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.html)
[ICamera::SetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionEntity.html)
[ICamera::SetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetPositionSpherical.html)
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.html)
[ICamera::LockCameraPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
