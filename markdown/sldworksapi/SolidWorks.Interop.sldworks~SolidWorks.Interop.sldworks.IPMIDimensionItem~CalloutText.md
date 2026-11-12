---
title: "CalloutText Property (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "CalloutText"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~CalloutText.html"
---

# CalloutText Property (IPMIDimensionItem)

Gets the callout value for this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Property CalloutText As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.String

instance.CalloutText = value

value = instance.CalloutText
```

### C#

```csharp
System.string CalloutText {get; set;}
```

### C++/CLI

```cpp
property System.String^ CalloutText {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Callout value

## VBA Syntax

See [PMIDimensionItem::CalloutText](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~CalloutText.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
