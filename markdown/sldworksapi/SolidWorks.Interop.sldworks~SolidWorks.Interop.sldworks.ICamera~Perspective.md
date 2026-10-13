---
title: "Perspective Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "Perspective"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Perspective.html"
---

# Perspective Property (ICamera)

Gets whether the camera is in perspective mode or not.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Perspective As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Boolean

instance.Perspective = value

value = instance.Perspective
```

### C#

```csharp
System.bool Perspective {get; set;}
```

### C++/CLI

```cpp
property System.bool Perspective {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if camera is in perspective mode, false if not

## VBA Syntax

See [Camera::Perspective](ms-its:sldworksapivb6.chm::/sldworks~Camera~Perspective.html).

## Examples

[Insert Camera (C#)](Insert_Cavity_Example_CSharp.htm)
[Insert Camera (VB.NET)](Insert_Camera_Example_VBNET.htm)
[Insert Camera (VBA)](Insert_Camera_Example_VB.htm)

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)
[ICamera::FieldOfViewAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewAngle.html)
[ICamera::FieldOfViewDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewDepth.html)
[ICamera::FieldOfViewHeight Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~FieldOfViewHeight.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
