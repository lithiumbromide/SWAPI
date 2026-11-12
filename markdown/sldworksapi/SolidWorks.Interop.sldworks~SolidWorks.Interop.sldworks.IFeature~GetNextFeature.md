---
title: "GetNextFeature Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetNextFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.html"
---

# GetNextFeature Method (IFeature)

Gets the next feature in the part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetNextFeature()
```

### C#

```csharp
System.object GetNextFeature()
```

### C++/CLI

```cpp
System.Object^ GetNextFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [Feature::GetNextFeature](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetNextFeature.html).

## Examples

[Iterate through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)
[Select Plane (VBA)](Select_Plane_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Suppress or Unsuppress Feature (VBA)](Feature_Suppression_Example_VB.htm)
[Traverse All Cosmetic Threads (VBA)](Traverse_All_Cosmetic_Threads_Example_VB.htm)
[Traverse Assembly at Component and Feature Level (VBA)](Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm)
[Traverse Subfeatures (VBA)](Traverse_SubFeatures_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)

## Remarks

This method:

- allows you to access suppressed features.
- returns features in the current order for the model, and this order changes when the model is edited.

Your application should not assume that:

- features retain the same relative or absolute position throughout the model’s lifetime. For example, you should not assume that Sketch1 always appears before Sketch2.
- any feature has a specific name. Because features can be renamed, you cannot assume that the first reference plane feature is named Plane1.

When traversing the FeatureManager design tree, your application should use [IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.html) and [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html) to identify specific features instead of relying solely on [IFeature::Name](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Name.html).

This method returns features in the model definition order, which is not the same as the order displayed in the user interface. See [ITreeControlItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITreeControlItem.html) for details.

[IFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstSubFeature.html) and [IFeature::IGetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFirstSubFeature.html) provide access to subfeatures.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.html)
[IFeature::IGetNextFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.html)
[IFeature::IGetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.html)
[IComponent::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FirstFeature.html)
[IPartDoc::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.html)
[IPartDoc::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFirstFeature.html)
[IModelDoc2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.html)
[IModelDoc2::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.html)
