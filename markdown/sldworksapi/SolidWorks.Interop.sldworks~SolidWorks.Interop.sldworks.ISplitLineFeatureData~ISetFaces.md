---
title: "ISetFaces Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "ISetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetFaces.html"
---

# ISetFaces Method (ISplitLineFeatureData)

Sets the faces split by the split line.

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
Dim instance As ISplitLineFeatureData
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

- `Count`: Number of faces
- `EntIn`: - in-process, unmanaged C++: Pointer to an array of split [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## VBA Syntax

See [SplitLineFeatureData::ISetFaces](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~ISetFaces.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetFacesCount.html)
[ISplitLineFeatureData::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetFaces.html)
[ISplitLineFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Faces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
