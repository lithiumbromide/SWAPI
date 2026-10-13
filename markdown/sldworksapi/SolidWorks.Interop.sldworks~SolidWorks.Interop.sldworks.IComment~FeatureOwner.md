---
title: "FeatureOwner Property (IComment)"
project: "SOLIDWORKS API Help"
interface: "IComment"
member: "FeatureOwner"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~FeatureOwner.html"
---

# FeatureOwner Property (IComment)

Gets the feature that owns this comment.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureOwner As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IComment
Dim value As Feature

value = instance.FeatureOwner
```

### C#

```csharp
Feature FeatureOwner {get;}
```

### C++/CLI

```cpp
property Feature^ FeatureOwner {
   Feature^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object that owns this comment

## VBA Syntax

See [Comment::FeatureOwner](ms-its:sldworksapivb6.chm::/sldworks~Comment~FeatureOwner.html).

## Remarks

If the comment is not owned by a feature, then NULL is returned.

Because you cannot set the name of comment owned by a feature, use this property before using [IComment::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComment~Name.html) to determine if the comment is owned by a feature.

## See Also

[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.html)
[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
