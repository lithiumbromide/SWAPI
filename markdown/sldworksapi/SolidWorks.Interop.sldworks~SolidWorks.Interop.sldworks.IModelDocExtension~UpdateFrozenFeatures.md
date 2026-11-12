---
title: "UpdateFrozenFeatures Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "UpdateFrozenFeatures"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html"
---

# UpdateFrozenFeatures Method (IModelDocExtension)

Updates frozen features of the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateFrozenFeatures( _
   ByVal UpdateAllConfigs As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim UpdateAllConfigs As System.Boolean
Dim value As System.Integer

value = instance.UpdateFrozenFeatures(UpdateAllConfigs)
```

### C#

```csharp
System.int UpdateFrozenFeatures(
   System.bool UpdateAllConfigs
)
```

### C++/CLI

```cpp
System.int UpdateFrozenFeatures(
   System.bool UpdateAllConfigs
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UpdateAllConfigs`: True to update all configurations, false to not

### Return Value

Number of frozen features updated

## VBA Syntax

See [ModelDocExtension::UpdateFrozenFeatures](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~UpdateFrozenFeatures.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)
[IFeature::IsFrozen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)
[IFeature::MoveFreezeBarTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.html)
[IFeatureManager::EditFreeze Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.html)
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
