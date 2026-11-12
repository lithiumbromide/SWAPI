---
title: "GetPosition Method (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "GetPosition"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPosition.html"
---

# GetPosition Method (ICamera)

Gets the current position of the camera.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPosition() As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As MathPoint

value = instance.GetPosition()
```

### C#

```csharp
MathPoint GetPosition()
```

### C++/CLI

```cpp
MathPoint^ GetPosition();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) object

## VBA Syntax

See [Camera::GetPosition](ms-its:sldworksapivb6.chm::/sldworks~Camera~GetPosition.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::GetPositionCartesian Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionCartesian.html)
[ICamera::GetPositionEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionEntity.html)
[ICamera::GetPositionSpherical Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetPositionSpherical.html)
[ICamera::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~PositionType.html)
[ICamera::LockCameraPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~LockCameraPosition.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
