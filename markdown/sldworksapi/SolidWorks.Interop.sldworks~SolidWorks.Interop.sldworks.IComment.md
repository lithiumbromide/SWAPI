---
title: "IComment Interface"
project: "SOLIDWORKS API Help"
interface: "IComment"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.html"
---

# IComment Interface

Allows access to the comments in the Comment folder in the FeatureManager design tree.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IComment
```

### Visual Basic (Usage)

```vb
Dim instance As IComment
```

### C#

```csharp
public interface IComment
```

### C++/CLI

```cpp
public interface class IComment
```

## VBA Syntax

See [Comment](ms-its:sldworksapivb6.chm::/sldworks~Comment.html).

## Examples

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

## Remarks

Remarks

| To... | Then use... |
| --- | --- |
| Get comments | ICommentFolder::GetComments , which returns an array of comments ISelectionMgr::GetSelectedObject6 , which returns a single comment |
| Add comments | ICommentFolder::AddComment IFeature::AddComment IModelDocExtension::AddComment |

## Accessors

[ICommentFolder::AddComment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommentFolder~AddComment.html)

[ICommentFolder::GetComments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommentFolder~GetComments.html) and [ICommentFolder::IGetComments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommentFolder~IGetComments.html)

[IFeature::AddComment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~AddComment.html)

[IModelDocExtension::AddComment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~AddComment.html)

## Access Diagram

[Comment](SWObjectModel.pdf#Comment)

## See Also

[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[ICommentFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.html)
