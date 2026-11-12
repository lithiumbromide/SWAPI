---
title: "ICreateSheetBody Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "ICreateSheetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.html"
---

# ICreateSheetBody Method (IFace2)

Creates a sheet body from this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSheetBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As Body2

value = instance.ICreateSheetBody()
```

### C#

```csharp
Body2 ICreateSheetBody()
```

### C++/CLI

```cpp
Body2^ ICreateSheetBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

New sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Face2::ICreateSheetBody](ms-its:sldworksapivb6.chm::/sldworks~Face2~ICreateSheetBody.html).

## Remarks

A sheet body is a surface body.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::CreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.html)
[IFace2::CreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html)
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html)
[IBody2::DeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.html)
[IBody2::IDeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.html)
[IBody2::IDeleteFacesMakeSheetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.html)
[IModeler::CreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateBodiesFromSheets2.html)
[IModeler::ICreateBodiesFromSheets2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodiesFromSheets2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
