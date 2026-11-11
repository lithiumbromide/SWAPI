---
title: "DeleteRow Method (ITable)"
project: ""
interface: "ITable"
member: "DeleteRow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteRow.html"
---

# DeleteRow Method (ITable)

Deletes the specified row from the Table.

## Syntax

### Visual Basic

```vb
Function DeleteRow( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool DeleteRow(
   System.int Index
)
```

### JScript

```
function DeleteRow(
   Index : System.int
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool DeleteRow(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool DeleteRow(
   System.int Index
)
```

### Parameters

- `Index`: Index of the row to delete from the Table

### Return Value

True if the row is deleted, false if not

## Remarks

Before calling this method, call [ITable::TotalRowCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalRowCount.html) to get a valid value for Index.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::InsertRow Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~InsertRow.html)
[ITable::DeleteColumn Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteColumn.html)
[ITable::InsertColumn Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~InsertColumn.html)

## Availability

DraftSight V1R4.0
