---
title: "GetNextSubFeature Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetNextSubFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.html"
---

# GetNextSubFeature Method (IFeature)

Gets the next sub-feature from the owner of this sub-feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextSubFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetNextSubFeature()
```

### C#

```csharp
System.object GetNextSubFeature()
```

### C++/CLI

```cpp
System.Object^ GetNextSubFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next sub-[feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [Feature::GetNextSubFeature](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetNextSubFeature.html).

## Examples

[Iterate Through Dimensions in Model (VBA)](Iterate_Through_Dimensions_in_Model_Example_VB.htm)
[Traverse All Cosmetic Threads (VBA)](Traverse_All_Cosmetic_Threads_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels (VBA)](Traverse_Assembly_at_Component_and_Feature_Level_Example_VB.htm)
[Traverse Subfeatures (VBA)](Traverse_SubFeatures_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VBA)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VB.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (VB.NET)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_VBNET.htm)
[Traverse Assembly at Component and Feature Levels Using Recursion (C#)](Traverse_Assembly_at_Component_and_Feature_Levels_Using_Recursion_Example_CSharp.htm)

## Remarks

If no sub-feature exists, then this method returns NULL.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IGetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.html)
[IFeature::MakeSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MakeSubFeature.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::GetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.html)
[IFeature::GetNextFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.html)
[IFeature::IGetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.html)
[IFeature::IGetNextFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.html)
[IComponent2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FirstFeature.html)
[IModelDoc2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.html)
[IModelDoc2::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.html)
[IPartDoc::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.html)
[IPartDoc::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFirstFeature.html)
[IFeature::GetOwnerFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetOwnerFeature.html)
