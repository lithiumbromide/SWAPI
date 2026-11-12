---
title: "ReleaseSelectionAccess Method (ICavityFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICavityFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ICavityFeatureData)

Releases access to the selections that define this cavity feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ICavityFeatureData

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

See [CavityFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~CavityFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ICavityFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICavityFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[ICavityFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData.html)
[ICavityFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
