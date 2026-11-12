---
title: "CutlistType Property (ISwDMCutListItem4)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem4"
member: "CutlistType"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4~CutlistType.html"
---

# CutlistType Property (ISwDMCutListItem4)

Gets the type of this item's cut list.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CutlistType As swDMCutListType_e
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem4
Dim value As swDMCutListType_e

value = instance.CutlistType
```

### C#

```csharp
swDMCutListType_e CutlistType {get;}
```

### C++/CLI

```cpp
property swDMCutListType_e CutlistType {
   swDMCutListType_e get();
}
```

### Property Value

Cut list type as defined by [swDMCutListType_e](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.swDMCutListType_e.html)

## VBA Syntax

See [SwDMCutListItem4::CutListType](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem4~CutListType.html).

## See Also

[ISwDMCutListItem4 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4.html)
[ISwDMCutListItem4 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem4_members.html)

## Availability

SOLIDWORKS Document Manager API 2021 SP0
