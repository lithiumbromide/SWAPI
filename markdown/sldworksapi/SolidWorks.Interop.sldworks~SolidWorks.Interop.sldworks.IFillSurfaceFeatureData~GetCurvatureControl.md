---
title: "GetCurvatureControl Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "GetCurvatureControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html"
---

# GetCurvatureControl Method (IFillSurfaceFeatureData)

Gets the contact type for the input boundary.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurvatureControl( _
   ByVal EntityIn As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim EntityIn As System.Object
Dim value As System.Integer

value = instance.GetCurvatureControl(EntityIn)
```

### C#

```csharp
System.int GetCurvatureControl(
   System.object EntityIn
)
```

### C++/CLI

```cpp
System.int GetCurvatureControl(
   System.Object^ EntityIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityIn`: Edge or sketch boundary returned from [IFillSurfaceFeatureData::GetPatchBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html)

### Return Value

Control type as defined in [swContactType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swContactType_e.html)

## VBA Syntax

See [FillSurfaceFeatureData::GetCurvatureControl](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~GetCurvatureControl.html).

## Remarks

Sketch boundaries always return a control type of swContact.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.html)
[IFillSurfaceFeatureData::GetPatchBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundaryCount.html)
[IFillSurfaceFeatureData::IGetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.html)
[IFillSurfaceFeatureData::ISetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.html)
[IFillSurfaceFeatureData::SetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetCurvatureControl.html)
[IFillSurfaceFeatureData::SetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.html)
[IFillSurfaceFeatureData::ToggleAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ToggleAlternateFace.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
