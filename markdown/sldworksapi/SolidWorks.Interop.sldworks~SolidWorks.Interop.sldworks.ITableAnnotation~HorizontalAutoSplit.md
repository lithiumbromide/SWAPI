---
title: "HorizontalAutoSplit Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "HorizontalAutoSplit"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit.html"
---

# HorizontalAutoSplit Method (ITableAnnotation)

Starts the automatic horizontal splitting of this table using the specified options.

## Syntax

### Visual Basic (Declaration)

```vb
Function HorizontalAutoSplit( _
   ByVal MaxNumberOfRows As System.Integer, _
   ByVal Apply As System.Integer, _
   ByVal PlacementOfNewSplitTables As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim MaxNumberOfRows As System.Integer
Dim Apply As System.Integer
Dim PlacementOfNewSplitTables As System.Integer
Dim value As System.Object

value = instance.HorizontalAutoSplit(MaxNumberOfRows, Apply, PlacementOfNewSplitTables)
```

### C#

```csharp
System.object HorizontalAutoSplit(
   System.int MaxNumberOfRows,
   System.int Apply,
   System.int PlacementOfNewSplitTables
)
```

### C++/CLI

```cpp
System.Object^ HorizontalAutoSplit(
   System.int MaxNumberOfRows,
   System.int Apply,
   System.int PlacementOfNewSplitTables
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MaxNumberOfRows`: Maximum number of rows in the split portions
- `Apply`: How often to horizontally split the table as defined in [swHorizontalAutoSplitApply_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHorizontalAutoSplitApply_e.html)
- `PlacementOfNewSplitTables`: Where to place the horizontally split table as defined in [swHorizontalAutoSplitPlacementOfSplitTable_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHorizontalAutoSplitPlacementOfSplitTable_e.html)

### Return Value

Array of split [ITableAnnotation](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation.html)s

## VBA Syntax

See [TableAnnotation::HorizontalAutoSplit](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~HorizontalAutoSplit.html).

## Remarks

This method horizontally splits:

- [Hole tables](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleTableAnnotation.html)
- [Bill of Materials tables](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableAnnotation.html)
- [General tables](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IGeneralTableAnnotation.html)

If Apply is set to [swHorizontalAutoSplitApply_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHorizontalAutoSplitApply_e.html).Continuously, in order to stop the automatic splitting of tables, you must set [ITableAnnotation::StopAutoSplitting](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ITableAnnotation~StopAutoSplitting.html) to true.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::Split Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.html)
[ITableAnnotation::GetSplitInformation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
