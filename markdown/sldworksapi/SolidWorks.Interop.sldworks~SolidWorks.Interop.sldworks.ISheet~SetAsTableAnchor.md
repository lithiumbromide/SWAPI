---
title: "SetAsTableAnchor Method (ISheet)"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: "SetAsTableAnchor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~SetAsTableAnchor.html"
---

# SetAsTableAnchor Method (ISheet)

Sets the anchor for the specified table at a selected point in the sheet format.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAsTableAnchor( _
   ByVal TableType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
Dim TableType As System.Integer
Dim value As System.Object

value = instance.SetAsTableAnchor(TableType)
```

### C#

```csharp
System.object SetAsTableAnchor(
   System.int TableType
)
```

### C++/CLI

```cpp
System.Object^ SetAsTableAnchor(
   System.int TableType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TableType`: Table for which an anchor is required as defined in [swTableAnnotationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableAnnotationType_e.html)

### Return Value

[ITableAnchor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.html)

## VBA Syntax

See [Sheet::SetAsTableAnchor](ms-its:sldworksapivb6.chm::/Sldworks~Sheet~SetAsTableAnchor.html).

## Examples

[Set Table Anchors in Sheet Formats (VBA)](Set_Table_Anchors_Example_VB.htm)
[Set Table Anchors in Sheet Formats (VB.NET)](Set_Table_Anchors_Example_VBNET.htm)
[Set Table Anchors in Sheet Formats (C#)](Set_Table_Anchors_Example_CSharp.htm)

## Remarks

Before calling this method, you must call:

1. [IDrawingDoc::EditTemplate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditTemplate.html) to edit the sheet format.
2. [IModelDoc2::EditSketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditSketch.html) to create a sketch.
3. [ISketchManager::CreatePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePoint.html) to create a sketch point where to position the table anchor.

If an anchor already exists for the table, then this method moves the anchor of that table to the selected position.

After calling this method you must call:

1. [IDrawingDoc::EditSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html)
2. IModelDoc2::EditSketch
3. [IModelDoc2::ForceRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceRebuild3.html)

## See Also

[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[ISheet::TableAnchor Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet~TableAnchor.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
