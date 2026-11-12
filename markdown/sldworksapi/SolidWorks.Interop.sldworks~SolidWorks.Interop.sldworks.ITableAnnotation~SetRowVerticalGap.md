---
title: "SetRowVerticalGap Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "SetRowVerticalGap"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowVerticalGap.html"
---

# SetRowVerticalGap Method (ITableAnnotation)

Sets the gap between the text and the top or bottom of the specified row of this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetRowVerticalGap( _
   ByVal Index As System.Integer, _
   ByVal Gap As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Gap As System.Double
Dim value As System.Boolean

value = instance.SetRowVerticalGap(Index, Gap)
```

### C#

```csharp
System.bool SetRowVerticalGap(
   System.int Index,
   System.double Gap
)
```

### C++/CLI

```cpp
System.bool SetRowVerticalGap(
   System.int Index,
   System.double Gap
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of row for which to get the height
- `Gap`: Gap in system units

### Return Value

True if the gap is set, false if not

## VBA Syntax

See [TableAnnotation::SetRowVerticalGap](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~SetRowVerticalGap.html).

## Remarks

Use [ITableAnnotation::GetRowVerticalGap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~GetRowVerticalGap.html) to get the size of the gap.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::DeleteRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow.html)
[ITableAnnotation::GetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetRowHeight.html)
[ITableAnnotation::InsertRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.html)
[ITableAnnotation::MoveRow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MoveRow.html)
[ITableAnnotation::SetRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetRowHeight.html)
[ITableAnnotation::RowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.html)
[ITableAnnotation::TotalRowCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.html)
[ITableAnnotation::RowHidden Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.html)
[ITableAnnotation::GetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetLockRowHeight.html)
[ITableAnnotation::SetLockRowHeight Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetLockRowHeight.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
