---
title: "IGetSupplementalFaces Method (IMate2)"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: "IGetSupplementalFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IGetSupplementalFaces.html"
---

# IGetSupplementalFaces Method (IMate2)

Gets the faces in this mate.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetSupplementalFaces( _
   ByVal WhichOne As System.Integer, _
   ByVal FaceCount As System.Integer _
) As Face2
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
Dim WhichOne As System.Integer
Dim FaceCount As System.Integer
Dim value As Face2

value = instance.IGetSupplementalFaces(WhichOne, FaceCount)
```

### C#

```csharp
Face2 IGetSupplementalFaces(
   System.int WhichOne,
   System.int FaceCount
)
```

### C++/CLI

```cpp
Face2^ IGetSupplementalFaces(
   System.int WhichOne,
   System.int FaceCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: Number of components in this mate
- `FaceCount`: Number of faces in this mate

### Return Value

- in-process, unmanaged C++: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) in this mate

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)
[IMate2::GetSupplementalFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetSupplementalFaces.html)
[IMate2::HasLoadBearingFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces.html)
[IMate2::IsLoadBearingFacesBonded Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
