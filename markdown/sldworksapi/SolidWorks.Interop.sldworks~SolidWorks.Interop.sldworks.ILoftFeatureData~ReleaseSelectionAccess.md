---
title: "ReleaseSelectionAccess Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ILoftFeatureData)

Releases access to the selections for this loft feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData

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

See [LoftFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~ReleaseSelectionAccess.html).

## Examples

[Get Guide Curves in Loft Feature (C#)](Get_Guide_Curves_in_Loft_Feature_Example_CSharp.htm)
[Get Guide Curves in Loft Feature (VB.NET)](Get_Guide_Curves_in_Loft_Feature_Example_VBNET.htm)
[Get Guide Curves in Loft Feature (VBA)](Get_Guide_Curves_in_Loft_Feature_Example_VB.htm)

## Remarks

[ILoftFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~AccessSelections.html) and [ILoftFeatureData::IAccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoftFeatureData~IAccessSelections.html) put the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) or [IFeature::IModifyDefintion2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html) if you did.

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
