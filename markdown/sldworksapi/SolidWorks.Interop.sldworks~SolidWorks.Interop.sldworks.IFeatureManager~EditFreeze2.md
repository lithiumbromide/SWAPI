---
title: "EditFreeze2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "EditFreeze2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze2.html"
---

# EditFreeze2 Method (IFeatureManager)

Moves the freeze bar to the specified location in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditFreeze2( _
   ByVal Location As System.Integer, _
   ByVal FeatureName As System.String, _
   ByVal UpdateAllConfigs As System.Boolean, _
   ByVal UnlockConfigs As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Location As System.Integer
Dim FeatureName As System.String
Dim UpdateAllConfigs As System.Boolean
Dim UnlockConfigs As System.Boolean
Dim value As System.Integer

value = instance.EditFreeze2(Location, FeatureName, UpdateAllConfigs, UnlockConfigs)
```

### C#

```csharp
System.int EditFreeze2(
   System.int Location,
   System.string FeatureName,
   System.bool UpdateAllConfigs,
   System.bool UnlockConfigs
)
```

### C++/CLI

```cpp
System.int EditFreeze2(
   System.int Location,
   System.String^ FeatureName,
   System.bool UpdateAllConfigs,
   System.bool UnlockConfigs
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Location`: Location as defined in

[swMoveFreezeBarTo_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveFreezeBarTo_e.html)
- `FeatureName`: Name of the feature
- `UpdateAllConfigs`: True to update all configurations, false to not
- `UnlockConfigs`: True to unlock configurations, false to not

### Return Value

1 indicates that the freeze bar did not move to the specified location in the FeatureManager design tree; 0 indicates that the freeze bar did move to the specified location in the FeatureManager design tree

## VBA Syntax

See

[FeatureManager::EditFreeze2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~EditFreeze2.html)

.

## Examples

[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)

[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)

[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)

[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

[IFeatureManager::GetFreezeLocation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html)

[IFeature::HasFrozenUpdatePending Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)

[IFeature::IsFrozen Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)

[IFeature::MoveFreezeBarTo2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo2.html)

[IFeature::IsHiddenLock Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html)

[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)

[IModelDocExtension::UpdateFrozenFeatures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
