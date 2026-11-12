---
title: "QuantityDenotationText Property (IStackedBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IStackedBalloonOptions"
member: "QuantityDenotationText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~QuantityDenotationText.html"
---

# QuantityDenotationText Property (IStackedBalloonOptions)

Gets and sets the label of BOM item quantities.

## Syntax

### Visual Basic (Declaration)

```vb
Property QuantityDenotationText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IStackedBalloonOptions
Dim value As System.String

instance.QuantityDenotationText = value

value = instance.QuantityDenotationText
```

### C#

```csharp
System.string QuantityDenotationText {get; set;}
```

### C++/CLI

```cpp
property System.String^ QuantityDenotationText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Label of BOM item quantities

## VBA Syntax

See [StackedBalloonOptions::QuantityDenotationText](ms-its:sldworksapivb6.chm::/sldworks~StackedBalloonOptions~QuantityDenotationText.html).

## Examples

See [IStackedBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IStackedBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

## See Also

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.html)
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
