---
title: "CreateSheetBody Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "CreateSheetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBody.html"
---

# CreateSheetBody Method (IFace2)

Creates a sheet body from this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSheetBody() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.CreateSheetBody()
```

### C#

```csharp
System.object CreateSheetBody()
```

### C++/CLI

```cpp
System.Object^ CreateSheetBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

New sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [Face2::CreateSheetBody](ms-its:sldworksapivb6.chm::/sldworks~Face2~CreateSheetBody.html).

## Remarks

A sheet body is a surface body.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::ICreateSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBody.html)
[IFace2::ICreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~ICreateSheetBodyByFaceExtension.html)
[IFace2::CreateSheetBodyByFaceExtension Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~CreateSheetBodyByFaceExtension.html)
[IModeler::CreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CreateSheetFromFaces.html)
[IModeler::ICreateSheetFromFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateSheetFromFaces.html)
[IBody2::DeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFacesMakeSheetBodies.html)
[IBody2::IDeleteFacesMakeSheetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodies.html)
[IBody2::IDeleteFacesMakeSheetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IDeleteFacesMakeSheetBodiesCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
