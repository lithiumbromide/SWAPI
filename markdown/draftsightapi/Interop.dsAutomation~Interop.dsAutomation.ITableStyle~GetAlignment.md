---
title: "GetAlignment Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "GetAlignment"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~GetAlignment.html"
---

# GetAlignment Method (ITableStyle)

Gets the justification and alignment of the text in the specified type of cell in this TableStyle.

## Syntax

### Visual Basic

```vb
Function GetAlignment( _
   ByVal CellType As dsTableCellType_e _
) As dsTableCellAlignment_e
```

### C#

```csharp
dsTableCellAlignment_e GetAlignment(
   dsTableCellType_e CellType
)
```

### JScript

```
function GetAlignment(
   CellType : dsTableCellType_e
) : dsTableCellAlignment_e;
```

### Managed Extensions for C++

```
dsTableCellAlignment_e GetAlignment(
   dsTableCellType_e CellType
)
```

### C++/CLI

```cpp
dsTableCellAlignment_e GetAlignment(
   dsTableCellType_e CellType
)
```

### Parameters

- `CellType`: Type of cell in the TableStyle as defined in [dsTableCellType_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellType_e.html)

### Return Value

Justification and alignment of the text in the specified type of cell in this TableStyle as defined in [dsTableCellAlignment_e](Interop.dsAutomation~Interop.dsAutomation.dsTableCellAlignment_e.html)

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::SetAlignment Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~SetAlignment.html)

## Availability

DraftSight V1R3.0
