---
title: "GetCellRange Method (ISelectData)"
project: "SOLIDWORKS API Help"
interface: "ISelectData"
member: "GetCellRange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~GetCellRange.html"
---

# GetCellRange Method (ISelectData)

Gets the specified range of table cells for this selection.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetCellRange( _
   ByRef FirstRow As System.Integer, _
   ByRef LastRow As System.Integer, _
   ByRef FirstColumn As System.Integer, _
   ByRef LastColumn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISelectData
Dim FirstRow As System.Integer
Dim LastRow As System.Integer
Dim FirstColumn As System.Integer
Dim LastColumn As System.Integer

instance.GetCellRange(FirstRow, LastRow, FirstColumn, LastColumn)
```

### C#

```csharp
void GetCellRange(
   out System.int FirstRow,
   out System.int LastRow,
   out System.int FirstColumn,
   out System.int LastColumn
)
```

### C++/CLI

```cpp
void GetCellRange(
   [Out] System.int FirstRow,
   [Out] System.int LastRow,
   [Out] System.int FirstColumn,
   [Out] System.int LastColumn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FirstRow`: 0-based row number at the beginning of the selection range
- `LastRow`: 0-based row number at the end of the selection range
- `FirstColumn`: 0-based column number at the beginning of the selection range
- `LastColumn`: 0-based column number at the end of the selection range

### Return Value

## VBA Syntax

See [SelectData::GetCellRange](ms-its:sldworksapivb6.chm::/Sldworks~SelectData~GetCellRange.html).

## Remarks

The range of table cells are only used for a selection made in a table. For all other types of selections, these values are ignored.

By default, the value for FirstRow, LastRow, FirstColumn, and LastColumn is -1, which indicates that the entire table is selected.

## See Also

[ISelectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html)
[ISelectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html)
[ISelectData::SetCellRange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~SetCellRange.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
