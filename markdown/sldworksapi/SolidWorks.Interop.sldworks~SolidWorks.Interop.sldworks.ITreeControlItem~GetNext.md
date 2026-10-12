---
title: "GetNext Method (ITreeControlItem)"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: "GetNext"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~GetNext.html"
---

# GetNext Method (ITreeControlItem)

Gets the next sibling of this item in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNext() As TreeControlItem
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
Dim value As TreeControlItem

value = instance.GetNext()
```

### C#

```csharp
TreeControlItem GetNext()
```

### C++/CLI

```cpp
TreeControlItem^ GetNext();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Next sibling of this item in the FeatureManager design tree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem.html)

## VBA Syntax

See [TreeControlItem::GetNext](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem~GetNext.html).

## Examples

[Traverse FeatureManager Design Tree (VBA)](Traverse_FeatureManager_Design_Tree_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

## Remarks

Use [ITreeControlItem::GetPrevious](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetPrevious.html) to get the previous sibling of this item in the FeatureManager design tree.

## See Also

[ITreeControlItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html)
[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)

## Availability

SOLIDWORKS 2008 SP2, Revision Number 16.2
