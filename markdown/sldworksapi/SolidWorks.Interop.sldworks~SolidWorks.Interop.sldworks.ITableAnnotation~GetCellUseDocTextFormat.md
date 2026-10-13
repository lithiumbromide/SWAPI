---
title: "GetCellUseDocTextFormat Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetCellUseDocTextFormat"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellUseDocTextFormat.html"
---

# GetCellUseDocTextFormat Method (ITableAnnotation)

Gets whether this cell uses the document setting for its text format.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCellUseDocTextFormat( _
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

value = instance.GetCellUseDocTextFormat(Row, Column)
```

### C#

```csharp
System.bool GetCellUseDocTextFormat(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.bool GetCellUseDocTextFormat(
   System.int Row,
   System.int Column
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of the row in which the cell resides
- `Column`: Index of the column in which the cell resides

### Return Value

True to use the document setting for its text format, false to not

## VBA Syntax

See [TableAnnotation::GetCellUseDocTextFormat](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetCellUseDocTextFormat.html).

## Remarks

The index for both the rows and columns in this table are 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextFormat.html)
[ITableAnnotation::GetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetTextFormat.html)
[ITableAnnotation::SetCellTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextFormat.html)
[ITableAnnotation::SetTextFormat Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetTextFormat.html)
[ITableAnnotation::Text Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Text.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
