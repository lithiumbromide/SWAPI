---
title: "GetCellTextFormat Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetCellTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html"
---

# GetCellTextFormat Method (ITableAnnotation)

Gets the text format for the specified cell in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCellTextFormat( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As TextFormat
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As TextFormat

value = instance.GetCellTextFormat(Row, Column)
```

### C#

```csharp
TextFormat GetCellTextFormat(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
TextFormat^ GetCellTextFormat(
   System.int Row,
   System.int Column
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of the row in which the cell is located
- `Column`: Index of the column in which the cell is located

### Return Value

[ITextFormat](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITextFormat.html) object

## VBA Syntax

See [TableAnnotation::GetCellTextFormat](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetCellTextFormat.html).

## Remarks

The index for both the rows and columns is 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellUseDocTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html)
[ITableAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetTextFormat.html)
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetTextFormat.html)
[ITableAnnotation::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
