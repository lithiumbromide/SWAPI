---
title: "Text Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "Text"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text.html"
---

# Text Property (ITableAnnotation)

Obsolete. Superseded by [ITableAnnotation::Text2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Text( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As System.String

instance.Text(Row, Column) = value

value = instance.Text(Row, Column)
```

### C#

```csharp
System.string Text(
   System.int Row,
   System.int Column
) {get; set;}
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get(System.int Row, System.int Column);
   void set (System.int Row, System.int Column, System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of the row
- `Column`: Index of the column

### Property Value

Cell text

## VBA Syntax

See [TableAnnotation::Text](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~Text.html).

## Examples

[Get Table Annotation and Contents (VBA)](Get_Table_Annotation_and_Contents_Example_VB.htm)
[Insert Hole Table (VBA)](Insert_Hole_Table_Example_VB.htm)

## Remarks

Index for both rows and columns is 0-based.

This property returns the string that drives the text displayed in the specified cell. For example, the string returned by this property would be the parameter string if the cell is linked to a dimension value or custom property. To get the text actually displayed in the cell, use [ITableAnnotation::DisplayedText](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~DisplayedText.html).

Table annotation:

- [BOM](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html): All cells are editable.
- [General](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html): All cells are editable.
- [Hole](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html): Only some columns are editable because some information is automatically generated, thus, that information cannot be edited. The header row and custom columns are editable.
- [Revision](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableFeature.html): All cells are editable

You might experience decreased performance when updating the text in multiple cells in large tables because the table is rebuilt after changing the text in a cell. To increase performance while updating the text in large tables:

1. Set [IAnnotation::Visible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation~Visible.html) to false. (The table is not rebuilt while the table is hidden.)
2. Update the text in the table cells.
3. Set IAnnotation::Visible to true.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html)
[ITableAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetTextFormat.html)
[ITableAnnotation::GetUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetUseDocTextFormat.html)
[ITableAnnotation::IsCellTextEditable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.html)
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetTextFormat.html)
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
