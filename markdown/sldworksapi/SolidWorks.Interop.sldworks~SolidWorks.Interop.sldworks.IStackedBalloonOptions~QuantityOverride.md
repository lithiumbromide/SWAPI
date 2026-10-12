---
title: "QuantityOverride Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "QuantityOverride"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~QuantityOverride.html"
---

# QuantityOverride Property (IStackedBalloonOptions)

Gets and sets whether to override the BOM item quantities.

## Syntax

### Visual Basic (Declaration)

```vb
Property QuantityOverride As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.Boolean

instance.QuantityOverride = value

value = instance.QuantityOverride
```

### C#

```csharp
System.bool QuantityOverride {get; set;}
```

### C++/CLI

```cpp
property System.bool QuantityOverride {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override BOM item quantities, false to not

## VBA Syntax

See [StackedBalloonOptions::QuantityOverride](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~QuantityOverride.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
