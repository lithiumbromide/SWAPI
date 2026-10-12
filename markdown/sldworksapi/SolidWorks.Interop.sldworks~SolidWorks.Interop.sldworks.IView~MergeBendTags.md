---
title: "MergeBendTags Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "MergeBendTags"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~MergeBendTags.html"
---

# MergeBendTags Method (IView)

Merges or unmerges bend tags in drawings of sheet metal parts.

## Syntax

### Visual Basic (Declaration)

```vb
Function MergeBendTags( _
   ByVal Merge As System.Boolean, _
   ByVal BendNotes As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Merge As System.Boolean
Dim BendNotes As System.Object
Dim value As System.Boolean

value = instance.MergeBendTags(Merge, BendNotes)
```

### C#

```csharp
System.bool MergeBendTags(
   System.bool Merge,
   System.object BendNotes
)
```

### C++/CLI

```cpp
System.bool MergeBendTags(
   System.bool Merge,
   System.Object^ BendNotes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Merge`: True to merge bend tags, false to unmerge a merged bend tag
- `BendNotes`: Array of two or more bend [tags](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) to merge or an array of one merged bend tag to unmerge

### Return Value

True if the bend tags are merged or a merged bend tag is unmerged, false if not

## VBA Syntax

See [View::MergeBendTags](ms-its:sldworksapivb6.chm::/sldworks~View~MergeBendTags.html).

## Examples

[Merge and Unmerge Bend Tags (C#)](Merge_and_Unmerge_Bend_Tags_Example_CSharp.htm)
[Merge and Unmerge Bend Tags (VB.NET)](Merge_and_Unmerge_Bend_Tags_Example_VBNET.htm)
[Merge and Unmerge Bend Tags (VBA)](Merge_and_Unmerge_Bend_Tags_Example_VB.htm)

## Remarks

| To... | Do... |
| --- | --- |
| Merge two or more bend tags | Select the bend tags to merge. Select the drawing view in which the bend tags exist. Call this method with the Merge parameter set to true. Rebuild the drawing. |
| Unmerge a merged bend tag | Select the drawing view in which the merged bend tag exists. Activate the drawing view in which the merged bend tag exists. Select the merged bend tag to unmerge. Call this method with the Merge parameter set to false. |

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[INote::IsBendLineNote Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~IsBendLineNote.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
