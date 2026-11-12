---
title: "GetEndPoint2 Method (ISketchLine)"
project: "SOLIDWORKS API Help"
interface: "ISketchLine"
member: "GetEndPoint2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~GetEndPoint2.html"
---

# GetEndPoint2 Method (ISketchLine)

Gets the sketch point for the end point of the line.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndPoint2() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchLine
Dim value As System.Object

value = instance.GetEndPoint2()
```

### C#

```csharp
System.object GetEndPoint2()
```

### C++/CLI

```cpp
System.Object^ GetEndPoint2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

End [sketch point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchPoint.html) or NULL if the operation fails

## VBA Syntax

See [SketchLine::GetEndPoint2](ms-its:sldworksapivb6.chm::/sldworks~SketchLine~GetEndPoint2.html).

## Examples

[Create Imported Surface Body From Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)
[Get Names of Sketch Segments (VBA)](Get_Names_of_Sketch_Segments_Example_VB.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Autodimension All Sketches (C#)](Autodimension_All_Sketches_Example_CSharp.htm)
[Autodimension All Sketches (VB.NET)](Autodimension_All_Sketches_Example_VBNET.htm)
[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)

## See Also

[ISketchLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.html)
[ISketchLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html)
[ISketchLine::IGetEndPoint2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine~IGetEndPoint2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
