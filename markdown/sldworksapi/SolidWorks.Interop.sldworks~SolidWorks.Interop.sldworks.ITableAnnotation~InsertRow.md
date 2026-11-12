---
title: "InsertRow Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "InsertRow"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.html"
---

# InsertRow Method (ITableAnnotation)

Inserts a row into this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertRow( _
   ByVal Where As System.Integer, _
   ByVal Index As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim Index As System.Integer
Dim value As System.Boolean

value = instance.InsertRow(Where, Index)
```

### C#

```csharp
System.bool InsertRow(
   System.int Where,
   System.int Index
)
```

### C++/CLI

```cpp
System.bool InsertRow(
   System.int Where,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Where`: Where to insert the new row as defined in [swTableItemInsertPosition_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableItemInsertPosition_e.html)
- `Index`: Index of row where to insert new row (see **Remarks**)

## VBA Syntax

See [TableAnnotation::InsertRow](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~InsertRow.html).

## Examples

[Sort Table (VBA)](Sort_Table_Example_VB.htm)
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)
[Sort Table (C#)](Sort_Table_Example_CSharp.htm)

## Remarks

Index:

- is 0-based.
- is valid only if Where is set to swTableItemInsertPosition_e.swTableItemInsertPosition_After or swTableItemInsertPosition_e.swTableItemInsertPosition_Before.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.html)
[ITableAnnotation::GetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.html)
[ITableAnnotation::GetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.html)
[ITableAnnotation::MoveRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.html)
[ITableAnnotation::SetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.html)
[ITableAnnotation::SetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.html)
[ITableAnnotation::RowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.html)
[ITableAnnotation::TotalRowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.html)
[ITableAnnotation::GetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.html)
[ITableAnnotation::SetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.html)
[ITableAnnotation::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
