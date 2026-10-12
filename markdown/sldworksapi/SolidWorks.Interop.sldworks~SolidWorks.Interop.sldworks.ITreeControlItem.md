---
title: "ITreeControlItem Interface"
project: "SOLIDWORKS API Help"
interface: "ITreeControlItem"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html"
---

# ITreeControlItem Interface

Allows you to traverse items in the FeatureManager design tree exactly as they appear in the FeatureManager design tree.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITreeControlItem
```

### Visual Basic (Usage)

```vb
Dim instance As ITreeControlItem
```

### C#

```csharp
public interface ITreeControlItem
```

### C++/CLI

```cpp
public interface class ITreeControlItem
```

## VBA Syntax

See [TreeControlItem](ms-its:sldworksapivb6.chm::/sldworks~TreeControlItem.html).

## Examples

[Traverse FeatureManager Design Tree (VBA)](Traverse_FeatureManager_Design_Tree_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

## Remarks

ITreeControlItem objects are released whenever the FeatureManager design tree is rebuilt (e.g., add or remove features, rebuild the model, etc.).

## Accessors

[IFeatureManager::GetFeatureTreeRootItem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~GetFeatureTreeRootItem.html)

[ITreeControlItem::GetFirstChild](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetFirstChild.html)

[ITreeControlItem::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetNext.html)

[ITreeControlItem::GetParent](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetParent.html)

[ITreeControlItem::GetPrevious](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetPrevious.html)

[ITreeControlItem::GetRoot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem~GetRoot.html)

## Access Diagram

[TreeControlItem](SWObjectModel.pdf#TreeControlItem)

## See Also

[ITreeControlItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
