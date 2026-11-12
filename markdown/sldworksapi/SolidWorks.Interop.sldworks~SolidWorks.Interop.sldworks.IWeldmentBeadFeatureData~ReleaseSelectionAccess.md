---
title: "ReleaseSelectionAccess Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IWeldmentBeadFeatureData)

Releases access to the selections that define this weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData

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

See [WeldmentBeadFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IWeldmentBeadFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
