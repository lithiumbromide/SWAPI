---
title: "IDeleteFacesFromSheetBody Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "IDeleteFacesFromSheetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IDeleteFacesFromSheetBody.html"
---

# IDeleteFacesFromSheetBody Method (IModeler)

Deletes the unused faces of the sheet body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IDeleteFacesFromSheetBody( _
   ByVal Count As System.Integer, _
   ByRef FaceVar As Face2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Count As System.Integer
Dim FaceVar As Face2
Dim value As System.Boolean

value = instance.IDeleteFacesFromSheetBody(Count, FaceVar)
```

### C#

```csharp
System.bool IDeleteFacesFromSheetBody(
   System.int Count,
   ref Face2 FaceVar
)
```

### C++/CLI

```cpp
System.bool IDeleteFacesFromSheetBody(
   System.int Count,
   Face2^% FaceVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Count`: Number of faces to delete
- `FaceVar`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to delete from the sheet (surface) body

### Return Value

True if all of the faces are deleted, false if not

## VBA Syntax

See [Modeler::IDeleteFacesFromSheetBody](ms-its:sldworksapivb6.chm::/sldworks~Modeler~IDeleteFacesFromSheetBody.html).

## Remarks

Use this method to remove the unused faces from the sheet body created by [IModeler::CreateBrepBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBrepBody3.html) and [IModeler::ICreateBrepBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBrepBody3.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::DeleteFacesFromSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~DeleteFacesFromSheetBody.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
