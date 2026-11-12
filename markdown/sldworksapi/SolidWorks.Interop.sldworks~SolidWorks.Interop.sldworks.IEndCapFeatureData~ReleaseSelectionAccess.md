---
title: "ReleaseSelectionAccess Method (IEndCapFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEndCapFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IEndCapFeatureData)

Releases access to the selections that define this end-cap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IEndCapFeatureData

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

See [EndCapFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~EndCapFeatureData~ReleaseSelectionAccess.html).

## Examples

[List End-cap Feature Properties (VBA)](List_End-Cap_Feature_Properties_Example_VB.htm)

## Remarks

[IEndCapFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEndCapFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did.

## See Also

[IEndCapFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData.html)
[IEndCapFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
