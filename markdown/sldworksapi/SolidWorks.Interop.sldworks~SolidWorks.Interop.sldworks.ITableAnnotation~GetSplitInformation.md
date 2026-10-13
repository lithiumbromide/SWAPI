---
title: "GetSplitInformation Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetSplitInformation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetSplitInformation.html"
---

# GetSplitInformation Method (ITableAnnotation)

Gets information about any splits in this table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplitInformation( _
   ByRef Index As System.Integer, _
   ByRef Count As System.Integer, _
   ByRef RangeStart As System.Integer, _
   ByRef RangeEnd As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim Count As System.Integer
Dim RangeStart As System.Integer
Dim RangeEnd As System.Integer
Dim value As System.Integer

value = instance.GetSplitInformation(Index, Count, RangeStart, RangeEnd)
```

### C#

```csharp
System.int GetSplitInformation(
   out System.int Index,
   out System.int Count,
   out System.int RangeStart,
   out System.int RangeEnd
)
```

### C++/CLI

```cpp
System.int GetSplitInformation(
   [Out] System.int Index,
   [Out] System.int Count,
   [Out] System.int RangeStart,
   [Out] System.int RangeEnd
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Piece of the table that this is
- `Count`: Piece of the table that this is
- `RangeStart`: Beginning row for this piece of the table
- `RangeEnd`: Ending row for this piece of the table

### Return Value

Direction in which the table was split as defined by [swTableSplitDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTableSplitDirection_e.html)

## VBA Syntax

See [TableAnnotation::GetSplitInformation](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetSplitInformation.html).

## Examples

[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)
[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)

## Remarks

A table split is a table divided into multiple tables, also called pieces.

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::Split Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~Split.html)
[ITableAnnotation::HorizontalAutoSplit Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~HorizontalAutoSplit.html)
[ITableAnnotation::StopAutoSplitting Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~StopAutoSplitting.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
