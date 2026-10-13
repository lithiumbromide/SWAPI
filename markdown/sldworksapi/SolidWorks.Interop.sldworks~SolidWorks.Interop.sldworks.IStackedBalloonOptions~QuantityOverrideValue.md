---
title: "QuantityOverrideValue Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "QuantityOverrideValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~QuantityOverrideValue.html"
---

# QuantityOverrideValue Property (IStackedBalloonOptions)

Gets and sets the override value for BOM item quantities.

## Syntax

### Visual Basic (Declaration)

```vb
Property QuantityOverrideValue As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.String

instance.QuantityOverrideValue = value

value = instance.QuantityOverrideValue
```

### C#

```csharp
System.string QuantityOverrideValue {get; set;}
```

### C++/CLI

```cpp
property System.String^ QuantityOverrideValue {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

BOM item quantity override value; valid only when [IStackedBalloonOptions::QuantityOverride](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions~QuantityOverride.html) is true

## VBA Syntax

See [StackedBalloonOptions::QuantityOverrideValue](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~QuantityOverrideValue.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
