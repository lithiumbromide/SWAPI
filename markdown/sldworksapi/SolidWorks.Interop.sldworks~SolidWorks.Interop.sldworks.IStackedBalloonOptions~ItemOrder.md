---
title: "ItemOrder Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "ItemOrder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~ItemOrder.html"
---

# ItemOrder Property (IStackedBalloonOptions)

Gets and sets item ordering.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Integer

instance.ItemOrder = value

value = instance.ItemOrder
```

### C#

```csharp
System.int ItemOrder {get; set;}
```

### C++/CLI

```cpp
property System.int ItemOrder {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Item ordering as defined in [swBalloonItemNumbersOrder_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonItemNumbersOrder_e.html)

## VBA Syntax

See [StackedBalloonOptions::ItemOrder](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~ItemOrder.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
