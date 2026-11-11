---
title: "SetRowHeightAt Method (ITable)"
project: ""
interface: "ITable"
member: "SetRowHeightAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetRowHeightAt.html"
---

# SetRowHeightAt Method (ITable)

Sets the height of the specified row in the Table.

## Syntax

### Visual Basic

```vb
Sub SetRowHeightAt( _
   ByVal Row As System.Integer, _
   ByVal Height As System.Double _
)
```

### C#

```csharp
void SetRowHeightAt(
   System.int Row,
   System.double Height
)
```

### JScript

```
function SetRowHeightAt(
   Row : System.int,
   Height : System.double
);
```

### Managed Extensions for C++

```
void SetRowHeightAt(
   System.int Row,
   System.double Height
)
```

### C++/CLI

```cpp
void SetRowHeightAt(
   System.int Row,
   System.double Height
)
```

### Parameters

- `Row`: Row whose height to set
- `Height`: Height for Row

## Remarks

Before calling this method, call [ITable::TotalRowCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalRowCount.html) to get a valid value for Row.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetRowHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetRowHeight.html)
[ITable::GetRowHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetRowHeight.html)
[ITable::GetColumnWidth Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetColumnWidth.html)
[ITable::SetColumnWidth Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetColumnWidth.html)
[ITable::SetColumnWidthAt Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetColumnWidthAt.html)

## Availability

DraftSight V1R4.0
