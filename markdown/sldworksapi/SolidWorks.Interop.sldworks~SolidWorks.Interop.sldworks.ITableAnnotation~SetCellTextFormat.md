---
title: "SetCellTextFormat Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetCellTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html"
---

# SetCellTextFormat Method (ITableAnnotation)

Sets the text format for the text in the specified cell.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetCellTextFormat( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal UseDoc As System.Boolean, _
   ByVal TextFormat As TextFormat _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim UseDoc As System.Boolean
Dim TextFormat As TextFormat
Dim value As System.Boolean

value = instance.SetCellTextFormat(Row, Column, UseDoc, TextFormat)
```

### C#

```csharp
System.bool SetCellTextFormat(
   System.int Row,
   System.int Column,
   System.bool UseDoc,
   TextFormat TextFormat
)
```

### C++/CLI

```cpp
System.bool SetCellTextFormat(
   System.int Row,
   System.int Column,
   System.bool UseDoc,
   TextFormat^ TextFormat
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of row in which cell resides
- `Column`: Index of column in which cell resides
- `UseDoc`: True to use the document setting for the text format, false to not
- `TextFormat`: [ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object

### Return Value

True if the text format is set, false if not

## VBA Syntax

See [TableAnnotation::SetCellTextFormat](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetCellTextFormat.html).

## Remarks

The index for both rows and columns is 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellRange.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::IsCellTextEditable Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellTextEditable.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellRange.html)
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.html)
[ITableAnnotation::CellTextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextHorizontalJustification.html)
[ITableAnnotation::CellTextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~CellTextVerticalJustification.html)
[ITableAnnotation::TextHorizontalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextHorizontalJustification.html)
[ITableAnnotation::TextVerticalJustification Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TextVerticalJustification.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
