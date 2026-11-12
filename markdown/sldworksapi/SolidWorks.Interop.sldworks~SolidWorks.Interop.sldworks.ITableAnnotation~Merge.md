---
title: "Merge Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "Merge"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Merge.html"
---

# Merge Method (ITableAnnotation)

Merges the display of this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function Merge( _
   ByVal Where As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim value As System.Boolean

value = instance.Merge(Where)
```

### C#

```csharp
System.bool Merge(
   System.int Where
)
```

### C++/CLI

```cpp
System.bool Merge(
   System.int Where
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Where`: Merge the display of this table as defined in [swTableMergeLocations_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableMergeLocations_e.html)

### Return Value

True if the merge is successful, false if not

## VBA Syntax

See [TableAnnotation::Merge](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~Merge.html).

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::GetSplitInformation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.html)
[ITableAnnotation::Split Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.html)
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
