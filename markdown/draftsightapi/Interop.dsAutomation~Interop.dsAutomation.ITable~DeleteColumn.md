---
title: "DeleteColumn Method (ITable)"
project: ""
interface: "ITable"
member: "DeleteColumn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteColumn.html"
---

# DeleteColumn Method (ITable)

Deletes the column at the specified index from the Table.

## Syntax

### Visual Basic

```vb
Function DeleteColumn( _
   ByVal Index As System.Integer _
) As System.Boolean
```

### C#

```csharp
System.bool DeleteColumn(
   System.int Index
)
```

### JScript

```
function DeleteColumn(
   Index : System.int
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool DeleteColumn(
   System.int Index
)
```

### C++/CLI

```cpp
System.bool DeleteColumn(
   System.int Index
)
```

### Parameters

- `Index`: Index of the column to delete from the Table

### Return Value

True if the column is deleted, false if not

## Remarks

Before calling this method, call [ITable::TotalColumnCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalColumnCount.html) to get a valid value for Index.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::InsertColumn Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~InsertColumn.html)
[ITable::InsertRow Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~InsertRow.html)
[ITable::DeleteRow Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteRow.html)

## Availability

DraftSight V1R4.0
