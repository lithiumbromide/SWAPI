---
title: "ReleaseSelectionAccess Method (ISurfExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfExtrudeFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISurfExtrudeFeatureData)

Releases access to the selections for this extruded surface.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfExtrudeFeatureData

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

See [SurfExtrudeFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SurfExtrudeFeatureData~ReleaseSelectionAccess.html).

## Examples

See the [ISurfExtrudeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html) examples.

## Remarks

[ISurfExtrudeFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfExtrudeFeatureData~AccessSelections.html) and [ISurfExtrudeFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfExtrudeFeatureData~IAccessSelections.html) put the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[ISurfExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData.html)
[ISurfExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
