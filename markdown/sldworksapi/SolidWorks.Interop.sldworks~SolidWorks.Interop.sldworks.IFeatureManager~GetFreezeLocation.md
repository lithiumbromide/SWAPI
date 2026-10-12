---
title: "GetFreezeLocation Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "GetFreezeLocation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html"
---

# GetFreezeLocation Method (IFeatureManager)

Gets the location of the freeze bar in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFreezeLocation() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.GetFreezeLocation()
```

### C#

```csharp
Feature GetFreezeLocation()
```

### C++/CLI

```cpp
Feature^ GetFreezeLocation();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html); Null, if the freeze bar is at the top of the FeatureManager design tree

## VBA Syntax

See [FeatureManager::GetFreezeLocation](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~GetFreezeLocation.html).

## Examples

[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)
[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::EditFreeze Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html)
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)
[IFeature::IsFrozen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)
[IFeature::MoveFreezeBarTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.html)
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
