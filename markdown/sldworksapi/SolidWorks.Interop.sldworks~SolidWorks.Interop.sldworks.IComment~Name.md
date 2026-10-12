---
title: "Name Property (IComment)"
project: "SOLIDWORKS API Help"
interface: "IComment"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment~Name.html"
---

# Name Property (IComment)

Gets or sets the name of the comment as it appears in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComment
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the comment as it appears in the FeatureManager design tree

## VBA Syntax

See [Comment::Name](ms-its:sldworksapivb6.chm::/sldworks~Comment~Name.html).

## Examples

[Get Comments in Comments Folder (C#)](Get_Comments_in_Comments_Folder_Example_CSharp.htm)
[Get Comments in Comments Folder (VB.NET)](Get_Comments_in_Comments_Folder_Example_VBNET.htm)
[Get Comments in Comments Folder (VBA)](Get_Comments_in_Comments_Folder_Example_VB.htm)

## Remarks

You cannot set this property if the comment is owned by a feature because the name of the comment always matches the name of the feature that owns it. To determine if a comment is owned by a feature, use [IComment::FeatureOwner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComment~FeatureOwner.html).

You must rebuild the FeatureManager design tree after setting the name of a comment. Use [IFeatureManager::UpdateFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~UpdateFeatureTree.html) to perform this action.

## See Also

[IComment Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment.html)
[IComment Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
