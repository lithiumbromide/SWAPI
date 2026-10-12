---
title: "IGetPatchBoundary Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "IGetPatchBoundary"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.html"
---

# IGetPatchBoundary Method (IFillSurfaceFeatureData)

Gets the entities used to define the patch boundary for this fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetPatchBoundary( _
   ByVal Count As System.Integer, _
   ByRef EntType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim Count As System.Integer
Dim EntType As System.Integer
Dim value As System.Object

value = instance.IGetPatchBoundary(Count, EntType)
```

### C#

```csharp
System.object IGetPatchBoundary(
   System.int Count,
   out System.int EntType
)
```

### C++/CLI

```cpp
System.Object^ IGetPatchBoundary(
   System.int Count,
   [Out] System.int EntType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities used to define the patch boundary
- `EntType`: - in-process, unmanaged C++: Pointer to an array of types of entities used to define the patch boundary as defined by [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

    - edges (swSelEDGES)
    - sketches (swSelSKETCHES)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

- in-process, unmanaged C++: Pointer to an array of entities used to define the patch boundary of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Call [IFillSurfaceFeatureData::GetPatchBoundaryCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundaryCount.html) before calling this method.

[IFillSurfaceFeatureData::GetCurvatureControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html) uses the return value as input, so call IFillSurfaceFeatureData::IGetPatchBoundary before calling IFillSurfaceFeatureData::GetCurvatureControl.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.html)
[IFillSurfaceFeatureData::GetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html)
[IFillSurfaceFeatureData::ISetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.html)
[IFillSurfaceFeatureData::SetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.html)
[IFillSurfaceFeatureData::ToggleAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ToggleAlternateFace.html)
[IFillSurfaceFeatureData::TryToFormSolid Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~TryToFormSolid.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
