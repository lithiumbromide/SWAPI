---
title: "ExcludeFromCutlist Property (ISwDMCutListItem4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem4"
member: "ExcludeFromCutlist"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4~ExcludeFromCutlist.html"
---

# ExcludeFromCutlist Property (ISwDMCutListItem4)

Gets whether this item is excluded from the cut list.

**NOTE: This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property ExcludeFromCutlist As swDMCutListExclusionStatus_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem4
Dim value As swDMCutListExclusionStatus_e

instance.ExcludeFromCutlist = value

value = instance.ExcludeFromCutlist
```

### C#

```csharp
swDMCutListExclusionStatus_e ExcludeFromCutlist {get; set;}
```

### C++/CLI

```cpp
property swDMCutListExclusionStatus_e ExcludeFromCutlist {
   swDMCutListExclusionStatus_e get();
   void set (    swDMCutListExclusionStatus_e value);
}
```

### Property Value

As defined by [swDMCutListExclusionStatus _e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDMCutListExclusionStatus_e.html)

## VBA Syntax

See [SwDMCutListItem4::ExcludeFromCutlist](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem4~ExcludeFromCutlist.html).

## Remarks

This property is only valid for documents saved in SOLIDWORKS 2021 or later.

## See Also

[ISwDMCutListItem4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4.html)
[ISwDMCutListItem4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4_members.html)

## Availability

SOLIDWORKS Document Manager API 2021 SP0
