---
title: "ItemOrder Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "ItemOrder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~ItemOrder.html"
---

# ItemOrder Property (IAutoBalloonOptions)

Gets and sets item ordering.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
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

See [AutoBalloonOptions::ItemOrder](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~ItemOrder.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
