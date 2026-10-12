---
title: "ISetDeletedFaces Method (IDeleteFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDeleteFaceFeatureData"
member: "ISetDeletedFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~ISetDeletedFaces.html"
---

# ISetDeletedFaces Method (IDeleteFaceFeatureData)

Sets the faces for the DeleteFace feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetDeletedFaces( _
   ByVal Count As System.Integer, _
   ByRef Facedisp As Face2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDeleteFaceFeatureData
Dim Count As System.Integer
Dim Facedisp As Face2
Dim value As System.Boolean

value = instance.ISetDeletedFaces(Count, Facedisp)
```

### C#

```csharp
System.bool ISetDeletedFaces(
   System.int Count,
   ref Face2 Facedisp
)
```

### C++/CLI

```cpp
System.bool ISetDeletedFaces(
   System.int Count,
   Face2^% Facedisp
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces
- `Facedisp`: - in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

### Return Value

True if the faces are set, false if not

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.html)
[IDeleteFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData_members.html)
[IDeleteFaceFeatureData::SetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~SetDeletedFaces.html)
[IDeleteFaceFeatureData::GetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFaces.html)
[IDeleteFaceFeatureData::GetDeletedFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~GetDeletedFacesCount.html)
[IDeleteFaceFeatureData::IGetDeletedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData~IGetDeletedFaces.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
