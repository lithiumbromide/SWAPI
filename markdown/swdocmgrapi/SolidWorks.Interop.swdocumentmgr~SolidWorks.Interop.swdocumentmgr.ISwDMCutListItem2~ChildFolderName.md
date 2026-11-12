---
title: "ChildFolderName Property (ISwDMCutListItem2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMCutListItem2"
member: "ChildFolderName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2~ChildFolderName.html"
---

# ChildFolderName Property (ISwDMCutListItem2)

Gets the name of the cut list's child folder, if it exists.

## Syntax

### Visual Basic (Declaration)

```vb
Property ChildFolderName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMCutListItem2
Dim value As System.String

instance.ChildFolderName = value

value = instance.ChildFolderName
```

### C#

```csharp
System.string ChildFolderName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ChildFolderName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of cut list's child folder, if it exists

## VBA Syntax

See [SwDMCutListItem2::ChildFolderName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMCutListItem2~ChildFolderName.html).

## Remarks

This property only supports documents saved in SOLIDWORKS 2009 or later.

## See Also

[ISwDMCutListItem2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2.html)
[ISwDMCutListItem2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMCutListItem2_members.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
