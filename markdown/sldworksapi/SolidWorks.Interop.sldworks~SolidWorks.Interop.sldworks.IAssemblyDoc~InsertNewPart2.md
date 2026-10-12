---
title: "InsertNewPart2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertNewPart2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewPart2.html"
---

# InsertNewPart2 Method (IAssemblyDoc)

Inserts a new part on the specified face or plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertNewPart2( _
   ByVal FilePathIn As System.String, _
   ByVal Face_or_Plane_to_select As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim FilePathIn As System.String
Dim Face_or_Plane_to_select As System.Object
Dim value As System.Integer

value = instance.InsertNewPart2(FilePathIn, Face_or_Plane_to_select)
```

### C#

```csharp
System.int InsertNewPart2(
   System.string FilePathIn,
   System.object Face_or_Plane_to_select
)
```

### C++/CLI

```cpp
System.int InsertNewPart2(
   System.String^ FilePathIn,
   System.Object^ Face_or_Plane_to_select
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePathIn`: Path and filename for the new part
- `Face_or_Plane_to_select`: [Face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [reference plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) where to insert the new part

### Return Value

Error code as defined by [swInsertNewPartErrorCode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInsertNewPartErrorCode_e.html)

## VBA Syntax

See [AssemblyDoc::InsertNewPart2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertNewPart2.html).

## Examples

[Insert Join Feature (C#)](Insert_Join_Feature_Example_CSharp.htm)
[Insert Join Feature (VB.NET)](Insert_Join_Feature_Example_VBNET.htm)
[Insert Join Feature (VBA)](Insert_Join_Feature_Example_VB.htm)

## Remarks

The Face_or_Plane_to_select argument can be a [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) or [reference plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html), which means that you have to call [IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html) first.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12
