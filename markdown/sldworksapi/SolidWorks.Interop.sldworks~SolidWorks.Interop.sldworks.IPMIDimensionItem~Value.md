---
title: "Value Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "Value"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Value.html"
---

# Value Property (IPMIDimensionItem)

Gets the primary value of this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Value As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.Double

instance.Value = value

value = instance.Value
```

### C#

```csharp
System.double Value {get; set;}
```

### C++/CLI

```cpp
property System.double Value {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Primary value of this PMI dimension item

## VBA Syntax

See [PMIDimensionItem::Value](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~Value.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)
[IPMIDimensionItem::ValuePrecision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~ValuePrecision.html)
[IPMIDimensionItem::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Unit.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
