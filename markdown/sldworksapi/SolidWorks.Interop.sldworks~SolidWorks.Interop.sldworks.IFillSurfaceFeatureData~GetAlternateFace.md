---
title: "GetAlternateFace Method (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "GetAlternateFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace.html"
---

# GetAlternateFace Method (IFillSurfaceFeatureData)

Gets an alternate face to use as the boundary face for the curvature control of the patch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAlternateFace() As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim value As Face2

value = instance.GetAlternateFace()
```

### C#

```csharp
Face2 GetAlternateFace()
```

### C++/CLI

```cpp
Face2^ GetAlternateFace();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the alternate face, the [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) object

## VBA Syntax

See [FillSurfaceFeatureData::GetAlternateFace](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~GetAlternateFace.html).

## Remarks

This method is valid only when the contact type is tangent and edges are used to define the patch boundary. If an edge has two faces, then this method returns the face with which the resultant feature geometry is tangent.

Use [IFillSurfaceFeatureData::GetCurvatureControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.html) to determine the contact type.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
