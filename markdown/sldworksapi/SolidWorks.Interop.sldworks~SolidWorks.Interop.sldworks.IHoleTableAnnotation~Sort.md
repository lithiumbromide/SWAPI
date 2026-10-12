---
title: "Sort Method (IHoleTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IHoleTableAnnotation"
member: "Sort"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation~Sort.html"
---

# Sort Method (IHoleTableAnnotation)

Sorts this hole table by the specified column in the specified sorting direction.

## Syntax

### Visual Basic (Declaration)

```vb
Function Sort( _
   ByVal ColumnIndex As System.Integer, _
   ByVal SortAscending As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleTableAnnotation
Dim ColumnIndex As System.Integer
Dim SortAscending As System.Boolean
Dim value As System.Boolean

value = instance.Sort(ColumnIndex, SortAscending)
```

### C#

```csharp
System.bool Sort(
   System.int ColumnIndex,
   System.bool SortAscending
)
```

### C++/CLI

```cpp
System.bool Sort(
   System.int ColumnIndex,
   System.bool SortAscending
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColumnIndex`: 0-based index of column to sort by (see **Remarks**)
- `SortAscending`: True to sort ascending, false to sort descending

### Return Value

True if sorted successfully, false if not

## VBA Syntax

See [HoleTableAnnotation::Sort](ms-its:sldworksapivb6.chm::/sldworks~HoleTableAnnotation~Sort.html).

## Examples

[Sort Table (C#)](Sort_Table_Example_CSharp.htm)
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)
[Sort Table (VBA)](Sort_Table_Example_VB.htm)

## Remarks

Hole tables must be sorted by the Tag column.

See [Sorting Tables](sldworksapiprogguide.chm::/OVERVIEW/Sorting_Tables.htm) for more information.

## See Also

[IHoleTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation.html)
[IHoleTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
