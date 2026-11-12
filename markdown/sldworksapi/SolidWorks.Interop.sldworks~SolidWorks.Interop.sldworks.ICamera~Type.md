---
title: "Type Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "Type"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Type.html"
---

# Type Property (ICamera)

Gets or sets the type of camera.

## Syntax

### Visual Basic (Declaration)

```vb
Property Type As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Integer

instance.Type = value

value = instance.Type
```

### C#

```csharp
System.int Type {get; set;}
```

### C++/CLI

```cpp
property System.int Type {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of camera as defined in [swCameraType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCameraType_e.html)

## VBA Syntax

See [Camera::Type](ms-its:sldworksapivb6.chm::/sldworks~Camera~Type.html).

## Examples

[Turn Cameras On and Off (VBA)](Turn_Cameras_On_and_Off_Example_VB.htm)
[Turn Cameras On and Off (VB.NET)](Turn_Cameras_On_and_Off_Example_VBNET.htm)
[Turn Cameras On and Off (C#)](Turn_Cameras_On_and_Off_Example_CSharp.htm)

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::TargetPointPosition Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointPosition.html)
[ICamera::TargetPointBySelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~TargetPointBySelection.html)
[ICamera::RotationRollFlipDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~RotationRollFlipDirection.html)
[ICamera::SetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~SetTargetPointEntity.html)
[ICamera::GetTargetPointEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~GetTargetPointEntity.html)

## Availability

SOLIDWORKS 2007 SP1, Revision Number 15
