---
title: "MoveFreezeBarTo Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "MoveFreezeBarTo"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.html"
---

# MoveFreezeBarTo Method (IFeature)

Obsolete. Superseded by [IFeature::MoveFreezeBarTo2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~MoveFreezeBarTo2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveFreezeBarTo( _
   ByVal Location As System.Integer, _
   ByVal UpdateAllConfigs As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim Location As System.Integer
Dim UpdateAllConfigs As System.Boolean
Dim value As System.Integer

value = instance.MoveFreezeBarTo(Location, UpdateAllConfigs)
```

### C#

```csharp
System.int MoveFreezeBarTo(
   System.int Location,
   System.bool UpdateAllConfigs
)
```

### C++/CLI

```cpp
System.int MoveFreezeBarTo(
   System.int Location,
   System.bool UpdateAllConfigs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Location`: - [swMoveFreezeBarTo_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveFreezeBarTo_e.html).swMoveFreezeBarToBeforeFeature

    -or-

  - swMoveFreezeBarTo_e.swMoveFreezeBarToAfterFeature
- `UpdateAllConfigs`: True to update all configurations, false to not

### Return Value

0 indicates that the freeze bar did not move to the specified location in the FeatureManager design tree; a non-0 value indicates that the freeze bar did move to the specified location in the FeatureManager design tree

## VBA Syntax

See [Feature::MoveFreezeBarTo](ms-its:sldworksapivb6.chm::/sldworks~Feature~MoveFreezeBarTo.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html)
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IFeature::IsFrozen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)
[IFeatureManager::EditFreeze Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.html)
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html)
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
