---
title: "GetReferenceEntity Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetReferenceEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetReferenceEntity.html"
---

# GetReferenceEntity Method (ISketch)

Gets the entity on which this sketch was created.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferenceEntity( _
   ByRef LEntityType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim LEntityType As System.Integer
Dim value As System.Object

value = instance.GetReferenceEntity(LEntityType)
```

### C#

```csharp
System.object GetReferenceEntity(
   out System.int LEntityType
)
```

### C++/CLI

```cpp
System.Object^ GetReferenceEntity(
   [Out] System.int LEntityType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LEntityType`: Entity type as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html) (only swSelFACES and swSelDATUMPLANES are valid values for this method)

### Return Value

Either a [reference plane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) or a [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), depending on the value of lEntityType

## VBA Syntax

See [Sketch::GetReferenceEntity](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetReferenceEntity.html).

## Examples

[Get Plane On Which Sketch Created (VBA)](Get_Plane_on_which_Sketch_Created_Example_VB.htm)
[Get Plane or Face for Sketch (VBA)](Get_Plane_or_Face_for_Sketch_Example_VB.htm)

## Remarks

If the sketch resides on a face that is consumed by subsequent features, then this method returns NULL and swSelNOTHING. To get to the face, edit the sketch using [IModelDoc2::EditSketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditSketch.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
