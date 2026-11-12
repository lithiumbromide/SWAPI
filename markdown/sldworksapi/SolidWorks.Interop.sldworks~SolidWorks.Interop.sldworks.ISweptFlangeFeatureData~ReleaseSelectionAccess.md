---
title: "ReleaseSelectionAccess Method (ISweptFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISweptFlangeFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISweptFlangeFeatureData)

Releases access to the selections for this swept flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISweptFlangeFeatureData

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

See [SweptFlangeFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SweptFlangeFeatureData~ReleaseSelectionAccess.html).

## Examples

See the [ISheetMetalGaugeTableParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters.html) examples.

## Remarks

[ISweptFlangeFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did modify the feature.

## See Also

[ISweptFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData.html)
[ISweptFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
