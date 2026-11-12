---
title: "Text Property (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "Text"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~Text.html"
---

# Text Property (ITreeControlItem)

Gets the text for this item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Text As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As System.String

value = instance.Text
```

### C#

```csharp
System.string Text {get;}
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Text for this item in the FeatureManager design tree

## VBA Syntax

See [TreeControlItem::Text](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~Text.html).

## Examples

[Traverse FeatureManager Design Tree (VBA)](Traverse_FeatureManager_Design_Tree_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
