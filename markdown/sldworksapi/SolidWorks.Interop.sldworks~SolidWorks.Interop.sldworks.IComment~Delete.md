---
title: "Delete Method (IComment)"
project: "SOLIDWORKS API Help"
interface: "IComment"
member: "Delete"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Delete.html"
---

# Delete Method (IComment)

Deletes a comment.

## Syntax

### Visual Basic (Declaration)

```vb
Function Delete() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComment
Dim value As System.Boolean

value = instance.Delete()
```

### C#

```csharp
System.bool Delete()
```

### C++/CLI

```cpp
System.bool Delete();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the comment is deleted, false if not

## VBA Syntax

See [Comment::Delete](ms-its:sldworksapivb6.chm::/sldworks~Comment~Delete.html).

## Remarks

The comment to delete must not be selected in the FeatureManager design tree. Use [IModelDoc2::ClearSelection2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ClearSelection2.html) to ensure that the comment is not currently selected.

You must rebuild the FeatureManager design tree after deleting the comment. Use [IFeatureManager::UpdateFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~UpdateFeatureTree.html) to perform this action.

## See Also

[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.html)
[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.html)
[ICommentFolder::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~AddComment.html)
[IFeature::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment.html)
[IModelDocExtension::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
