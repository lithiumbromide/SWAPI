---
title: "GetFirstChild Method (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "GetFirstChild"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetFirstChild.html"
---

# GetFirstChild Method (ITreeControlItem)

Gets the first child of this item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstChild() As TreeControlItem
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As TreeControlItem

value = instance.GetFirstChild()
```

### C#

```csharp
TreeControlItem GetFirstChild()
```

### C++/CLI

```cpp
TreeControlItem^ GetFirstChild();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[First child of this item in the FeatureManager design tree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem.html)

## VBA Syntax

See [TreeControlItem::GetFirstChild](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~GetFirstChild.html).

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
