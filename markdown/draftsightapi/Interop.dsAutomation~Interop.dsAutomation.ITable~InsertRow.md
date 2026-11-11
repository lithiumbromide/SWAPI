---
title: "InsertRow Method (ITable)"
project: ""
interface: "ITable"
member: "InsertRow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITable~InsertRow.html"
---

# InsertRow Method (ITable)

Inserts a row of the specified height at the specified index in the Table.

## Syntax

### Visual Basic

```vb
Function InsertRow( _
   ByVal Index As System.Integer, _
   ByVal Height As System.Double _
) As System.Boolean
```

### C#

```csharp
System.bool InsertRow(
   System.int Index,
   System.double Height
)
```

### JScript

```
function InsertRow(
   Index : System.int,
   Height : System.double
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool InsertRow(
   System.int Index,
   System.double Height
)
```

### C++/CLI

```cpp
System.bool InsertRow(
   System.int Index,
   System.double Height
)
```

### Parameters

- `Index`: Index where to insert the row
- `Height`: Height of the row

### Return Value

True if the row is inserted in the Table, false if not

## Remarks

Before calling this method, call [ITable::TotalRowCount](Interop.dsAutomation~Interop.dsAutomation.ITable~TotalRowCount.html) to determine a valid value for Index.

## See Also

[ITable Interface](Interop.dsAutomation~Interop.dsAutomation.ITable.html)
[ITable Members](Interop.dsAutomation~Interop.dsAutomation.ITable_members.html)
[ITable::DeleteRow Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteRow.html)
[ITable::DeleteColumn Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~DeleteColumn.html)
[ITable::InsertColumn Method ()](Interop.dsAutomation~Interop.dsAutomation.ITable~InsertColumn.html)

## Availability

DraftSight V1R4.0
