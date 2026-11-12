---
title: "ValuePrecision Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "ValuePrecision"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~ValuePrecision.html"
---

# ValuePrecision Property (IPMIDimensionItem)

Gets the value precision of this dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property ValuePrecision As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.Integer

instance.ValuePrecision = value

value = instance.ValuePrecision
```

### C#

```csharp
System.int ValuePrecision {get; set;}
```

### C++/CLI

```cpp
property System.int ValuePrecision {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Value](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Value.html) precision

## VBA Syntax

See [PMIDimensionItem::ValuePrecision](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~ValuePrecision.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)
[IPMIDimensionItem::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Unit.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
