---
title: "Ascending Property (IBomTableSortData)"
project: "SOLIDWORKS API Help"
interface: "IBomTableSortData"
member: "Ascending"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~Ascending.html"
---

# Ascending Property (IBomTableSortData)

Gets and sets whether this is an ascending sort for the specified sort order index.

## Syntax

### Visual Basic (Declaration)

```vb
Property Ascending( _
   ByVal SortOrderIndex As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableSortData
Dim SortOrderIndex As System.Integer
Dim value As System.Boolean

instance.Ascending(SortOrderIndex) = value

value = instance.Ascending(SortOrderIndex)
```

### C#

```csharp
System.bool Ascending(
   System.int SortOrderIndex
) {get; set;}
```

### C++/CLI

```cpp
property System.bool Ascending {
   System.bool get(System.int SortOrderIndex);
   void set (System.int SortOrderIndex, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SortOrderIndex`: 0 for primary sort, 1 for secondary sort, 2 for tertiary sort (see **Remarks**)

### Property Value

True if sort is ascending, false if descending

## VBA Syntax

See [BomTableSortData::Ascending](ms-its:sldworksapivb6.chm::/sldworks~BomTableSortData~Ascending.html).

## Examples

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html) examples.

## Remarks

BOM tables may be sorted by up to three columns. This property maps the sort order index with a sorting direction (ascending or descending). Call this property three times to set the sorting directions of all three sort order indexes.

## See Also

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.html)
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
