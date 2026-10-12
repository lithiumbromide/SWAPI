---
title: "Sort Method (IBomTableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IBomTableAnnotation"
member: "Sort"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~Sort.html"
---

# Sort Method (IBomTableAnnotation)

Sorts this BOM table using the specified sorting data.

## Syntax

### Visual Basic (Declaration)

```vb
Function Sort( _
   ByVal SortData As BomTableSortData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomTableAnnotation
Dim SortData As BomTableSortData
Dim value As System.Boolean

value = instance.Sort(SortData)
```

### C#

```csharp
System.bool Sort(
   BomTableSortData SortData
)
```

### C++/CLI

```cpp
System.bool Sort(
   BomTableSortData^ SortData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SortData`: [IBomTableSortData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableSortData.html)

### Return Value

True if sorted successfully, false if not

## VBA Syntax

See [BomTableAnnotation::Sort](ms-its:sldworksapivb6.chm::/sldworks~BomTableAnnotation~Sort.html).

## Examples

[Sort Table (C#)](Sort_Table_Example_CSharp.htm)
[Sort Table (VB.NET)](Sort_Table_Example_VBNET.htm)
[Sort Table (VBA)](Sort_Table_Example_VB.htm)

## Remarks

Before calling this method, call [IBomTableAnnotation::GetBomTableSortData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation~GetBomTableSortData.html) to populate SortData.

See [Sorting Tables](sldworksapiprogguide.chm::/OVERVIEW/Sorting_Tables.htm) for more information.

## See Also

[IBomTableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation.html)
[IBomTableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html)
[IBomTableAnnotation::ApplySavedSortScheme Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation~ApplySavedSortScheme.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
