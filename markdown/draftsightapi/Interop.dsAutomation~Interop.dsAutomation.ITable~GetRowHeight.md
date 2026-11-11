---
title: "GetRowHeight Method (ITable)"
project: ""
interface: "ITable"
member: "GetRowHeight"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetRowHeight.html"
---

# GetRowHeight Method (ITable)

Gets the height of the specified row in this Table.

## Syntax

### Visual Basic

```vb
Function GetRowHeight( _
   ByVal Row As System.Integer _
) As System.Double
```

### C#

```csharp
System.double GetRowHeight(
   System.int Row
)
```

### JScript

```
function GetRowHeight(
   Row : System.int
) : System.double;
```

### Managed Extensions for C++

```
System.double GetRowHeight(
   System.int Row
)
```

### C++/CLI

```cpp
System.double GetRowHeight(
   System.int Row
)
```

### Parameters

- `Row`: Row for which to get its height

### Return Value

Height of the row

## Remarks

Before calling this method, call [ITable::TotalRowCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalRowCount.html) to get a valid value for Row.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetRowHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetRowHeight.html)
[ITable::SetRowHeightAt Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetRowHeightAt.html)
[ITable::GetColumnWidth Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetColumnWidth.html)
[ITable::SetColumnWidth Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetColumnWidth.html)
[ITable::SetColumnWidthAt Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetColumnWidthAt.html)

## Availability

DraftSight V1R4.0
