---
title: "IsReferenceOnly Method (IPMIDimensionItem)"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: "IsReferenceOnly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~IsReferenceOnly.html"
---

# IsReferenceOnly Method (IPMIDimensionItem)

Gets whether this PMI dimension is reference only.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsReferenceOnly() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
Dim value As System.Boolean

value = instance.IsReferenceOnly()
```

### C#

```csharp
System.bool IsReferenceOnly()
```

### C++/CLI

```cpp
System.bool IsReferenceOnly();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this PMI dimension is reference-only, false if not

## VBA Syntax

See [PMIDimensionItem::IsReferenceOnly](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem~IsReferenceOnly.html).

## Remarks

If this method returns true, then this dimension item is used for information purposes only. It does not govern production or inspection operations.

## See Also

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html)
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
