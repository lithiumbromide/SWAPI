---
title: "ISetFaces Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "ISetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetFaces.html"
---

# ISetFaces Method (IMoveFaceFeatureData)

Sets the faces for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFaces( _
   ByVal Count As System.Integer, _
   ByRef EntIn As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim Count As System.Integer
Dim EntIn As Face2

instance.ISetFaces(Count, EntIn)
```

### C#

```csharp
void ISetFaces(
   System.int Count,
   ref Face2 EntIn
)
```

### C++/CLI

```cpp
void ISetFaces(
   System.int Count,
   Face2^% EntIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces to move
- `EntIn`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to move

  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetFacesCount.html)
[IMoveFaceFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetFaces.html)
[IMoveFaceFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Faces.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
