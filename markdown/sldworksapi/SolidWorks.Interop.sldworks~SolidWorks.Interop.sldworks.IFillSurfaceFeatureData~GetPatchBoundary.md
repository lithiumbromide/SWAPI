---
title: "GetPatchBoundary Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "GetPatchBoundary"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html"
---

# GetPatchBoundary Method (IFillSurfaceFeatureData)

Gets the entities used to define the patch boundary for this fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPatchBoundary( _
   ByRef EntType As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim EntType As System.Object
Dim value As System.Object

value = instance.GetPatchBoundary(EntType)
```

### C#

```csharp
System.object GetPatchBoundary(
   out System.object EntType
)
```

### C++/CLI

```cpp
System.Object^ GetPatchBoundary(
   [Out] System.Object^ EntType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntType`: Array of types of entities used to define the patch boundary as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

  - Edges (swSelEDGES)
  - Sketches (swSelSKETCHES)

### Return Value

Array of entities used to define the patch boundary

## VBA Syntax

See [FillSurfaceFeatureData::GetPatchBoundary](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~GetPatchBoundary.html).

## Examples

[Insert Fill-surface Feature (C#)](Insert_Fill-surface_Feature_Example_CSharp.htm)
[Insert Fill-surface Feature (VB.NET)](Insert_Fill-surface_Feature_Example_VBNET.htm)
[Insert Fill-surface Feature (VBA)](Insert_Fill-surface_Feature_Example_VB.htm)

## Remarks

[IFillSurfaceFeatureData::GetCurvatureControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html) uses the return value as input, so call IFillSurfaceFeatureData::GetPatchBoundary before calling IFillSurfaceFeatureData::GetCurvatureControl.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.html)
[IFillSurfaceFeatureData::GetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html)
[IFillSurfaceFeatureData::GetPatchBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundaryCount.html)
[IFillSurfaceFeatureData::IGetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.html)
[IFillSurfaceFeatureData::ISetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.html)
[IFillSurfaceFeatureData::SetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetCurvatureControl.html)
[IFillSurfaceFeatureData::SetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.html)
[IFillSurfaceFeatureData::ToggleAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ToggleAlternateFace.html)
[IFillSurfaceFeatureData::TryToFormSolid Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~TryToFormSolid.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
