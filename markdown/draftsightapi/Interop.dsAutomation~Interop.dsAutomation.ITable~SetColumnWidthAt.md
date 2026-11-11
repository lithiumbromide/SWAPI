---
title: "SetColumnWidthAt Method (ITable)"
project: ""
interface: "ITable"
member: "SetColumnWidthAt"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~SetColumnWidthAt.html"
---

# SetColumnWidthAt Method (ITable)

Sets the width of the specified column in the Table.

## Syntax

### Visual Basic

```vb
Sub SetColumnWidthAt( _
   ByVal Column As System.Integer, _
   ByVal Width As System.Double _
)
```

### C#

```csharp
void SetColumnWidthAt(
   System.int Column,
   System.double Width
)
```

### JScript

```
function SetColumnWidthAt(
   Column : System.int,
   Width : System.double
);
```

### Managed Extensions for C++

```
void SetColumnWidthAt(
   System.int Column,
   System.double Width
)
```

### C++/CLI

```cpp
void SetColumnWidthAt(
   System.int Column,
   System.double Width
)
```

### Parameters

- `Column`: Column whose width to set
- `Width`: Width for column

## Remarks

Before calling this method, call [ITable::TotalColumnCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalColumnCount.html) to get a valid value for Column.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::SetColumnWidth Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetColumnWidth.html)
[ITable::GetColumnWidth Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetColumnWidth.html)
[ITable::SetRowHeightAt Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetRowHeightAt.html)
[ITable::SetRowHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~SetRowHeight.html)
[ITable::GetRowHeight Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~GetRowHeight.html)

## Availability

DraftSight V1R4.0
