---
title: "ICreateSheetBodyByFaceExtension Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "ICreateSheetBodyByFaceExtension"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html"
---

# ICreateSheetBodyByFaceExtension Method (IFace2)

Creates a sheet body by extending the face.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSheetBodyByFaceExtension( _
   ByRef BoxLowIn As System.Double, _
   ByRef BoxHighIn As System.Double _
) As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim BoxLowIn As System.Double
Dim BoxHighIn As System.Double
Dim value As Body2

value = instance.ICreateSheetBodyByFaceExtension(BoxLowIn, BoxHighIn)
```

### C#

```csharp
Body2 ICreateSheetBodyByFaceExtension(
   ref System.double BoxLowIn,
   ref System.double BoxHighIn
)
```

### C++/CLI

```cpp
Body2^ ICreateSheetBodyByFaceExtension(
   System.double% BoxLowIn,
   System.double% BoxHighIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoxLowIn`: Pointer to an array of 3 doubles (x,y,z)
- `BoxHighIn`: Pointer to an array of 3 doubles (x,y,z)

### Return Value

Pointer to the newly created sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Face2::ICreateSheetBodyByFaceExtension](ms-its:sldworksapivb6.chm::/sldworks~Face2~ICreateSheetBodyByFaceExtension.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IBody2::DeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.html)
[IBody2::IDeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.html)
[IBody2::IDeleteFacesMakeSheetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.html)
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.html)
[IFace2::CreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html)
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.html)
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
