---
title: "ApplySavedSortScheme Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "ApplySavedSortScheme"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~ApplySavedSortScheme.html"
---

# ApplySavedSortScheme Method (IBomTableAnnotation)

Sorts this BOM table using the sort data that was previously saved in the table.

## Syntax

### Visual Basic (Declaration)

```vb
Function ApplySavedSortScheme( _
   ByVal SortData As BomTableSortData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim SortData As BomTableSortData
Dim value As System.Boolean

value = instance.ApplySavedSortScheme(SortData)
```

### C#

```csharp
System.bool ApplySavedSortScheme(
   BomTableSortData SortData
)
```

### C++/CLI

```cpp
System.bool ApplySavedSortScheme(
   BomTableSortData^ SortData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SortData`: [IBomTableSortData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableSortData.html)

### Return Value

True if BOM table is successfully sorted, false if not

## VBA Syntax

See [BomTableAnnotation::ApplySavedSortScheme](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~ApplySavedSortScheme.html).

## Examples

[Sort Table (VBA)](Sort_Table_Example_VB.htm)
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)
[Sort Table (C#)](Sort_Table_Example_CSharp.htm)

## Remarks

Before calling this method, you must:

1. Set [IBomTableSortData::SaveCurrentSortParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableSortData~SaveCurrentSortParameters.html) to true to indicate that the sort settings should be saved in the BOM table in the drawing.
2. [IBomTableAnnotation::Sort](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~Sort.html) to actually save the sort settings in the BOM table in the drawing.
3. [IBomTableAnnotation::GetBomTableSortData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetBomTableSortData.html) to populate SortData.

See [Sorting Tables](sldworksapiprogguide.chm::/OVERVIEW/Sorting_Tables.htm) for more information.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
