---
title: "DeleteColumn2 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "DeleteColumn2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~DeleteColumn2.html"
---

# DeleteColumn2 Method (ITableAnnotation)

Deletes the specified column in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteColumn2( _
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

value = instance.DeleteColumn2(Index, IncludeHidden)
```

### C#

```csharp
System.bool DeleteColumn2(
   System.int Index,
   System.bool IncludeHidden
)
```

### C++/CLI

```cpp
System.bool DeleteColumn2(
   System.int Index,
   System.bool IncludeHidden
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the column you want to delete
- `IncludeHidden`: True to delete the hidden column, false to not

### Return Value

True if column is deleted successfully, false if not

## VBA Syntax

See [TableAnnotation::DeleteColumn2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~DeleteColumn2.html).

## Remarks

The index for both the rows and columns is 0-based.

This method deletes the entire table if you try to delete the only column in the table.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::InsertColumn2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~InsertColumn2.html)
[ITableAnnotation::ColumnCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnCount.html)
[ITableAnnotation::ColumnHidden Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~ColumnHidden.html)
[ITableAnnotation::TotalColumnCount Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~TotalColumnCount.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
