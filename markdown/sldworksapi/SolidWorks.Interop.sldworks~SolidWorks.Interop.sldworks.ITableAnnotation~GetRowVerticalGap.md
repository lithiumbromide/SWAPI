---
title: "GetRowVerticalGap Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetRowVerticalGap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.html"
---

# GetRowVerticalGap Method (ITableAnnotation)

Gets the gap between the text and the top or bottom of the specified row of this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRowVerticalGap( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim value As System.Double

value = instance.GetRowVerticalGap(Index)
```

### C#

```csharp
System.double GetRowVerticalGap(
   System.int Index
)
```

### C++/CLI

```cpp
System.double GetRowVerticalGap(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of row for which to get the height

### Return Value

Gap in system units

## VBA Syntax

See [TableAnnotation::GetRowVerticalGap](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetRowVerticalGap.html).

## Remarks

Use [ITableAnnotation::SetRowVerticalGap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.html) to set the size of the gap.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.html)
[ITableAnnotation::GetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.html)
[ITableAnnotation::MoveRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.html)
[ITableAnnotation::SetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.html)
[ITableAnnotation::TotalRowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.html)
[ITableAnnotation::GetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.html)
[ITableAnnotation::GetRowVerticalGap Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.html)
[ITableAnnotation::InsertRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.html)
[ITableAnnotation::SetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.html)
[ITableAnnotation::RowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.html)
[ITableAnnotation::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
