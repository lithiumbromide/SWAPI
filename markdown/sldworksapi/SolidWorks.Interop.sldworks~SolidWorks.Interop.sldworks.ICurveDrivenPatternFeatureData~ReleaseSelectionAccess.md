---
title: "ReleaseSelectionAccess Method (ICurveDrivenPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICurveDrivenPatternFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ICurveDrivenPatternFeatureData)

Releases access to the selections that define this curve-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ICurveDrivenPatternFeatureData

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

See [CurveDrivenPatternFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~CurveDrivenPatternFeatureData~ReleaseSelectionAccess.html).

## Examples

[Create and Access Curve-driven Pattern Feature (C#)](Create_and_Access_Curve-driven_Pattern_Feature_Example_CSharp.htm)
[Create and Access Curve-driven Pattern Feature (VB.NET)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VBNET.htm)
[Create and Access Curve-driven Pattern Feature (VBA)](Create_and_Access_Curve-driven_Pattern_Feature_Example_VB.htm)

## Remarks

[ICurveDrivenPatternFeatureData::AccessSelections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICurveDrivenPatternFeatureData~AccessSelections.html) puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use [IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html) if you did.

## See Also

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.html)
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
