---
title: "InsertColumn Method (ITable)"
project: ""
interface: "ITable"
member: "InsertColumn"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~InsertColumn.html"
---

# InsertColumn Method (ITable)

Inserts a column of the specified width at the specified index in the Table.

## Syntax

### Visual Basic

```vb
Function InsertColumn( _
   ByVal Index As System.Integer, _
   ByVal Width As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool InsertColumn(
   System.int Index,
   System.double Width
)
```

### JScript

```
function InsertColumn(
   Index : System.int,
   Width : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool InsertColumn(
   System.int Index,
   System.double Width
)
```

### C++/CLI

```cpp
System.bool InsertColumn(
   System.int Index,
   System.double Width
)
```

### Parameters

- `Index`: Index where to insert the column
- `Width`: Width of the column

### Return Value

True if the column is inserted in the Table, false if not

## Remarks

Before calling this method, call [ITable::TotalColumnCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalColumnCount.html) to determine a valid value for Index.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::DeleteColumn Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteColumn.html)
[ITable::DeleteRow Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteRow.html)
[ITable::InsertRow Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~InsertRow.html)

## Availability

DraftSight V1R4.0
