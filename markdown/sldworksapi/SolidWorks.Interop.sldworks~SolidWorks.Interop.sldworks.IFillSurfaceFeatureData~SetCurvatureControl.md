---
title: "SetCurvatureControl Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "SetCurvatureControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetCurvatureControl.html"
---

# SetCurvatureControl Method (IFillSurfaceFeatureData)

Sets the contact type for this fill-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCurvatureControl( _
   ByVal EntityIn As System.Object, _
   ByVal ControlType As System.Integer, _
   ByVal BAll As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim EntityIn As System.Object
Dim ControlType As System.Integer
Dim BAll As System.Boolean
Dim value As System.Boolean

value = instance.SetCurvatureControl(EntityIn, ControlType, BAll)
```

### C#

```csharp
System.bool SetCurvatureControl(
   System.object EntityIn,
   System.int ControlType,
   System.bool BAll
)
```

### C++/CLI

```cpp
System.bool SetCurvatureControl(
   System.Object^ EntityIn,
   System.int ControlType,
   System.bool BAll
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EntityIn`: Edge or sketch boundary returned by [IFillSurfaceFeatureData::GetPatchBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html) or [IFillSurfaceFeatureData::IGetPatchBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.html)
- `ControlType`: Contact type as defined in [swContactType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swContactType_e.html)
- `BAll`: True to set contact type for all boundary entities, false to not

### Return Value

True if contact type is set, false if not

## VBA Syntax

See [FillSurfaceFeatureData::SetCurvatureControl](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~SetCurvatureControl.html).

## Remarks

Sketch boundaries must be set to swContact.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)
[IFillSurfaceFeatureData::GetAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.html)
[IFillSurfaceFeatureData::GetCurvatureControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html)
[IFillSurfaceFeatureData::GetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html)
[IFillSurfaceFeatureData::GetPatchBoundaryCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundaryCount.html)
[IFillSurfaceFeatureData::ISetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.html)
[IFillSurfaceFeatureData::SetPatchBoundary Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.html)
[IFillSurfaceFeatureData::ToggleAlternateFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ToggleAlternateFace.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
