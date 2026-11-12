---
title: "ISetFaces Method (IChamferFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IChamferFeatureData2"
member: "ISetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~ISetFaces.html"
---

# ISetFaces Method (IChamferFeatureData2)

Gets the faces to which a chamfer is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFaces( _
   ByVal Count As System.Integer, _
   ByRef FaceList As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IChamferFeatureData2
Dim Count As System.Integer
Dim FaceList As Face2

instance.ISetFaces(Count, FaceList)
```

### C#

```csharp
void ISetFaces(
   System.int Count,
   ref Face2 FaceList
)
```

### C++/CLI

```cpp
void ISetFaces(
   System.int Count,
   Face2^% FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces
- `FaceList`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Count

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IChamferFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2.html)
[IChamferFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html)
[IChamferFeatureData2::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~IGetFaces.html)
[IChamferFeatureData2::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2~Faces.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
