---
title: "Width Property (IPlaneManipulator)"
project: "SOLIDWORKS API Help"
interface: "IPlaneManipulator"
member: "Width"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator~Width.html"
---

# Width Property (IPlaneManipulator)

Gets or sets the width of a plane that has a manipulator.

## Syntax

### Visual Basic (Declaration)

```vb
Property Width As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPlaneManipulator
Dim value As System.Double

instance.Width = value

value = instance.Width
```

### C#

```csharp
System.double Width {get; set;}
```

### C++/CLI

```cpp
property System.double Width {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Width of a plane that has a manipulator

## VBA Syntax

See [PlaneManipulator::Width](ms-its:sldworksapivb6.chm::/sldworks~PlaneManipulator~Width.html).

## Examples

[Insert and Use Plane with Manipulator (VBA)](Insert_and_Use_Plane_with_Manipulator_Example_VB.htm)
[Insert and Use Plane with Manipulator (C#)](Insert_and_Use_Plane_with_Manipulator_Example_CSharp.htm)
[Insert and Use Plane with Manipulator (VB.NET)](Insert_and_Use_Plane_with_Manipulator_Example_VBNET.htm)

## See Also

[IPlaneManipulator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator.html)
[IPlaneManipulator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
