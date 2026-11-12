---
title: "RotationRollAngle Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "RotationRollAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle.html"
---

# RotationRollAngle Property (ICamera)

Gets or sets the camera's roll angle.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationRollAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Double

instance.RotationRollAngle = value

value = instance.RotationRollAngle
```

### C#

```csharp
System.double RotationRollAngle {get; set;}
```

### C++/CLI

```cpp
property System.double RotationRollAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Roll angle for camera

## VBA Syntax

See [Camera::RotationRollAngle](ms-its:sldworksapivb6.chm::/sldworks~Camera~RotationRollAngle.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::RotationRollBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection.html)
[ICamera::RotationRollEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity.html)
[ICamera::RotationRollFlipDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
