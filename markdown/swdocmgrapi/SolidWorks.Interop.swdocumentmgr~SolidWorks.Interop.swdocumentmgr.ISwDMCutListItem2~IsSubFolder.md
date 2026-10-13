---
title: "IsSubFolder Property (ISwDMCutListItem2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem2"
member: "IsSubFolder"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~IsSubFolder.html"
---

# IsSubFolder Property (ISwDMCutListItem2)

Gets whether a cut-list item is a sub-folder.

**NOTE: This property is a get-only property. Set is not implemented.**

## Syntax

### Visual Basic (Declaration)

```vb
Property IsSubFolder As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem2
Dim value As System.Boolean

instance.IsSubFolder = value

value = instance.IsSubFolder
```

### C#

```csharp
System.bool IsSubFolder {get; set;}
```

### C++/CLI

```cpp
property System.bool IsSubFolder {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the cut-list item is a sub-folder, false if not

## VBA Syntax

See [SwDMCutListItem2::IsSubFolder](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem2~IsSubFolder.html).

## Remarks

A cut-list folder has either one or no child folder.

This property only supports documents saved in SOLIDWORKS 2009 or later.

## See Also

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.html)
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.html)
