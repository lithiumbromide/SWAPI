---
title: "ID Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "ID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~ID.html"
---

# ID Property (ICamera)

Gets the ID for this camera.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Integer

value = instance.ID
```

### C#

```csharp
System.int ID {get;}
```

### C++/CLI

```cpp
property System.int ID {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

ID for camera

## VBA Syntax

See [Camera::ID](ms-its:sldworksapivb6.chm::/sldworks~Camera~ID.html).

## Examples

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)
[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[IModelDocExtension::GetCameraById Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCameraById.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
