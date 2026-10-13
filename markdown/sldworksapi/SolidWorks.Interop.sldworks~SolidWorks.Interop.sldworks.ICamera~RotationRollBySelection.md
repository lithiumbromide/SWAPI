---
title: "RotationRollBySelection Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "RotationRollBySelection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection.html"
---

# RotationRollBySelection Property (ICamera)

Gets or sets whether you can select the camera's rotation roll direction.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationRollBySelection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Boolean

instance.RotationRollBySelection = value

value = instance.RotationRollBySelection
```

### C#

```csharp
System.bool RotationRollBySelection {get; set;}
```

### C++/CLI

```cpp
property System.bool RotationRollBySelection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if you can select the camera's rotation roll, false if not

## VBA Syntax

See [Camera::RotationRollBySelection](ms-its:sldworksapivb6.chm::/sldworks~Camera~RotationRollBySelection.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::RotationRollAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle.html)
[ICamera::RotationRollEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity.html)
[ICamera::RotationRollFlipDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
