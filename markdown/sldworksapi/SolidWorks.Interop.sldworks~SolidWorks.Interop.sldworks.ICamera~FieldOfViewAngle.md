---
title: "FieldOfViewAngle Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "FieldOfViewAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewAngle.html"
---

# FieldOfViewAngle Property (ICamera)

Gets the camera's horizontal angle of the field of view.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property FieldOfViewAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Double

instance.FieldOfViewAngle = value

value = instance.FieldOfViewAngle
```

### C#

```csharp
System.double FieldOfViewAngle {get; set;}
```

### C++/CLI

```cpp
property System.double FieldOfViewAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Camera's horizontal angle of the field of view in radians

## VBA Syntax

See [Camera::FieldOfViewAngle](ms-its:sldworksapivb6.chm::/sldworks~Camera~FieldOfViewAngle.html).

## Examples

[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)
[Insert Camera (C#)](Insert_Camera_Example_CSharp.htm)
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)

## Remarks

This property is only meaningful for a perspective camera.

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::FieldOfViewDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewDepth.html)
[ICamera::FieldOfViewHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewHeight.html)
[ICamera::Perspective Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Perspective.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
