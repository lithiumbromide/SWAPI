---
title: "Rename Method (ITableStyle)"
project: ""
interface: "ITableStyle"
member: "Rename"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyle~Rename.html"
---

# Rename Method (ITableStyle)

Renames the TableStyle to the specified name.

## Syntax

### Visual Basic

```vb
Function Rename( _
   ByVal Name As System.String _
) As dsCreateObjectResult_e
```

### C#

```csharp
dsCreateObjectResult_e Rename(
   System.string Name
)
```

### JScript

```
function Rename(
   Name : System.String
) : dsCreateObjectResult_e;
```

### Managed Extensions for C++

```
dsCreateObjectResult_e Rename(
   System.string* Name
)
```

### C++/CLI

```cpp
dsCreateObjectResult_e Rename(
   System.String^ Name
)
```

### Parameters

- `Name`: New name for TableStyle

### Return Value

Status of renaming the TableStyle as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[ITableStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)
[ITableStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyle_members.html)
[ITableStyle::Name Property](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~Name.html)

## Availability

DraftSight V1R3.0
