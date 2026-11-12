---
title: "IsFrozen Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IsFrozen"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html"
---

# IsFrozen Method (IFeature)

Gets whether this feature is frozen.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsFrozen() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.IsFrozen()
```

### C#

```csharp
System.bool IsFrozen()
```

### C++/CLI

```cpp
System.bool IsFrozen();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the feature is frozen, false if not (see **Remarks**)

## VBA Syntax

See [Feature::IsFrozen](ms-its:sldworksapivb6.chm::/sldworks~Feature~IsFrozen.html).

## Examples

[Get Whether Feature is Frozen (VBA)](Get_Whether_Feature_is_Locked_Example_VB.htm)
[Get Whether Feature is Frozen (VB.NET)](Get_Whether_Feature_is_Locked_Example_VBNET.htm)
[Get Whether Feature is Frozen (C#)](Get_Whether_Feature_is_Locked_Example_CSharp.htm)
[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)
[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)

## Remarks

When a feature is frozen, you cannot edit the feature and the feature is excluded from rebuilds of the model.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)
[IFeature::MoveFreezeBarTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.html)
[IFeatureManager::EditFreeze Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.html)
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html)
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html)
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html)
[IFeatureManager::InsertFeatureLock Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFeatureLock.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
