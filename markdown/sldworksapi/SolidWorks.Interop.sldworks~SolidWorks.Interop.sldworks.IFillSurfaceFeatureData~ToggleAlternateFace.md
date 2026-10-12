---
title: "ToggleAlternateFace Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "ToggleAlternateFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ToggleAlternateFace.html"
---

# ToggleAlternateFace Method (IFillSurfaceFeatureData)

Switches the boundary face of the curvature control of the patch.

## Syntax

### Visual Basic (Declaration)

```vb
Function ToggleAlternateFace() As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim value As Face2

value = instance.ToggleAlternateFace()
```

### C#

```csharp
Face2 ToggleAlternateFace()
```

### C++/CLI

```cpp
Face2^ ToggleAlternateFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the new boundary face, [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) object

## VBA Syntax

See [FillSurfaceFeatureData::ToggleAlternateFace](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~ToggleAlternateFace.html).

## Remarks

This method is valid only when the contact type is tangent and edges are used to define the patch boundary. Use [IFillSurfaceFeatureData::GetCurvatureControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html) to determine the contact type.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.html)
[IFillSurfaceFeatureData::GetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html)
[IFillSurfaceFeatureData::GetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html)
[IFillSurfaceFeatureData::GetPatchBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundaryCount.html)
[IFillSurfaceFeatureData::IGetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.html)
[IFillSurfaceFeatureData::ISetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.html)
[IFillSurfaceFeatureData::SetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetCurvatureControl.html)
[IFillSurfaceFeatureData::SetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
