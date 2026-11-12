---
title: "GetFeatureCount Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetFeatureCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFeatureCount.html"
---

# GetFeatureCount Method (IFeatureManager)

Gets the number of features in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureCount( _
   ByVal ToplevelOnly As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim ToplevelOnly As System.Boolean
Dim value As System.Integer

value = instance.GetFeatureCount(ToplevelOnly)
```

### C#

```csharp
System.int GetFeatureCount(
   System.bool ToplevelOnly
)
```

### C++/CLI

```cpp
System.int GetFeatureCount(
   System.bool ToplevelOnly
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ToplevelOnly`: True to get only the number of features at the top level of the FeatureManager design tree, false to get the number of top-level features and all child features in the FeatureManager design tree

### Return Value

Number of features

## VBA Syntax

See [FeatureManager::GetFeatureCount](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetFeatureCount.html).

## Examples

[Create Loft Body (VB.NET)](Create_Loft_Body_Example_VBNET.htm)
[Create Loft Body (VBA)](Create_Loft_Body_Example_VB.htm)
[Create Loft Body (C#)](Create_Loft_Body_Example_CSharp.htm)

## Remarks

Call this method before calling [IFeatureManager::IGetFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IGetFeatures.html) to determine the size of the array to pass into that method.

If TopLevelOnly is false, then this method counts all of the feature and child features in this document. It does not count features in components.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeature::GetFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFeatures.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::GetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.html)
[IFeature::GetNextFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextFeature.html)
[IFeature::GetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.html)
[IFeature::GetOwnerFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetOwnerFeature.html)
[IFeature::GetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html)
[IFeature::IGetChildCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildCount.html)
[IFeature::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.html)
[IFeature::IGetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.html)
[IFeature::IGetNextFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextFeature.html)
[IFeature::IGetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.html)
[IFeature::IGetParentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParentCount.html)
[IFeature::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.html)
[IModelDoc2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FirstFeature.html)
[IModelDoc2::GetFeatureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetFeatureCount.html)
[IPartDoc::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FirstFeature.html)
[IComponent2::FirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FirstFeature.html)
[IModelDoc2::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFirstFeature.html)
[IPartDoc::IFirstFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IFirstFeature.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
