---
title: "Split Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "Split"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.html"
---

# Split Method (ITableAnnotation)

Splits the table at the specified location.

## Syntax

### Visual Basic (Declaration)

```vb
Function Split( _
   ByVal Where As System.Integer, _
   ByVal Index As System.Integer _
) As TableAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Where As System.Integer
Dim Index As System.Integer
Dim value As TableAnnotation

value = instance.Split(Where, Index)
```

### C#

```csharp
TableAnnotation Split(
   System.int Where,
   System.int Index
)
```

### C++/CLI

```cpp
TableAnnotation^ Split(
   System.int Where,
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Where`: Where to split the table as defined in [swTableSplitLocations_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableSplitLocations_e.html)
- `Index`: Index of the row or column as specified in Where to split the table (see **Remarks**)

### Return Value

Newly created [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html) object

## VBA Syntax

See [TableAnnotation::Split](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~Split.html).

## Remarks

The index for both rows and columns is 0-based.

The indexes for the rows and columns always correspond to the rows and columns of the table from which the split table originates.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::Merge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Merge.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::UnmergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.html)
[ITableAnnotation::GetSplitInformation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.html)
[ITableAnnotation::HorizontalAutoSplit Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit.html)
[ITableAnnotation::StopAutoSplitting Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~StopAutoSplitting.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
