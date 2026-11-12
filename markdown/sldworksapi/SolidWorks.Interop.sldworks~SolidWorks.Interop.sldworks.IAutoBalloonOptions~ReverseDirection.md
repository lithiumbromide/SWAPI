---
title: "ReverseDirection Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "ReverseDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~ReverseDirection.html"
---

# ReverseDirection Property (IAutoBalloonOptions)

Gets and sets whether to reverse the item ordering of the balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.Boolean

instance.ReverseDirection = value

value = instance.ReverseDirection
```

### C#

```csharp
System.bool ReverseDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to reverse the item ordering, false to not; only valid when [IAutoBalloonOptions::ItemOrder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions~ItemOrder.html) is set to [swBalloonItemNumbersOrder_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonItemNumbersOrder_e.html).swBalloonItemNumbers_OrderSequentially

## VBA Syntax

See [AutoBalloonOptions::ReverseDirection](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~ReverseDirection.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
