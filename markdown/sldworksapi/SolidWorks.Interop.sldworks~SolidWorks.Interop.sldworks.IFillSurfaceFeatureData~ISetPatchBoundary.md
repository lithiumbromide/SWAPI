---
title: "ISetPatchBoundary Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "ISetPatchBoundary"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.html"
---

# ISetPatchBoundary Method (IFillSurfaceFeatureData)

Sets the patch boundary for this fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetPatchBoundary( _
   ByVal Count As System.Integer, _
   ByRef DispArr As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim Count As System.Integer
Dim DispArr As System.Object
Dim value As System.Boolean

value = instance.ISetPatchBoundary(Count, DispArr)
```

### C#

```csharp
System.bool ISetPatchBoundary(
   System.int Count,
   ref System.object DispArr
)
```

### C++/CLI

```cpp
System.bool ISetPatchBoundary(
   System.int Count,
   System.Object^% DispArr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of entities to use for the patch boundary
- `DispArr`: - in-process, unmanaged C++: Pointer to an array of entities to use as the patch boundary of size count; valid entities are:

    - [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)
    - [sketches](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the patch boundary is set, false if not

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.html)
[IFillSurfaceFeatureData::GetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html)
[IFillSurfaceFeatureData::GetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html)
[IFillSurfaceFeatureData::GetPatchBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundaryCount.html)
[IFillSurfaceFeatureData::IGetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.html)
[IFillSurfaceFeatureData::SetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetCurvatureControl.html)
[IFillSurfaceFeatureData::SetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.html)
[IFillSurfaceFeatureData::ToggleAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ToggleAlternateFace.html)
[IFillSurfaceFeatureData::TryToFormSolid Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~TryToFormSolid.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
