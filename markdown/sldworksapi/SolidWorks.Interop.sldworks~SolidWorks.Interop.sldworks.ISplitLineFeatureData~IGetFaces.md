---
title: "IGetFaces Method (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "IGetFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetFaces.html"
---

# IGetFaces Method (ISplitLineFeatureData)

Gets the faces split by the split line.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFaces( _
   ByVal Count As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
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

- `Count`: Number of faces to split

### Return Value

- in-process, unmanaged C++: Pointer to an array of split [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [ISplitLineFeatureData::GetFacesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplitLineFeatureData~GetFacesCount.html) to determine the size of the array for this method.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetFaces.html)
[ISplitLineFeatureData::Faces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Faces.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
