---
title: "ShapeIntensity Property (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "ShapeIntensity"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~ShapeIntensity.html"
---

# ShapeIntensity Property (IBreakLine)

Gets or sets the shape intensity of a jagged cut break line.

## Syntax

### Visual Basic (Declaration)

```vb
Property ShapeIntensity As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBreakLine
Dim value As System.Integer

instance.ShapeIntensity = value

value = instance.ShapeIntensity
```

### C#

```csharp
System.int ShapeIntensity {get; set;}
```

### C++/CLI

```cpp
property System.int ShapeIntensity {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Shape intensity of a jagged cut break line; valid range is 1 (most) to 5 (least) (see **Remarks**)

## VBA Syntax

See [BreakLine::ShapeIntensity](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~ShapeIntensity.html).

## Examples

[Insert Jagged Cut Break (C#)](Insert_Jagged_Cut_Break_Example_CSharp.htm)
[Insert Jagged Cut Break (VB.NET)](Insert_Jagged_Cut_Break_Example_VBNET.htm)
[Insert Jagged Cut Break (VBA)](Insert_Jagged_Cut_Break_Example_VB.htm)

## Remarks

Call [IBreakLine::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Style.html) to determine if this break line is a jagged cut break line.

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
