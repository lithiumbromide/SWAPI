---
title: "Expanded Property (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "Expanded"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~Expanded.html"
---

# Expanded Property (ITreeControlItem)

Gets or sets whether to expand this item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property Expanded As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As System.Boolean

instance.Expanded = value

value = instance.Expanded
```

### C#

```csharp
System.bool Expanded {get; set;}
```

### C++/CLI

```cpp
property System.bool Expanded {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to expand, false to collapse

## VBA Syntax

See [TreeControlItem::Expanded](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~Expanded.html).

## Examples

[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)
[IFeatureManager::ExpandFeature Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ExpandFeature.html)

## Availability

SOLIDWORKS 2012 SP04, Revision 20.4
