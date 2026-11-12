---
title: "Angle Property (ISketchLine)"
project: "SOLIDWORKS API Help"
interface: "ISketchLine"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~Angle.html"
---

# Angle Property (ISketchLine)

Gets or sets the angle of the line.

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchLine
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle in radians

## VBA Syntax

See [SketchLine::Angle](ms-its:sldworksapivb6.chm::/sldworks~SketchLine~Angle.html).

## Examples

[Make Line Infinite (VBA)](Make_Line_Infinite_Example_VB.htm)

## Remarks

This property does not support lines in 3D sketches.

## See Also

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
