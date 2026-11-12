---
title: "GetUIState Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetUIState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUIState.html"
---

# GetUIState Method (IFeature)

Gets the user-interface state of the current feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetUIState( _
   ByVal StateType As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim StateType As System.Integer
Dim value As System.Boolean

value = instance.GetUIState(StateType)
```

### C#

```csharp
System.bool GetUIState(
   System.int StateType
)
```

### C++/CLI

```cpp
System.bool GetUIState(
   System.int StateType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StateType`: User interface state type as defined in [swUIStates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUIStates_e.html)

### Return Value

True if the state type is set, false if it is not

## VBA Syntax

See [Feature::GetUIState](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetUIState.html).

## Examples

[Hide Feature in FeatureManager Design Tree (VBA)](Hide_Feature_in_FeatureManager_Design_Tree_Example_VB.htm)
[Display of Item in FeatureManager Design Tree (C++)](Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm)

## Remarks

If you pass in the user-interface state type of swIsHiddenInFeatureMgr, this method returns True if the current feature is hidden in the FeatureManager design tree or false if the current feature is visible in the FeatureManager design tree.

The user-interface state is not a property.

To see your changes in the FeatureManager design tree, call [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html). Currently, the user-interface state data is runtime only.

Features are initialized with all user-interface state type values set to false.

A change in a feature state setting causes all the dependents of the feature to inherit the same behavior, without actually setting the state type values of those dependents. Therefore, to get the actual user-interface state value of a feature, you must check the owning feature.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::SetUIState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetUIState.html)
[IFeature::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.html)
