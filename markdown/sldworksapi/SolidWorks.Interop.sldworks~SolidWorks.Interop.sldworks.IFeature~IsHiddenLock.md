---
title: "IsHiddenLock Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IsHiddenLock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsHiddenLock.html"
---

# IsHiddenLock Method (IFeature)

Gets whether this feature is the freeze bar.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsHiddenLock() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Boolean

value = instance.IsHiddenLock()
```

### C#

```csharp
System.bool IsHiddenLock()
```

### C++/CLI

```cpp
System.bool IsHiddenLock();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the freeze bar, false if not

## VBA Syntax

See [Feature::IsHiddenLock](ms-its:sldworksapivb6.chm::/sldworks~Feature~IsHiddenLock.html).

## Examples

[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)
[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)

## Remarks

Call this property during FeatureManager tree traversal to locate the position of the freeze bar. During a traversal, the freeze bar has been located if:

- [IFeature::Name](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~Name.html) returns "Freeze***"

-and-

- IFeature::IsHiddenLock returns true

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IsFrozen Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsFrozen.html)
[IFeature::MoveFreezeBarTo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~MoveFreezeBarTo.html)
[IFeatureManager::EditFreeze Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditFreeze.html)
[IFeatureManager::GetFreezeLocation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~GetFreezeLocation.html)
[IFeature::HasFrozenUpdatePending Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.html)
[IModelDocExtension::NeedsRebuild2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.html)
[IModelDocExtension::UpdateFrozenFeatures Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateFrozenFeatures.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
