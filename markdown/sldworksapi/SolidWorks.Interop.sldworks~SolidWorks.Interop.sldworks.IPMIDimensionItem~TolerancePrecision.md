---
title: "TolerancePrecision Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "TolerancePrecision"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolerancePrecision.html"
---

# TolerancePrecision Property (IPMIDimensionItem)

Gets the tolerance precision of this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property TolerancePrecision As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.Integer

instance.TolerancePrecision = value

value = instance.TolerancePrecision
```

### C#

```csharp
System.int TolerancePrecision {get; set;}
```

### C++/CLI

```cpp
property System.int TolerancePrecision {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tolerance precision

## VBA Syntax

See [PMIDimensionItem::TolerancePrecision](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~TolerancePrecision.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This property is valid only if [IPMIDimensionItem::TolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolType.html) does not return [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html).swTolNONE.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)
[IPMIDimensionItem::TolType Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolType.html)
[IPMIDimensionItem::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Unit.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
