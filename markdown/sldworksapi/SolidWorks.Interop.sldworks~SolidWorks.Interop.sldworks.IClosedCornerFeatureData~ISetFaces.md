---
title: "ISetFaces Method (IClosedCornerFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IClosedCornerFeatureData"
member: "ISetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~ISetFaces.html"
---

# ISetFaces Method (IClosedCornerFeatureData)

Sets the faces for this closed corner feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFaces( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceArray As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IClosedCornerFeatureData
Dim FaceCount As System.Integer
Dim FaceArray As System.Object

instance.ISetFaces(FaceCount, FaceArray)
```

### C#

```csharp
void ISetFaces(
   System.int FaceCount,
   ref System.object FaceArray
)
```

### C++/CLI

```cpp
void ISetFaces(
   System.int FaceCount,
   System.Object^% FaceArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of faces used to describe the closed corner
- `FaceArray`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) used to describe the closed corner of size FaceCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IClosedCornerFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData.html)
[IClosedCornerFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html)
[IClosedCornerFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~IGetFaces.html)
[IClosedCornerFeatureData::IGetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~IGetFacesCount.html)
[IClosedCornerFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData~Faces.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
