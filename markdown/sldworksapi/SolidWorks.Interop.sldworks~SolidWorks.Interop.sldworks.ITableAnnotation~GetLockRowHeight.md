---
title: "GetLockRowHeight Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetLockRowHeight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.html"
---

# GetLockRowHeight Method (ITableAnnotation)

Gets whether the height of the specified row is locked in this table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLockRowHeight( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.GetLockRowHeight(Index)
```

### C#

```csharp
System.bool GetLockRowHeight(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool GetLockRowHeight(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index of the row (see **Remarks**)

### Return Value

True if the specified row's height is locked, false if not

## VBA Syntax

See [TableAnnotation::GetLockRowHeight](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetLockRowHeight.html).

## Examples

[Get Components in Each BOM Table Row (C#)](Get_Components_in_Each_BOM_Table_Row_Example_CSharp.htm)
[Get Components in Each BOM Table Row (VB.NET)](Get_Components_in_Each_BOM_Table_Row_Example_VBNET.htm)
[Get Components in Each BOM Table Row (VBA)](Get_Components_in_Each_BOM_Table_Row_VB.htm)

## Remarks

Call [ITableAnnotation::RowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.html) to get the number of visible rows or [ITableAnnotation::TotalRowCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.html) to get the number of visible and hidden rows in this table annotation.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::SetLockRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.html)
[ITableAnnotation::DeleteRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.html)
[ITableAnnotation::GetRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.html)
[ITableAnnotation::GetRowVerticalGap Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.html)
[ITableAnnotation::InsertRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.html)
[ITableAnnotation::MoveRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.html)
[ITableAnnotation::SetRowHeight Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.html)
[ITableAnnotation::SetRowVerticalGap Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.html)
[ITableAnnotation::RowHidden Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.html)

## Availability

SOLIDWORKS 2017 FCS, Revision Number 25.0
