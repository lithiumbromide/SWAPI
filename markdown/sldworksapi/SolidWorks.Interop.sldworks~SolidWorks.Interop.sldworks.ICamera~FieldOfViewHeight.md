---
title: "FieldOfViewHeight Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "FieldOfViewHeight"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewHeight.html"
---

# FieldOfViewHeight Property (ICamera)

Gets the camera's height of the field of view.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property FieldOfViewHeight As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Double

instance.FieldOfViewHeight = value

value = instance.FieldOfViewHeight
```

### C#

```csharp
System.double FieldOfViewHeight {get; set;}
```

### C++/CLI

```cpp
property System.double FieldOfViewHeight {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Camera's height of the field of view

## VBA Syntax

See [Camera::FieldOfViewHeight](ms-its:sldworksapivb6.chm::/sldworks~Camera~FieldOfViewHeight.html).

## Examples

[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

## Remarks

This property is only meaningful for a perspective camera.

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::FieldOfViewAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewAngle.html)
[ICamera::FieldOfViewDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewDepth.html)
[ICamera::Perspective Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Perspective.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
