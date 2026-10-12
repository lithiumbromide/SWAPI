---
title: "ColumnIndex Property (IBomTableSortData)"
project: "SOLIDWORKS API Help"
interface: "IBomTableSortData"
member: "ColumnIndex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~ColumnIndex.html"
---

# ColumnIndex Property (IBomTableSortData)

Gets and sets the column index for the specified sort order index.

## Syntax

### Visual Basic (Declaration)

```vb
Property ColumnIndex( _
   ByVal SortOrderIndex As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableSortData
Dim SortOrderIndex As System.Integer
Dim value As System.Integer

instance.ColumnIndex(SortOrderIndex) = value

value = instance.ColumnIndex(SortOrderIndex)
```

### C#

```csharp
System.int ColumnIndex(
   System.int SortOrderIndex
) {get; set;}
```

### C++/CLI

```cpp
property System.int ColumnIndex {
   System.int get(System.int SortOrderIndex);
   void set (System.int SortOrderIndex, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SortOrderIndex`: 0 for primary sort, 1 for secondary sort, 2 for tertiary sort (see **Remarks**)

### Property Value

0-based column index mapped to the specified SortOrderIndex; specify -1 if the specified SortOrderIndex is not used

## VBA Syntax

See [BomTableSortData::ColumnIndex](ms-its:sldworksapivb6.chm::/sldworks~BomTableSortData~ColumnIndex.html).

## Examples

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html) examples.

## Remarks

BOM tables may be sorted by up to three columns. This property maps one column to a sort order index. Call this property three times to set the sort order indexes of all three columns.

## See Also

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html)
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
