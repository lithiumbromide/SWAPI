---
title: "EditFreeze Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "EditFreeze"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.html"
---

# EditFreeze Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::EditFreeze2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~EditFreeze2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function EditFreeze( _
   ByVal Location As System.Integer, _
   ByVal FeatureName As System.String, _
   ByVal UpdateAllConfigs As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Location As System.Integer
Dim FeatureName As System.String
Dim UpdateAllConfigs As System.Boolean
Dim value As System.Integer

value = instance.EditFreeze(Location, FeatureName, UpdateAllConfigs)
```

### C#

```csharp
System.int EditFreeze(
   System.int Location,
   System.string FeatureName,
   System.bool UpdateAllConfigs
)
```

### C++/CLI

```cpp
System.int EditFreeze(
   System.int Location,
   System.String^ FeatureName,
   System.bool UpdateAllConfigs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Location`: Location as defined in [swMoveFreezeBarTo_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveFreezeBarTo_e.html)
- `FeatureName`: Name of the feature
- `UpdateAllConfigs`: True to update all configurations, false to not

### Return Value

0 indicates that the freeze bar did not move to the specified location in the FeatureManager design tree; a non-0 value indicates that the freeze bar did move to the specified location in the FeatureManager design tree

## VBA Syntax

See [FeatureManager::EditFreeze](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~EditFreeze.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html)
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)
[IFeature::IsFrozen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)
[IFeature::MoveFreezeBarTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.html)
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
