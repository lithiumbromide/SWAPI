---
title: "ReleaseSelectionAccess Method (ILoftedBendsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftedBendsFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ILoftedBendsFeatureData)

Releases access to the selections for this lofted bends feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftedBendsFeatureData

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

See [LoftedBendsFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~LoftedBendsFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ILoftedBendsFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~AccessSelections.html) and [ILoftedBendsFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftedBendsFeatureData~IAccessSelections.html) put the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[ILoftedBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData.html)
[ILoftedBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
