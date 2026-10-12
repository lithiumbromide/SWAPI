---
title: "CreateSheetBodyByFaceExtension Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "CreateSheetBodyByFaceExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html"
---

# CreateSheetBodyByFaceExtension Method (IFace2)

Creates a sheet body by extending the face.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSheetBodyByFaceExtension( _
   ByVal BoxLowIn As System.Object, _
   ByVal BoxHighIn As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim BoxLowIn As System.Object
Dim BoxHighIn As System.Object
Dim value As System.Object

value = instance.CreateSheetBodyByFaceExtension(BoxLowIn, BoxHighIn)
```

### C#

```csharp
System.object CreateSheetBodyByFaceExtension(
   System.object BoxLowIn,
   System.object BoxHighIn
)
```

### C++/CLI

```cpp
System.Object^ CreateSheetBodyByFaceExtension(
   System.Object^ BoxLowIn,
   System.Object^ BoxHighIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoxLowIn`: Array of 3 doubles (x,y,z)
- `BoxHighIn`: Array of 3 doubles (x,y,z)

### Return Value

Newly created sheet body

## VBA Syntax

See [Face2::CreateSheetBodyByFaceExtension](ms-its:sldworksapivb6.chm::/sldworks~Face2~CreateSheetBodyByFaceExtension.html).

## Remarks

A sheet body is a surface body.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html)
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.html)
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.html)
[IBody2::DeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.html)
[IBody2::IDeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.html)
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.html)
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.html)
[IBody2::IDeleteFacesMakeSheetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
