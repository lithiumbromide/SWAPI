---
title: "RotationRollEntity Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "RotationRollEntity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollEntity.html"
---

# RotationRollEntity Property (ICamera)

Gets or sets the entity (line, edge, face, or plane) that defines the camera's rotation up direction.

## Syntax

### Visual Basic (Declaration)

```vb
Property RotationRollEntity As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Object

instance.RotationRollEntity = value

value = instance.RotationRollEntity
```

### C#

```csharp
System.object RotationRollEntity {get; set;}
```

### C++/CLI

```cpp
property System.Object^ RotationRollEntity {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the entity (line, edge, face, or plane) that defines the camera's rotation up direction

## VBA Syntax

See [Camera::RotationRollEntity](ms-its:sldworksapivb6.chm::/sldworks~Camera~RotationRollEntity.html).

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::RotationRollAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollAngle.html)
[ICamera::RotationRollBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollBySelection.html)
[ICamera::RotationRollFlipDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
