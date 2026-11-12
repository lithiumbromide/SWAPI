---
title: "RotationRollFlipDirection Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "RotationRollFlipDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.html"
---

# RotationRollFlipDirection Property (ICamera)

Gets or sets whether to flip the direction of the camera 180

.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationRollFlipDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Boolean

instance.RotationRollFlipDirection = value

value = instance.RotationRollFlipDirection
```

### C#

```csharp
System.bool RotationRollFlipDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool RotationRollFlipDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the direction of the camera 180, false to not

## VBA Syntax

See [Camera::RotationRollFlipDirection](ms-its:sldworksapivb6.chm::/sldworks~Camera~RotationRollFlipDirection.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::RotationRollAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle.html)
[ICamera::RotationRollBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection.html)
[ICamera::RotationRollEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
