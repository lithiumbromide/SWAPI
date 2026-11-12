---
title: "SetCellTextOrientation Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetCellTextOrientation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextOrientation.html"
---

# SetCellTextOrientation Method (ITableAnnotation)

Sets the text orientation in the specified table cell.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCellTextOrientation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal AllCells As System.Boolean, _
   ByVal Orientation As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim AllCells As System.Boolean
Dim Orientation As System.Integer

instance.SetCellTextOrientation(Row, Column, IncludeHidden, AllCells, Orientation)
```

### C#

```csharp
void SetCellTextOrientation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.bool AllCells,
   System.int Orientation
)
```

### C++/CLI

```cpp
void SetCellTextOrientation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.bool AllCells,
   System.int Orientation
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: 0-based index of row; valid only if AllCells is set to false
- `Column`: 0-based index of column; valid only if AllCells is set to false
- `IncludeHidden`: True to include hidden rows and columns in the Row and Column indexes, false to not
- `AllCells`: True for all cells, false if not; if false, set Row and Column
- `Orientation`: Text orientation as defined in [swTableCellOrientation_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableCellOrientation_e.html) (see **Remarks**)

## VBA Syntax

See [TableAnnotation::SetCellTextOrientation](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetCellTextOrientation.html).

## Remarks

You can set Orientation to any member of swTableCellOrientation_e except swTableCellOrientation_Varies.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetCellTextOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextOrientation.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
