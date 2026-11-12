---
title: "MaxVariation Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "MaxVariation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~MaxVariation.html"
---

# MaxVariation Property (IPMIDimensionItem)

Gets the maximum variation of tolerance for this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaxVariation As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.Double

instance.MaxVariation = value

value = instance.MaxVariation
```

### C#

```csharp
System.double MaxVariation {get; set;}
```

### C++/CLI

```cpp
property System.double MaxVariation {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Maximum variation of tolerance

## VBA Syntax

See [PMIDimensionItem::MaxVariation](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~MaxVariation.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This property is valid only if [IPMIDimensionItem::TolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolType.html) returns [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html):

- swTolBILAT
- swTolLIMIT
- swTolSYMMETRIC
- swTolFITWITHTOL
- swTolFITTOLONLY

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)
[IPMIDimensionItem::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Unit.html)
[IPMIDimensionItem::TolerancePrecision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolerancePrecision.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
