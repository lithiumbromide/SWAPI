---
title: "ReleaseSelectionAccess Method (ISMGussetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMGussetFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISMGussetFeatureData)

Releases access to the selections that define this sheet metal gusset feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISMGussetFeatureData

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

See [SMGussetFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SMGussetFeatureData~ReleaseSelectionAccess.html).

## Examples

See the examples for [ISMGussetFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData.html).

## Remarks

[ISMGussetFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISMGussetFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did modify the feature.

## See Also

[ISMGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData.html)
[ISMGussetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
