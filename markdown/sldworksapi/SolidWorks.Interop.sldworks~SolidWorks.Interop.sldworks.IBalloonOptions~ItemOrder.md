---
title: "ItemOrder Property (IBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IBalloonOptions"
member: "ItemOrder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~ItemOrder.html"
---

# ItemOrder Property (IBalloonOptions)

Gets and sets item ordering.

## Syntax

### Visual Basic (Declaration)

```vb
Property ItemOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBalloonOptions
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

See [BalloonOptions::ItemOrder](ms-its:sldworksapivb6.chm::/sldworks~BalloonOptions~ItemOrder.html).

## Examples

See [IBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about balloons.

## See Also

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.html)
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
