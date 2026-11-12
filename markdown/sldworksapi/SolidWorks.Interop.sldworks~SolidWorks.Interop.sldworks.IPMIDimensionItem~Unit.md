---
title: "Unit Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "Unit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Unit.html"
---

# Unit Property (IPMIDimensionItem)

Gets the units of this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.Integer

instance.Unit = value

value = instance.Unit
```

### C#

```csharp
System.int Unit {get; set;}
```

### C++/CLI

```cpp
property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Units of dimension as defined in [swPMIUnit_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIUnit_e.html)

## VBA Syntax

See [PMIDimensionItem::Unit](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~Unit.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)
[IPMIDimensionItem::Value Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Value.html)
[IPMIDimensionItem::MaxVariation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~MaxVariation.html)
[IPMIDimensionItem::MinVariation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~MinVariation.html)
[IPMIDimensionItem::TolerancePrecision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolerancePrecision.html)
[IPMIDimensionItem::ValuePrecision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~ValuePrecision.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
