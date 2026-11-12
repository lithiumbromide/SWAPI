---
title: "LockCameraPosition Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "LockCameraPosition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.html"
---

# LockCameraPosition Property (ICamera)

Gets or sets whether the camera position is locked.

## Syntax

### Visual Basic (Declaration)

```vb
Property LockCameraPosition As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Boolean

instance.LockCameraPosition = value

value = instance.LockCameraPosition
```

### C#

```csharp
System.bool LockCameraPosition {get; set;}
```

### C++/CLI

```cpp
property System.bool LockCameraPosition {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if camera position is locked, false if not

## VBA Syntax

See [Camera::LockCameraPosition](ms-its:sldworksapivb6.chm::/sldworks~Camera~LockCameraPosition.html).

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
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
