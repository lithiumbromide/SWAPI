---
title: "IGetFaces Method (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetFaces.html"
---

# IGetFaces Method (IMoveFaceFeatureData)

Gets the faces for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal Count As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim Count As System.Integer
Dim value As Face2

value = instance.IGetFaces(Count)
```

### C#

```csharp
Face2 IGetFaces(
   System.int Count
)
```

### C++/CLI

```cpp
Face2^ IGetFaces(
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces to move

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to move

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IMoveFaceFeatureData::GetFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveFaceFeatureData~GetFacesCount.html) before calling this method to dimension the array.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetFaces.html)
[IMoveFaceFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Faces.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
