---
title: "IsBendLineNote Property (INote)"
project: "SOLIDWORKS API Help"
interface: "INote"
member: "IsBendLineNote"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBendLineNote.html"
---

# IsBendLineNote Property (INote)

Gets whether this note is a bendline note.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsBendLineNote As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As INote
Dim value As System.Boolean

value = instance.IsBendLineNote
```

### C#

```csharp
System.bool IsBendLineNote {get;}
```

### C++/CLI

```cpp
property System.bool IsBendLineNote {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if note is a bendline note, false if not

## VBA Syntax

See [Note::IsBendLineNote](ms-its:sldworksapivb6.chm::/sldworks~Note~IsBendLineNote.html).

## Examples

[Merge and Unmerge Bend Tags (C#)](Merge_and_Unmerge_Bend_Tags_Example_CSharp.htm)
[Merge and Unmerge Bend Tags (VB.NET)](Merge_and_Unmerge_Bend_Tags_Example_VBNET.htm)
[Merge and Unmerge Bend Tags (VBA)](Merge_and_Unmerge_Bend_Tags_Example_VB.htm)

## See Also

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html)
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html)
[INote::GetBendLineValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~GetBendLineValues.html)
[IView::MergeBendTags Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~MergeBendTags.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
