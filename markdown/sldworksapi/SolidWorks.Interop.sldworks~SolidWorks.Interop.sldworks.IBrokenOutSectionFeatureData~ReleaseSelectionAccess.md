---
title: "ReleaseSelectionAccess Method (IBrokenOutSectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBrokenOutSectionFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (IBrokenOutSectionFeatureData)

Releases access to the selections in this broken-out section feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As IBrokenOutSectionFeatureData

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

See [BrokenOutSectionFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~BrokenOutSectionFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Broken-Out Section Feature Data (VBA)](Get_Broken_Out_Section_Feature_Data_Example_VB.htm)
[Get Broken-Out Section Feature Data (VB.NET)](Get_Broken_Out_Section_Feature_Data_Example_VBNET.htm)
[Get Broken-Out Section Feature Data (C#)](Get_Broken_Out_Section_Feature_Data_Example_CSharp.htm)

## Remarks

[IBrokenOutSectionFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~AccessSelections.html) or [IBrokenOutSectionFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBrokenOutSectionFeatureData~IAccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[IBrokenOutSectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData.html)
[IBrokenOutSectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
