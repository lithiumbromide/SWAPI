---
title: "TotalRowCount Property (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "TotalRowCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.html"
---

# TotalRowCount Property (ITableAnnotation)

Gets the total number of visible and hidden rows in this table.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TotalRowCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim value As System.Integer

value = instance.TotalRowCount
```

### C#

```csharp
System.int TotalRowCount {get;}
```

### C++/CLI

```cpp
property System.int TotalRowCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Total number of visible and hidden rows in this table

## VBA Syntax

See [TableAnnotation::TotalRowCount](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~TotalRowCount.html).

## Examples

[Get the Total Number of Columns and Rows in a Table (C#)](Get_Total_Columns_Rows_Example_CSharp.htm)
[Get the Total Number of Columns and Rows in a Table (VB.NET)](Get_Total_Columns_Rows_Example_VBNET.htm)
[Get the Total Number of Columns and Rows in a Table (VBA)](Get_Total_Columns_Rows_Example_VB.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.html)
[ITableAnnotation::GetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.html)
[ITableAnnotation::GetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.html)
[ITableAnnotation::InsertRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.html)
[ITableAnnotation::MoveRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.html)
[ITableAnnotation::SetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.html)
[ITableAnnotation::SetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.html)
[ITableAnnotation::RowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.html)
[ITableAnnotation::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.html)
[ITableAnnotation::GetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.html)
[ITableAnnotation::SetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.html)

## Availability

SOLIDWORKS 2011 SP05, Revision Number 19.5
