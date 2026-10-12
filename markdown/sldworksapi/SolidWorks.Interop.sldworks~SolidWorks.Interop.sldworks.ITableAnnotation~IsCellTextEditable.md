---
title: "IsCellTextEditable Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "IsCellTextEditable"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.html"
---

# IsCellTextEditable Method (ITableAnnotation)

Gets whether the text in this cell can be edited.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsCellTextEditable( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As System.Boolean

value = instance.IsCellTextEditable(Row, Column)
```

### C#

```csharp
System.bool IsCellTextEditable(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.bool IsCellTextEditable(
   System.int Row,
   System.int Column
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of row in which cell resides
- `Column`: Index of column in which cell resides

### Return Value

True if text in this cell can be edited, false if not

## VBA Syntax

See [TableAnnotation::IsCellTextEditable](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~IsCellTextEditable.html).

## Remarks

The index for both rows and columns is 0-based.

Tables and cells:

- [BOM table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html): All cells can be edited.
- [General table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html): All cells can be edited.
- [Hole table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html): Only some columns can be edited because some information is automatically generated, thus, that information cannot be edited. The header row and custom columns can be edited.
- [Revision table annotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation.html): All cells can be edited.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.html)
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.html)
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)
[ITableAnnotation::DisplayedText Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DisplayedText.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
