---
title: "ExpandFeature Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ExpandFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ExpandFeature.html"
---

# ExpandFeature Method (IFeatureManager)

Expands the specified component in the specified FeatureManager design tree pane.

## Syntax

### Visual Basic (Declaration)

```vb
Function ExpandFeature( _
   ByVal Component As System.Object, _
   ByVal FeatureName As System.String, _
   ByVal WhichPane As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Component As System.Object
Dim FeatureName As System.String
Dim WhichPane As System.Integer
Dim value As System.Boolean

value = instance.ExpandFeature(Component, FeatureName, WhichPane)
```

### C#

```csharp
System.bool ExpandFeature(
   System.object Component,
   System.string FeatureName,
   System.int WhichPane
)
```

### C++/CLI

```cpp
System.bool ExpandFeature(
   System.Object^ Component,
   System.String^ FeatureName,
   System.int WhichPane
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Component`: [Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
- `FeatureName`: Name of a feature in Component
- `WhichPane`: FeatureManager design tree pane in which to expand Component as defined in [swFeatMgrPane_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatMgrPane_e.html)

### Return Value

True if the specified component is expanded in the specified FeatureManager design tree pane, false if not

## VBA Syntax

See [FeatureManager::ExpandFeature](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ExpandFeature.html).

## Examples

[Expand Component in Specified FeatureManager Design Tree Pane (C#)](Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_CSharp.htm)
[Expand Component in Specified FeatureManager Design Tree Pane (VB.NET)](Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_VBNET.htm)
[Expand Component in Specified FeatureManager Design Tree Pane (VBA)](Expand_Component_in_Specified_FeatureManager_Design_Tree_Pane_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ITreeControlItem::Expanded Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem~Expanded.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
