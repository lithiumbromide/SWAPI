---
title: "AddComment Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "AddComment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment.html"
---

# AddComment Method (IModelDocExtension)

Adds a comment to this document's Comment Folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComment( _
   ByVal Text As System.String _
) As Comment
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
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

- `Text`: Comment to add to the document's Comment folder

### Return Value

[Comment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComment.html) folder

## VBA Syntax

See [ModelDocExtension::AddComment](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~AddComment.html).

## Examples

[Add Comment to Assembly Component (VBA)](Add_Comment_to_Assembly_Component_Example_VB.htm)
[Add Comment to Assembly Component (VB.NET)](Add_Comment_to_Assembly_Component_Example_VBNET.htm)
[Add Comment to Assembly Component (C#)](Add_Comment_to_Assembly_Component_Example_CSharp.htm)

## Remarks

A comment is added to the document's Comment folder, and the comment is associated with the preselected item when this method is run.

For example:

| If... | Then the comment is... |
| --- | --- |
| A feature is preselected | Associated with the feature (equivalent to running the IFeature::AddComment on the selected feature) |
| The Comment folder is preselected | Not associated with any feature, but is added to the Comment folder (equivalent to running the ICommentFolder::AddComment method) |

Although it might appear that ModelDocExtension::AddComment duplicates IFeature::AddComment and ICommentFolder::AddComment, IModelDocExtension::AddComment is used when recording macros, so it is different. IModelDocExtension::AddComment shares code with the user interface, so it should behave identical to the user interface.

IModelDocExtension::AddComment rebuilds the FeatureManager design tree automatically, which can be a time-consuming operation if the FeatureManager design tree gets large. Take this into consideration before using it.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IComment::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Delete.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
