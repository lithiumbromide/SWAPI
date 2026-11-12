---
title: "QuantityPlacement Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "QuantityPlacement"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~QuantityPlacement.html"
---

# QuantityPlacement Property (IStackedBalloonOptions)

Gets and sets the placement of a BOM item quantity with respect to its balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property QuantityPlacement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.QuantityPlacement = value

value = instance.QuantityPlacement
```

### C#

```csharp
System.int QuantityPlacement {get; set;}
```

### C++/CLI

```cpp
property System.int QuantityPlacement {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Placement of BOM item quantity value as defined in [swBalloonQuantityPlacement_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonQuantityPlacement_e.html); only swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Top and swBalloonQuantityPlacement_e.swBalloonQuantityPlacement_Bottom are valid options for stacked balloons

## VBA Syntax

See [StackedBalloonOptions::QuantityPlacement](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~QuantityPlacement.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
