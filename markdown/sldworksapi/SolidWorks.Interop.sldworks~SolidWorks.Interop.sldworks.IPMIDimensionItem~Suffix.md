---
title: "Suffix Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "Suffix"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Suffix.html"
---

# Suffix Property (IPMIDimensionItem)

Gets the suffix of this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Suffix As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.String

instance.Suffix = value

value = instance.Suffix
```

### C#

```csharp
System.string Suffix {get; set;}
```

### C++/CLI

```cpp
property System.String^ Suffix {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Suffix

## VBA Syntax

See [PMIDimensionItem::Suffix](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~Suffix.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
