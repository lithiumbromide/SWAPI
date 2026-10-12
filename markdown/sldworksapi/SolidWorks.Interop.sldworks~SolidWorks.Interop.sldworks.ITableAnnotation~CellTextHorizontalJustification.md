---
title: "CellTextHorizontalJustification Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "CellTextHorizontalJustification"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html"
---

# CellTextHorizontalJustification Property (ITableAnnotation)

Gets or sets the horizontal justification for the text in the specified cell.

## Syntax

### Visual Basic (Declaration)

```vb
Property CellTextHorizontalJustification( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As System.Integer

instance.CellTextHorizontalJustification(Row, Column) = value

value = instance.CellTextHorizontalJustification(Row, Column)
```

### C#

```csharp
System.int CellTextHorizontalJustification(
   System.int Row,
   System.int Column
) {get; set;}
```

### C++/CLI

```cpp
property System.int CellTextHorizontalJustification {
   System.int get(System.int Row, System.int Column);
   void set (System.int Row, System.int Column, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of the row in which the cell resides
- `Column`: Index of the column in which the cell resides

### Property Value

Justification as defined by [swTextJustification_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTextJustification_e.html)

## VBA Syntax

See [TableAnnotation::CellTextHorizontalJustification](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~CellTextHorizontalJustification.html).

## Remarks

The index for both the rows and columns is 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::IsCellTextEditable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.html)
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)
[ITableAnnotation::TextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextHorizontalJustification.html)
[ITableAnnotation::TextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextVerticalJustification.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
