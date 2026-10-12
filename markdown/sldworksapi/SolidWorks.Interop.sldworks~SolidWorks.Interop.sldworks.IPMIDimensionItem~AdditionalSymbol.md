---
title: "AdditionalSymbol Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "AdditionalSymbol"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~AdditionalSymbol.html"
---

# AdditionalSymbol Property (IPMIDimensionItem)

Gets the tolerance zone modifier for this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property AdditionalSymbol As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.Integer

instance.AdditionalSymbol = value

value = instance.AdditionalSymbol
```

### C#

```csharp
System.int AdditionalSymbol {get; set;}
```

### C++/CLI

```cpp
property System.int AdditionalSymbol {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tolerance zone modifier as defined in [swToleranceZoneModifier_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToleranceZoneModifier_e.html)

## VBA Syntax

See [PMIDimensionItem::AdditionalSymbol](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~AdditionalSymbol.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
