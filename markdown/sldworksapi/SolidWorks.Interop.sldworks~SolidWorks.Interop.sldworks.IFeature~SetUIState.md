---
title: "SetUIState Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "SetUIState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetUIState.html"
---

# SetUIState Method (IFeature)

Sets the user-interface state of the current feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetUIState( _
   ByVal StateType As System.Integer, _
   ByVal Flag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim StateType As System.Integer
Dim Flag As System.Boolean

instance.SetUIState(StateType, Flag)
```

### C#

```csharp
void SetUIState(
   System.int StateType,
   System.bool Flag
)
```

### C++/CLI

```cpp
void SetUIState(
   System.int StateType,
   System.bool Flag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StateType`: User interface state type as defined in [swUIStates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUIStates_e.html)
- `Flag`: True to set the user-interface state, false to not

## VBA Syntax

See [Feature::SetUIState](ms-its:sldworksapivb6.chm::/sldworks~Feature~SetUIState.html).

## Examples

[Display of Item in FeatureManager Design Tree (C++)](Display_of_Item_in_Feature_Manager_Example_CPlusPlus_COM.htm)
[Hide Feature in FeatureManager Design Tree (VBA)](Hide_Feature_in_FeatureManager_Design_Tree_Example_VB.htm)

## Remarks

If you pass in StateType of swIsHiddenInFeatureMgr and flag of True, then this method hides the display of the feature in the FeatureManager design tree. To see your changes in the FeatureManager design tree , use [IModelDoc2::EditRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditRebuild3.html).

Features are initialized with all user-interface state type values set to false. However, in the case of attributes, you can use [IAttributeDef::CreateInstance5](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html) to set the desired display state of the attribute at the time of creation.

A change in a the state setting of a feature causes all its dependents to inherit the same behavior, without actually setting the state type values of those dependents. Therefore, to get the actual user-interface state value of a feature, you can query its owner.

The user-interface state is not a property.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.html)
[IFeature::GetUIState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUIState.html)
