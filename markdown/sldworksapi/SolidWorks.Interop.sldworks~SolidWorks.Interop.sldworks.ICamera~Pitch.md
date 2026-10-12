---
title: "Pitch Property (ICamera)"
project: "SOLIDWORKS API Help"
interface: "ICamera"
member: "Pitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera~Pitch.html"
---

# Pitch Property (ICamera)

Gets or sets the pitch (up or down angle) of a [floating camera](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICamera~Type.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Pitch As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICamera
Dim value As System.Double

instance.Pitch = value

value = instance.Pitch
```

### C#

```csharp
System.double Pitch {get; set;}
```

### C++/CLI

```cpp
property System.double Pitch {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pitch

## VBA Syntax

See [Camera::Pitch](ms-its:sldworksapivb6.chm::/sldworks~Camera~Pitch.html).

## Examples

[Insert and Rotate Camera (C#)](Insert_and_Rotate_Camera_Example_CSharp.htm)
[Insert and Rotate Camera (VB.NET)](Insert_and_Rotate_Camera_Example_VBNET.htm)
[Insert and Rotate Camera (VBA)](Insert_and_Rotate_Camera_Example_VB.htm)

## See Also

[ICamera Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera.html)
[ICamera Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html)

## Availability

SOLIDWORKS 2009 SP4, Revision Number 17.4
