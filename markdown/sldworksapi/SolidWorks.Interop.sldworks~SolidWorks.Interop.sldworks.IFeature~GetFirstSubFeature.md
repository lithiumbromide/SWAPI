---
title: "GetFirstSubFeature Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetFirstSubFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.html"
---

# GetFirstSubFeature Method (IFeature)

Gets the first sub-feature that belongs to this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstSubFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetFirstSubFeature()
```

### C#

```csharp
System.object GetFirstSubFeature()
```

### C++/CLI

```cpp
System.Object^ GetFirstSubFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First sub-feature of this [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [Feature::GetFirstSubFeature](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetFirstSubFeature.html).

## Examples

[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)
[Traverse All Cosmetic Threads (VBA)](Traverse_All_Cosmetic_Threads_Example_VB.htm)
[Traverse Subfeatures (VBA)](Traverse_SubFeatures_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)

## Remarks

If no sub-features exist for this feature, then this method returns NULL.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.html)
[IFeature::IGetNextFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.html)
[IFeature::IGetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.html)
[IFeatureManager::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFeatures.html)
[IFeatureManager::IGetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IGetFeatures.html)
[IModelDoc2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.html)
[IModelDoc2::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.html)
[IPartDoc::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.html)
[IPartDoc::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFirstFeature.html)
[IComponent2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FirstFeature.html)
[IFeature::MakeSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MakeSubFeature.html)
