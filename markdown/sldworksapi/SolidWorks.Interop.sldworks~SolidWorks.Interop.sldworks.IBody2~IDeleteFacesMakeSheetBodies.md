---
title: "IDeleteFacesMakeSheetBodies Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IDeleteFacesMakeSheetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.html"
---

# IDeleteFacesMakeSheetBodies Method (IBody2)

Creates sheet bodies from deleted faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteFacesMakeSheetBodies( _
   ByVal FaceCount As System.Integer, _
   ByRef FaceList As Face2, _
   ByVal SheetCount As System.Integer _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim FaceCount As System.Integer
Dim FaceList As Face2
Dim SheetCount As System.Integer
Dim value As Body2

value = instance.IDeleteFacesMakeSheetBodies(FaceCount, FaceList, SheetCount)
```

### C#

```csharp
Body2 IDeleteFacesMakeSheetBodies(
   System.int FaceCount,
   ref Face2 FaceList,
   System.int SheetCount
)
```

### C++/CLI

```cpp
Body2^ IDeleteFacesMakeSheetBodies(
   System.int FaceCount,
   Face2^% FaceList,
   System.int SheetCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceCount`: Number of faces to delete
- `FaceList`: - in-process, unmanaged C++: Pointer to an array of the [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `SheetCount`: Number of sheets bodies to create

### Return Value

- in-process, unmanaged C++: Pointer to an array of sheet [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) created from the deleted faces
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IBody2:IDeleteFacesMakeSheetBodiesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.html) to get the number of sheet bodies to create from the deleted faces.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::DeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.html)
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.html)
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html)
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.html)
[IModeler::ICreateSheetFromSurface2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromSurface2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
