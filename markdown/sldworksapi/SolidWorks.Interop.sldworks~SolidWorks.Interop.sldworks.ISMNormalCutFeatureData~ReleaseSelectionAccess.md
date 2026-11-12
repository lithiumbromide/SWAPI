---
title: "ReleaseSelectionAccess Method (ISMNormalCutFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISMNormalCutFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISMNormalCutFeatureData)

Obsolete. See [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISMNormalCutFeatureData

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

See [SMNormalCutFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SMNormalCutFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ISMNormalCutFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did modify the feature.

## See Also

[ISMNormalCutFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData.html)
[ISMNormalCutFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
