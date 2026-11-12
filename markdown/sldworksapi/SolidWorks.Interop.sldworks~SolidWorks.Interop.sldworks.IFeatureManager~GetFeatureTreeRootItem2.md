---
title: "GetFeatureTreeRootItem2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetFeatureTreeRootItem2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFeatureTreeRootItem2.html"
---

# GetFeatureTreeRootItem2 Method (IFeatureManager)

Gets the root item of the FeatureManager design tree in the specified pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureTreeRootItem2( _
   ByVal WhichPane As System.Integer _
) As TreeControlItem
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim WhichPane As System.Integer
Dim value As TreeControlItem

value = instance.GetFeatureTreeRootItem2(WhichPane)
```

### C#

```csharp
TreeControlItem GetFeatureTreeRootItem2(
   System.int WhichPane
)
```

### C++/CLI

```cpp
TreeControlItem^ GetFeatureTreeRootItem2(
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichPane`: FeatureManager design tree pane as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

[ITreeControlItem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITreeControlItem.html)

## VBA Syntax

See [FeatureManager::GetFeatureTreeRootItem2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetFeatureTreeRootItem2.html).

## Examples

[Expand or Collapse FeatureManager Design Tree Nodes (VBA)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_VB.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (VB.NET)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_VBNET.htm)
[Expand or Collapse FeatureManager Design Tree Nodes (C#)](Expand_and_Collapse_FeatureManager_Design_Tree_Nodes_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2012 SP04, Revision 20.4
