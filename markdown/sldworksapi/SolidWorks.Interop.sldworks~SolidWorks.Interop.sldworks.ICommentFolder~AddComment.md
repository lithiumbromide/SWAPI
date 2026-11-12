---
title: "AddComment Method (ICommentFolder)"
project: "SOLIDWORKS API Help"
interface: "ICommentFolder"
member: "AddComment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~AddComment.html"
---

# AddComment Method (ICommentFolder)

Adds a comment to this folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComment( _
   ByVal Text As System.String _
) As Comment
```

### Visual Basic (Usage)

```vb
Dim instance As ICommentFolder
Dim Text As System.String
Dim value As Comment

value = instance.AddComment(Text)
```

### C#

```csharp
Comment AddComment(
   System.string Text
)
```

### C++/CLI

```cpp
Comment^ AddComment(
   System.String^ Text
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Text`: Comment to add to this folder

### Return Value

Pointer to the [IComment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComment.html) object

## VBA Syntax

See [CommentFolder::AddComment](ms-its:sldworksapivb6.chm::/sldworks~CommentFolder~AddComment.html).

## Examples

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

## Remarks

To see this comment, use [IFeatureManager::UpdateFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~UpdateFeatureTree.html) to rebuild the FeatureManager design tree.

## See Also

[ICommentFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.html)
[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.html)
[IComment::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Delete.html)
[IFeature::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment.html)
[IModelDocExtension::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
