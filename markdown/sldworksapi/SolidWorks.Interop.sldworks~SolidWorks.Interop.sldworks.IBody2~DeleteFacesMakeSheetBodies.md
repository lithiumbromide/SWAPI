---
title: "DeleteFacesMakeSheetBodies Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DeleteFacesMakeSheetBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.html"
---

# DeleteFacesMakeSheetBodies Method (IBody2)

Creates sheet bodies from deleted faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteFacesMakeSheetBodies( _
   ByVal FaceList As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim FaceList As System.Object
Dim value As System.Object

value = instance.DeleteFacesMakeSheetBodies(FaceList)
```

### C#

```csharp
System.object DeleteFacesMakeSheetBodies(
   System.object FaceList
)
```

### C++/CLI

```cpp
System.Object^ DeleteFacesMakeSheetBodies(
   System.Object^ FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceList`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to delete

### Return Value

Array of sheet [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) created from the deleted faces

## VBA Syntax

See [Body2::DeleteFacesMakeSheetBodies](ms-its:sldworksapivb6.chm::/sldworks~Body2~DeleteFacesMakeSheetBodies.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IDeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.html)
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.html)
[IFace2::CreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html)
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.html)
[IModeler::CreateSheetFromSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromSurface.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
