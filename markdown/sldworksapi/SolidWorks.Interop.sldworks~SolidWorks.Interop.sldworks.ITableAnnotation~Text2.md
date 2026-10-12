---
title: "Text2 Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "Text2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text2.html"
---

# Text2 Property (ITableAnnotation)

Gets or sets the parametrized string of text for the specified cell of this table.

## Syntax

### Visual Basic (Declaration)

```vb
Property Text2( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.String

instance.Text2(Row, Column, IncludeHidden) = value

value = instance.Text2(Row, Column, IncludeHidden)
```

### C#

```csharp
System.string Text2(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ Text2 {
   System.String^ get(System.int Row, System.int Column, System.bool IncludeHidden);
   void set (System.int Row, System.int Column, System.bool IncludeHidden, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of the row
- `Column`: Index of the column
- `IncludeHidden`: True to get or set text in the hidden cell, false to not

### Property Value

Cell text

## VBA Syntax

See [TableAnnotation::Text2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~Text2.html).

## Examples

[Insert BOM Table and Extract Data (VBA)](Insert_BOM_Table_and_Extract_Data_Example_VB.htm)
[Insert BOM Table and Extract Data (VB.NET)](Insert_BOM_Table_and_Extract_Data_Example_VBNET.htm)
[Insert BOM Table and Extract Data (C#)](Insert_BOM_Table_and_Extract_Data_Example_CSharp.htm)

## Remarks

Index for both rows and columns is 0-based.

This property returns the string that drives the text displayed in the specified cell. For example, the string returned by this property would be the parameter string if the cell is linked to a dimension value or custom property. To get the text actually displayed in the cell, use [ITableAnnotation::DisplayedText2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText2.html).

Table annotation:

- [BOM](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html): All cells are editable.
- [General](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation.html): All cells are editable.
- [Hole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html): Only columns that are not automatically generated are editable. The header row and custom columns are editable.
- [Revision](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableFeature.html): All cells are editable

You might experience decreased performance when updating the text in multiple cells in large tables, because the table automatically rebuilds each time you change the text in a cell. To increase performance while updating the text in large tables:

1. Set [IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Visible.html) to false. (The table is not rebuilt while the table is hidden.)
2. Update the text in the table cells.
3. Set IAnnotation::Visible to true.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
