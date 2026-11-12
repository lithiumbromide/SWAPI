---
title: "Rename Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "Rename"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~Rename.html"
---

# Rename Method (IDimensionStyle)

Renames the DimensionStyle.

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

- `Name`: New name for the DimensionStyle

### Return Value

Status of renaming the DimensionStyle as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)
[IDimensionStyle::Name Property](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~Name.html)

## Availability

DraftSight V1R1.1
