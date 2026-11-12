---
title: "ObjectType Property (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "ObjectType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~ObjectType.html"
---

# ObjectType Property (ITreeControlItem)

Gets the type of SOLIDWORKS object for this item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ObjectType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As System.Integer

value = instance.ObjectType
```

### C#

```csharp
System.int ObjectType {get;}
```

### C++/CLI

```cpp
property System.int ObjectType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of SOLIDWORKS object for this item in the FeatureManager design tree as defined by [swTreeControlItemType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTreeControlItemType_e.html)

## VBA Syntax

See [TreeControlItem::ObjectType](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~ObjectType.html).

## Examples

[Traverse FeatureManager Design Tree (VBA)](Traverse_FeatureManager_Design_Tree_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

## Remarks

Currently only [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) and [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) are supported. Null is returned for sub-components of an assembly loaded hidden with a selective open.

Use [ITreeControlItem::Object](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~Object.html) to get the SOLIDWORKS object associated with this item.

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
