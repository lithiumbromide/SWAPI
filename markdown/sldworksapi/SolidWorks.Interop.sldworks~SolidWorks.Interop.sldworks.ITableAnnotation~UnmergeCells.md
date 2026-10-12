---
title: "UnmergeCells Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "UnmergeCells"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~UnmergeCells.html"
---

# UnmergeCells Method (ITableAnnotation)

Splits the specified previously merged cell in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function UnmergeCells( _
   ByVal Row As System.Integer, _
   ByVal Column As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Row As System.Integer
Dim Column As System.Integer
Dim value As System.Boolean

value = instance.UnmergeCells(Row, Column)
```

### C#

```csharp
System.bool UnmergeCells(
   System.int Row,
   System.int Column
)
```

### C++/CLI

```cpp
System.bool UnmergeCells(
   System.int Row,
   System.int Column
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Row`: Index of the row of the cell
- `Column`: Index of the column of the cell

### Return Value

True if the cell splits successfully, false if not

## VBA Syntax

See [TableAnnotation::UnmergeCells](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~UnmergeCells.html).

## Remarks

Index for both rows and columns is 0-based.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::GetSplitInformation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.html)
[ITableAnnotation::IsCellMerged Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~IsCellMerged.html)
[ITableAnnotation::Merge Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Merge.html)
[ITableAnnotation::MergeCells Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~MergeCells.html)
[ITableAnnotation::Split Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
