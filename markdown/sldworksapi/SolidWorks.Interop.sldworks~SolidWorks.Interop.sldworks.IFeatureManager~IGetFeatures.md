---
title: "IGetFeatures Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "IGetFeatures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IGetFeatures.html"
---

# IGetFeatures Method (IFeatureManager)

Gets the features in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFeatures( _
   ByVal ToplevelOnly As System.Boolean, _
   ByVal Count As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim ToplevelOnly As System.Boolean
Dim Count As System.Integer
Dim value As Feature

value = instance.IGetFeatures(ToplevelOnly, Count)
```

### C#

```csharp
Feature IGetFeatures(
   System.bool ToplevelOnly,
   System.int Count
)
```

### C++/CLI

```cpp
Feature^ IGetFeatures(
   System.bool ToplevelOnly,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToplevelOnly`: True to get only the features at the top level of the FeatureManager design tree, false to get the top-level features and all child features in the FeatureManager design tree
- `Count`: Number of features

### Return Value

- in-process, unmanaged C++: Pointer to an array of [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IFeatureManager::GetFeatureCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~GetFeatureCount.html) before calling this method to get the size for the array of features.

If TopLevelOnly is false, then this method gets all of the feature and child features in this document. It does not get features in components.

The features that are returned by this method can be in any order. You should not rely on the order to indicate anything about children or parents. If hierarchy and order information is needed, then use [IPartDoc::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~FirstFeature.html) or [IPartDoc::IFirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPartDoc~IFirstFeature.html) or [IModelDoc2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~FirstFeature.html) or [IModelDoc2::FirstFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IFirstFeature.html), [IFeature::GetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextFeature.html) or [IFeatureIGetNextFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextFeature.html), [IFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstSubFeature.html) or [IFeature::IGetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFirstSubFeature.html), and [IFeature::GetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextSubFeature.html) or [IFeature::IGetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextSubFeature.html) to retrieve your information.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFeatures.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::GetOwnerFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetOwnerFeature.html)
[IFeature::GetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html)
[IFeature::IGetChildCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildCount.html)
[IFeature::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.html)
[IFeature::IGetParentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParentCount.html)
[IFeature::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.html)
[IComponent2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FirstFeature.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
