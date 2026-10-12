---
title: "Color Property (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Color"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Color.html"
---

# Color Property (ISketchHatch)

Gets or sets the sketch hatch line color.

## Syntax

### Visual Basic (Declaration)

```vb
Property Color As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
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

COLORREF value

## VBA Syntax

See [SketchHatch::Color](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Color.html).

## Examples

See the [ISketchHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html) examples.

## Examples

[Override Layer Color for Area Hatch (VBA)](Override_Layer_Color_for_Area_Hatch_Example_VB.htm)

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
