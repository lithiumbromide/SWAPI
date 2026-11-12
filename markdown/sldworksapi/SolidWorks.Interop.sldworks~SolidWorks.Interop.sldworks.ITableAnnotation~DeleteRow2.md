---
title: "DeleteRow2 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "DeleteRow2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteRow2.html"
---

# DeleteRow2 Method (ITableAnnotation)

Deletes the specified row from this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteRow2( _
   ByVal Index As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.Boolean

value = instance.DeleteRow2(Index, IncludeHidden)
```

### C#

```csharp
System.bool DeleteRow2(
   System.int Index,
   System.bool IncludeHidden
)
```

### C++/CLI

```cpp
System.bool DeleteRow2(
   System.int Index,
   System.bool IncludeHidden
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the row you want to delete
- `IncludeHidden`: True to delete the hidden row, false to not

### Return Value

True if the row is deleted successfully, false if not

## VBA Syntax

See [TableAnnotation::DeleteRow2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~DeleteRow2.html).

## Remarks

The index for both the rows and columns is 0-based.

This method deletes the entire table if you try to delete the only row in the table.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::InsertRow Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertRow.html)
[ITableAnnotation::RowCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowCount.html)
[ITableAnnotation::RowHidden Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~RowHidden.html)
[ITableAnnotation::TotalRowCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalRowCount.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
