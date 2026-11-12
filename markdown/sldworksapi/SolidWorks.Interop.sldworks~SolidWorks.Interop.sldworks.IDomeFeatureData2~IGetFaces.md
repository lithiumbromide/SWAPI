---
title: "IGetFaces Method (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IGetFaces.html"
---

# IGetFaces Method (IDomeFeatureData2)

Gets the planar or non-planar faces of this dome feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal FaceCount As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
Dim FaceCount As System.Integer
Dim value As Face2

value = instance.IGetFaces(FaceCount)
```

### C#

```csharp
Face2 IGetFaces(
   System.int FaceCount
)
```

### C++/CLI

```cpp
Face2^ IGetFaces(
   System.int FaceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of planar or non-planar faces of this dome feature

### Return Value

- in-process, unmanaged C++: Pointer to an array of planar or non-planar [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of this dome feature
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IDomeFeatureData2::GetFaceCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDomeFeatureData2~GetFaceCount.html) before using this method to determine the size of the output array.

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
[IDomeFeatureData2::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ISetFaces.html)
[IDomeFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Faces.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
