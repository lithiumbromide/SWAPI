---
title: "IGetFaces Method (ISurfaceOffsetFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISurfaceOffsetFeatureData"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~IGetFaces.html"
---

# IGetFaces Method (ISurfaceOffsetFeatureData)

Obsolete. Superseded by [ISurfaceOffsetFeatureData::IGetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceOffsetFeatureData~IGetEntities.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal Count As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As ISurfaceOffsetFeatureData
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

- `Count`: Number of offset faces

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [ISurfaceOffsetFeatureData::GetFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurfaceOffsetFeatureData~GetFacesCount.html) before calling this method to get the value for Count.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISurfaceOffsetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData.html)
[ISurfaceOffsetFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html)
[ISurfaceOffsetFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~ISetFaces.html)
[ISurfaceOffsetFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData~Faces.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
