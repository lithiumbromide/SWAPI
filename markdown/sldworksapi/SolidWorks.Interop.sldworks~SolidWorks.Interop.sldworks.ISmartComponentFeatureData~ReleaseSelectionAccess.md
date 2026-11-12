---
title: "ReleaseSelectionAccess Method (ISmartComponentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISmartComponentFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ISmartComponentFeatureData)

Releases access to the selection lists of a Smart Component.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ISmartComponentFeatureData

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

See [SmartComponentFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~SmartComponentFeatureData~ReleaseSelectionAccess.html).

## Remarks

[ISmartComponentFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISmartComponentFeatureData~AccessSelections.html) opens the training assembly in which this Smart Component is defined and allows access to the selection lists on the PropertyManager page of the SmartComponent.

To close the training assembly:

- Call this method if you did not insert or delete features and components.
- Call [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) to rebuild the Smart Component if you inserted or deleted features and components.

## See Also

[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.html)
[ISmartComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
