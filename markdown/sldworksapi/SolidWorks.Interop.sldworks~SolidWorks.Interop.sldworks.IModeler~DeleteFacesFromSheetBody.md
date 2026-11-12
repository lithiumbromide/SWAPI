---
title: "DeleteFacesFromSheetBody Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "DeleteFacesFromSheetBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~DeleteFacesFromSheetBody.html"
---

# DeleteFacesFromSheetBody Method (IModeler)

Deletes the unused faces of the sheet body.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteFacesFromSheetBody( _
   ByVal FaceVar As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim FaceVar As System.Object
Dim value As System.Boolean

value = instance.DeleteFacesFromSheetBody(FaceVar)
```

### C#

```csharp
System.bool DeleteFacesFromSheetBody(
   System.object FaceVar
)
```

### C++/CLI

```cpp
System.bool DeleteFacesFromSheetBody(
   System.Object^ FaceVar
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceVar`: Array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to delete from the sheet (surface) body

## VBA Syntax

See [Modeler::DeleteFacesFromSheetBody](ms-its:sldworksapivb6.chm::/sldworks~Modeler~DeleteFacesFromSheetBody.html).

## Remarks

Use this method to remove the unused faces from the sheet body created by [IModeler::CreateBrepBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~CreateBrepBody3.html) and [IModeler::ICreateBrepBody3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBrepBody3.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
[IModeler::IDeleteFacesFromSheetBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~IDeleteFacesFromSheetBody.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
