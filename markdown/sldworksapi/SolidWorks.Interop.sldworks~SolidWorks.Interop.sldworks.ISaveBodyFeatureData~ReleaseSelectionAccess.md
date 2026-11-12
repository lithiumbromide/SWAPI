---
title: "ReleaseSelectionAccess Method (ISaveBodyFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISaveBodyFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISaveBodyFeatureData)

Releases access to the selections that define this Save Bodies feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISaveBodyFeatureData

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

See [SaveBodyFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SaveBodyFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Number of Bodies in Save Bodies Feature (VBA)](Get_Number_of_Bodies_in_Save_Bodies_Feature_Example_VB.htm)

## Remarks

[ISaveBodiesFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISaveBodyFeatureData~AccessSelections.html) puts the model in a rollback state to allow access to the selections that define the feature.

Use this method to restore the rollback state if you did not modify the feature, or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did modify the feature.

## See Also

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.html)
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
