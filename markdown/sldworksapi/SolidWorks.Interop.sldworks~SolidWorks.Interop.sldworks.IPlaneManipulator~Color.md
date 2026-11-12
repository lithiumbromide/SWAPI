---
title: "Color Property (IPlaneManipulator)"
project: "SOLIDWORKS API Help"
interface: "IPlaneManipulator"
member: "Color"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Color.html"
---

# Color Property (IPlaneManipulator)

Gets or sets the color of a plane.

## Syntax

### Visual Basic (Declaration)

```vb
Property Color As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPlaneManipulator
Dim value As System.Integer

instance.Color = value

value = instance.Color
```

### C#

```csharp
System.int Color {get; set;}
```

### C++/CLI

```cpp
property System.int Color {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

RGB color for plane

## VBA Syntax

See [PlaneManipulator::Color](ms-its:sldworksapivb6.chm::/sldworks~PlaneManipulator~Color.html).

## Examples

[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)
[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)

## See Also

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
