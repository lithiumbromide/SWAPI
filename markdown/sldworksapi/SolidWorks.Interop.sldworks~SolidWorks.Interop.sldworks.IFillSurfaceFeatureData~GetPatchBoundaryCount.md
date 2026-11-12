---
title: "GetPatchBoundaryCount Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "GetPatchBoundaryCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundaryCount.html"
---

# GetPatchBoundaryCount Method (IFillSurfaceFeatureData)

Gets the number of entities used to define the patch boundary for this fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatchBoundaryCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim value As System.Integer

value = instance.GetPatchBoundaryCount()
```

### C#

```csharp
System.int GetPatchBoundaryCount()
```

### C++/CLI

```cpp
System.int GetPatchBoundaryCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of entities used to define the patch boundary

## VBA Syntax

See [FillSurfaceFeatureData::GetPatchBoundaryCount](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~GetPatchBoundaryCount.html).

## Examples

[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)

## Remarks

Call this method before calling [IFillSurfaceFeatureData::IGetPatchBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.html).

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.html)
[IFillSurfaceFeatureData::GetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html)
[IFillSurfaceFeatureData::GetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html)
[IFillSurfaceFeatureData::ISetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.html)
[IFillSurfaceFeatureData::SetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetCurvatureControl.html)
[IFillSurfaceFeatureData::SetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.html)
[IFillSurfaceFeatureData::ToggleAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ToggleAlternateFace.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
