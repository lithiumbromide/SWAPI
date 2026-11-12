---
title: "ReleaseSelectionAccess Method (IAdvancedHoleFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedHoleFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IAdvancedHoleFeatureData)

Releases access to the selections used to define the Hole Wizard feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedHoleFeatureData

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

See [AdvancedHoleFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~AdvancedHoleFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IAdvancedHoleFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

You must use either of the following methods to restore the original state of the model:

- [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html), if you modified the feature
- this method, if you did not modify the feature

## See Also

[IAdvancedHoleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.html)
[IAdvancedHoleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
