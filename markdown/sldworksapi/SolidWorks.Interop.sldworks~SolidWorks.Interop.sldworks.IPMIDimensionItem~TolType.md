---
title: "TolType Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "TolType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolType.html"
---

# TolType Property (IPMIDimensionItem)

Gets the tolerance type of this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property TolType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.Integer

instance.TolType = value

value = instance.TolType
```

### C#

```csharp
System.int TolType {get; set;}
```

### C++/CLI

```cpp
property System.int TolType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tolerance type as defined in [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html)

## VBA Syntax

See [PMIDimensionItem::TolType](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~TolType.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)
[IPMIDimensionItem::MaxVariation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~MaxVariation.html)
[IPMIDimensionItem::MinVariation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~MinVariation.html)
[IPMIDimensionItem::TolerancePrecision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolerancePrecision.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
