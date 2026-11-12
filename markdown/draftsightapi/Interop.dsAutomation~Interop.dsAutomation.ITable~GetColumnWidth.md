---
title: "GetColumnWidth Method (ITable)"
project: ""
interface: "ITable"
member: "GetColumnWidth"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~GetColumnWidth.html"
---

# GetColumnWidth Method (ITable)

Gets the width of the specified column in the Table.

## Syntax

### Visual Basic

```vb
Function GetColumnWidth( _
   ByVal Column As System.Integer _
) As System.Double
```

### C#

```csharp
System.double GetColumnWidth(
   System.int Column
)
```

### JScript

```
function GetColumnWidth(
   Column : System.int
) : System.double;
```

### Managed Extensions for C++

```
System.double GetColumnWidth(
   System.int Column
)
```

### C++/CLI

```cpp
System.double GetColumnWidth(
   System.int Column
)
```

### Parameters

- `Column`: Column for which to get its width

### Return Value

Width of Column

## Remarks

Before calling this method, call [ITable::TotalColumnCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalColumnCount.html) to get a valid value for Column.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetColumnWidth Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetColumnWidth.html)
[ITable::SetColumnWidthAt Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetColumnWidthAt.html)
[ITable::GetRowHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetRowHeight.html)
[ITable::SetRowHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetRowHeight.html)
[ITable::SetRowHeightAt Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetRowHeightAt.html)

## Availability

DraftSight V1R4.0
