---
title: "MoveFreezeBarTo2 Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "MoveFreezeBarTo2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo2.html"
---

# MoveFreezeBarTo2 Method (IFeature)

Moves the freeze bar to the specified location in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveFreezeBarTo2( _
   ByVal Location As System.Integer, _
   ByVal UpdateAllConfigs As System.Boolean, _
   ByVal UnlockConfigs As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Location As System.Integer
Dim UpdateAllConfigs As System.Boolean
Dim UnlockConfigs As System.Boolean
Dim value As System.Integer

value = instance.MoveFreezeBarTo2(Location, UpdateAllConfigs, UnlockConfigs)
```

### C#

```csharp
System.int MoveFreezeBarTo2(
   System.int Location,
   System.bool UpdateAllConfigs,
   System.bool UnlockConfigs
)
```

### C++/CLI

```cpp
System.int MoveFreezeBarTo2(
   System.int Location,
   System.bool UpdateAllConfigs,
   System.bool UnlockConfigs
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `Location`: - [swMoveFreezeBarTo_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveFreezeBarTo_e.html)

  .swMoveFreezeBarToBeforeFeature

  -or-

- swMoveFreezeBarTo_e.swMoveFreezeBarToAfterFeature
- `UpdateAllConfigs`: True to update all configurations, false to not
- `UnlockConfigs`: True to unlock configurations, false to not

### Return Value

1 indicates that the freeze bar did not move to the specified location in the FeatureManager design tree; 0 indicates that the freeze bar did move to the specified location in the FeatureManager design tree

## VBA Syntax

See

[Feature::MoveFreezeBarTo2](ms-its:sldworksapivb6.chm::/sldworks~Feature~MoveFreezeBarTo2.html)

.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

[IFeature::IsFrozen Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)

[IFeature::HasFrozenUpdatePending Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)

[IFeature::IsHiddenLock Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html)

[IFeatureManager::EditFreeze2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze2.html)

[IFeatureManager::GetFreezeLocation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html)

[IModelDocExtension::UpdateFrozenFeatures Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html)

[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
