---
title: "GetConstraintCurvesCount Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "GetConstraintCurvesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurvesCount.html"
---

# GetConstraintCurvesCount Method (IFillSurfaceFeatureData)

Gets the number of entities used to create the constraint curves for this fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConstraintCurvesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim value As System.Integer

value = instance.GetConstraintCurvesCount()
```

### C#

```csharp
System.int GetConstraintCurvesCount()
```

### C++/CLI

```cpp
System.int GetConstraintCurvesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities

## VBA Syntax

See [FillSurfaceFeatureData::GetConstraintCurvesCount](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~GetConstraintCurvesCount.html).

## Examples

[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)

## Remarks

Call this method before calling [IFillSurfaceFeatureData::IGetConstraintCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~IGetConstraintCurves.html).

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetConstraintCurves.html)
[IFillSurfaceFeatureData::ISetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetConstraintCurves.html)
[IFillSurfaceFeatureData::SetConstraintCurves Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetConstraintCurves.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
