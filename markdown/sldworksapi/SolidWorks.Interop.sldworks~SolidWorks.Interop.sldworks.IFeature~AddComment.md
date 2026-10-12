---
title: "AddComment Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "AddComment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~AddComment.html"
---

# AddComment Method (IFeature)

Adds a comment to this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddComment( _
   ByVal Text As System.String _
) As Comment
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
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

- `Text`: Comment to add to this feature

### Return Value

Pointer to the [IComment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComment.html) object

## VBA Syntax

See [Feature::AddComment](ms-its:sldworksapivb6.chm::/sldworks~Feature~AddComment.html).

## Remarks

The comment is added in the [Comment folder](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICommentFolder.html), but the comment is associated with this feature. If your pointer is on the feature in the FeatureManager design tree, then the comment is displayed as a ToolTip.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IComment::Delete Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Delete.html)
[IModelDocExtension::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~AddComment.html)
[ICommentFolder::AddComment Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder~AddComment.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
