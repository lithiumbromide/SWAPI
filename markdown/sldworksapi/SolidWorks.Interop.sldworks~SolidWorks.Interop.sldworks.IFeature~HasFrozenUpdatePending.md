---
title: "HasFrozenUpdatePending Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "HasFrozenUpdatePending"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html"
---

# HasFrozenUpdatePending Method (IFeature)

Gets whether this feature has pending freeze updates.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasFrozenUpdatePending() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.HasFrozenUpdatePending()
```

### C#

```csharp
System.bool HasFrozenUpdatePending()
```

### C++/CLI

```cpp
System.bool HasFrozenUpdatePending();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the feature needs an update, false if not

## VBA Syntax

See [Feature::HasFrozenUpdatePending](ms-its:sldworksapivb6.chm::/sldworks~Feature~HasFrozenUpdatePending.html).

## Examples

[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)
[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html)
[IFeature::IsFrozen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)
[IFeature::MoveFreezeBarTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.html)
[IFeatureManager::EditFreeze Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.html)
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html)
[IFeature::IsHiddenLock Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html)
[IModelDocExtension::ShowPartRebuildIndicators Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowPartRebuildIndicators.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
