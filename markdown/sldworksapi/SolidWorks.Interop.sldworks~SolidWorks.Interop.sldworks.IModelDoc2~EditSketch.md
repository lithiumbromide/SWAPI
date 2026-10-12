---
title: "EditSketch Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "EditSketch"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.html"
---

# EditSketch Method (IModelDoc2)

Allows the currently selected sketch to be edited.

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditSketch()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.EditSketch()
```

### C#

```csharp
void EditSketch()
```

### C++/CLI

```cpp
void EditSketch();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::EditSketch](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~EditSketch.html).

## Examples

[Autodimension All Sketches (VBA)](Autodimension_All_Sketches_Example_VB.htm)
[Delete All Constraints in Selected Sketch (VBA)](Delete_All_Constraints_in_Selected_Sketch_Example_VB.htm)
[Get Sketch Constraints (VBA)](Get_Sketch_Constraints_Example_VB.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Replace Sketch Text (VBA)](Replace_Sketch_Text_Example_VB.htm)
[Create and Edit Circular Sketch Pattern (VB.NET)](Create_and_Edit_Circular_Sketch_Pattern_Example_VBNET.htm)
[Create and Edit Circular Sketch Pattern (C#)](Create_and_Edit_Circular_Sketch_Pattern_Example_CSharp.htm)
[Create and Edit Circular Sketch Pattern (VBA)](Create_and_Edit_Circular_Sketch_Pattern_Example_VB.htm)

## Remarks

This method corresponds to **SOLIDWORKS menu > Edit > Sketch**. If the selection is a feature, its underlying sketch is placed in edit mode.

After a sketch is in edit mode, you can add or delete geometry from the sketch and perform other standard sketch operations.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::EditSketchOrSingleSketchFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketchOrSingleSketchFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
