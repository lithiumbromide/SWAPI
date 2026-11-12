---
title: "ReleaseSelectionAccess Method (ITabAndSlotFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITabAndSlotFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ITabAndSlotFeatureData)

Releases access to the selections for this Tab and Slot feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ITabAndSlotFeatureData

instance.ReleaseSelectionAccess()
```

### C#

```csharp
void ReleaseSelectionAccess()
```

### C++/CLI

```cpp
void ReleaseSelectionAccess();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [TabAndSlotFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~TabAndSlotFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ITabAndSlotFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[ITabAndSlotFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData.html)
[ITabAndSlotFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
