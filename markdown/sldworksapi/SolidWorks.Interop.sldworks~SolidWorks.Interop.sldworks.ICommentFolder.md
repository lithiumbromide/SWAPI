---
title: "ICommentFolder Interface"
project: "SOLIDWORKS API Help"
interface: "ICommentFolder"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder.html"
---

# ICommentFolder Interface

Allows access to the Comment folder in the FeatureManager design tree.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICommentFolder
```

### Visual Basic (Usage)

```vb
Dim instance As ICommentFolder
```

### C#

```csharp
public interface ICommentFolder
```

### C++/CLI

```cpp
public interface class ICommentFolder
```

## VBA Syntax

See [CommentFolder](ms-its:sldworksapivb6.chm::/sldworks~CommentFolder.html).

## Examples

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

## Remarks

| To... | Then use... |
| --- | --- |
| Get comments | ICommentFolder::GetComments , which returns an array of comments ISelectionMgr::GetSelectedObject6 , which returns a single comment |
| Add comments | ICommentFolder::AddComment IFeature::AddComment IModelDocExtension::AddComment |

## Accessors

[IFeature::GetSpecificFeature2 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c303' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c3685'

## Access Diagram

[CommentFolder](SWObjectModel.pdf#CommentFolder)

## See Also

[ICommentFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.html)
