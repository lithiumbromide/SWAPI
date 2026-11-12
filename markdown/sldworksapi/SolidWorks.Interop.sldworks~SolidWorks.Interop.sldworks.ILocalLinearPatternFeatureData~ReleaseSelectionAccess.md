---
title: "ReleaseSelectionAccess Method (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ILocalLinearPatternFeatureData)

Releases access to the selections that created this linear component pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData

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

See [LocalLinearPatternFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ILocalLinearPatternFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~AccessSelections.html) and [ILocalLinearPatternFeatureData::IAccessSelections2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILocalLinearPatternFeatureData~IAccessSelections2.html) put the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
