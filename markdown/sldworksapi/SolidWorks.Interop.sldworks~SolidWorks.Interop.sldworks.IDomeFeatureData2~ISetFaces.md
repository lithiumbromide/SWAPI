---
title: "ISetFaces Method (IDomeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IDomeFeatureData2"
member: "ISetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~ISetFaces.html"
---

# ISetFaces Method (IDomeFeatureData2)

Sets the planar or non-planar faces of this dome feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFaces( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceList As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDomeFeatureData2
Dim FaceCount As System.Integer
Dim FaceList As Face2

instance.ISetFaces(FaceCount, FaceList)
```

### C#

```csharp
void ISetFaces(
   System.int FaceCount,
   ref Face2 FaceList
)
```

### C++/CLI

```cpp
void ISetFaces(
   System.int FaceCount,
   Face2^% FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of planar or non-planar faces
- `FaceList`: - in-process, unmanaged C++: Pointer to an array of planar and non-planar [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of this dome feature

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method does not affect geometry until you call [IFeature::IModifyDefintion2.](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IModifyDefinition2.html)

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDomeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2.html)
[IDomeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html)
[IDomeFeatureData2::GetFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~GetFaceCount.html)
[IDomeFeatureData2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~IGetFaces.html)
[IDomeFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2~Faces.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
