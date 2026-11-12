---
title: "IDeleteFacesMakeSheetBodiesCount Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDeleteFacesMakeSheetBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.html"
---

# IDeleteFacesMakeSheetBodiesCount Method (IBody2)

Gets the number of sheet bodies to create from the deleted faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteFacesMakeSheetBodiesCount( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceList As Face2 _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim FaceCount As System.Integer
Dim FaceList As Face2
Dim value As System.Integer

value = instance.IDeleteFacesMakeSheetBodiesCount(FaceCount, FaceList)
```

### C#

```csharp
System.int IDeleteFacesMakeSheetBodiesCount(
   System.int FaceCount,
   ref Face2 FaceList
)
```

### C++/CLI

```cpp
System.int IDeleteFacesMakeSheetBodiesCount(
   System.int FaceCount,
   Face2^% FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of faces to delete from the body
- `FaceList`: - in-process, unmanaged C++: Pointer to an array of the [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

Number of sheet bodies to create from the deleted faces

## Remarks

To create sheet bodies from deleted faces, call [IBody2::IDeleteFacesMakeSheetBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
