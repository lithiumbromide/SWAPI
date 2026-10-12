---
title: "Sort Method (IWeldmentCutListAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListAnnotation"
member: "Sort"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~Sort.html"
---

# Sort Method (IWeldmentCutListAnnotation)

Sorts this weldment cut list by the specified column in the specified sorting direction.

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
Dim instance As IWeldmentCutListAnnotation
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

See [WeldmentCutListAnnotation::Sort](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListAnnotation~Sort.html).

## Examples

[Sort Table (VBA)](Sort_Table_Example_VB.htm)
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)
[Sort Table (C#)](Sort_Table_Example_CSharp.htm)

## Remarks

Weldment cut lists must be sorted by any column except Item Number.

See [Sorting Tables](sldworksapiprogguide.chm::/OVERVIEW/Sorting_Tables.htm) for more information.

## See Also

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.html)
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
