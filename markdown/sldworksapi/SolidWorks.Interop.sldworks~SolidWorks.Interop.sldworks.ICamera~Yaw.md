---
title: "Yaw Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "Yaw"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Yaw.html"
---

# Yaw Property (ICamera)

Gets or sets the yaw (side-to-side angle) of a [floating camera](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICamera~Type.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Yaw As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Double

instance.Yaw = value

value = instance.Yaw
```

### C#

```csharp
System.double Yaw {get; set;}
```

### C++/CLI

```cpp
property System.double Yaw {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Yaw

## VBA Syntax

See [Camera::Yaw](ms-its:sldworksapivb6.chm::/sldworks~Camera~Yaw.html).

## Examples

[Insert and Rotate Camera (C#)](Insert_and_Rotate_Camera_Example_CSharp.htm)
[Insert and Rotate Camera (VB.NET)](Insert_and_Rotate_Camera_Example_VBNET.htm)
[Insert and Rotate Camera (VBA)](Insert_and_Rotate_Camera_Example_VB.htm)

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)

## Availability

SOLIDWORKS 2009 SP4, Revision Number 17.4
