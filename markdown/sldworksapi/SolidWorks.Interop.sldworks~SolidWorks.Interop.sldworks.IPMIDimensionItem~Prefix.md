---
title: "Prefix Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "Prefix"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Prefix.html"
---

# Prefix Property (IPMIDimensionItem)

Gets the prefix of this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property Prefix As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.String

instance.Prefix = value

value = instance.Prefix
```

### C#

```csharp
System.string Prefix {get; set;}
```

### C++/CLI

```cpp
property System.String^ Prefix {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Prefix

## VBA Syntax

See [PMIDimensionItem::Prefix](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~Prefix.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
