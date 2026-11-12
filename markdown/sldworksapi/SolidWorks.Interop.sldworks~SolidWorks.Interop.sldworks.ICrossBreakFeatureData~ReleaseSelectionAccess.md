---
title: "ReleaseSelectionAccess Method (ICrossBreakFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICrossBreakFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ICrossBreakFeatureData)

Releases access to the selections that define this cross break feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ICrossBreakFeatureData

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

See [CrossBreakFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~CrossBreakFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

## Remarks

[ICrossBreakFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICrossBreakFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature. Use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefinition2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[ICrossBreakFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData.html)
[ICrossBreakFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
