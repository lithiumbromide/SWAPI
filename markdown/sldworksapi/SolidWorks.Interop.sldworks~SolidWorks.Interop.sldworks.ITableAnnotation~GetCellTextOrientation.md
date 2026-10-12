---
title: "GetCellTextOrientation Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetCellTextOrientation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetCellTextOrientation.html"
---

# GetCellTextOrientation Method (ITableAnnotation)

Gets the text orientation in the specified cell of this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCellTextOrientation( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer, _
   ByVal IncludeHidden As System.Boolean, _
   ByVal AllCells As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim IncludeHidden As System.Boolean
Dim AllCells As System.Boolean
Dim value As System.Integer

value = instance.GetCellTextOrientation(Row, Column, IncludeHidden, AllCells)
```

### C#

```csharp
System.int GetCellTextOrientation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.bool AllCells
)
```

### C++/CLI

```cpp
System.int GetCellTextOrientation(
   System.int Row,
   System.int Column,
   System.bool IncludeHidden,
   System.bool AllCells
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: 0-based index of the cell row; valid only if AllCells is set to false
- `Column`: 0-based index of the cell column; valid only if AllCells is set to false
- `IncludeHidden`: True to include hidden rows and columns in Row and Column indexes, false to not
- `AllCells`: True to get the orientation in all cells, false to not; if false, set Row and Column (see **Remarks**)

### Return Value

Text orientation as defined in [swTableCellOrientation_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTableCellOrientation_e.html) (see **Remarks**)

## VBA Syntax

See [TableAnnotation::GetCellTextOrientation](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetCellTextOrientation.html).

## Remarks

If AllCells is set to false, this method returns one of swTableCellOrientation_e.:

- swTableCellOrientation_Right
- swTableCellOrientation_Left
- swTableCellOrientation_Up
- swTableCellOrientation_Down

If AllCells is set to true, this method returns one of the above or:

- swTableCellOrientation_Varies, if all the cells do not share the same text orientation.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::SetCellTextOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetCellTextOrientation.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
