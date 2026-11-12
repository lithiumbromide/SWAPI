---
title: "ReleaseSelectionAccess Method (IWrapSketchFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWrapSketchFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IWrapSketchFeatureData)

Releases access to the selections that define this wrap feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IWrapSketchFeatureData

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

See [WrapSketchFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~WrapSketchFeatureData~ReleaseSelectionAccess.html).

## Remarks

[IWrapeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWrapSketchFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[IWrapSketchFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData.html)
[IWrapSketchFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
