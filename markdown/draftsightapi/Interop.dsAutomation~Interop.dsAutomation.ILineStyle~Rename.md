---
title: "Rename Method (ILineStyle)"
project: ""
interface: "ILineStyle"
member: "Rename"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILineStyle~Rename.html"
---

# Rename Method (ILineStyle)

Renames the simple LineStyle.

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

- `Name`: New name for the simple LineStyle

### Return Value

Result as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[ILineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html)
[ILineStyle Members](Interop.dsAutomation~Interop.dsAutomation.ILineStyle_members.html)
[ILineStyle::Name Property ()](Interop.dsAutomation~Interop.dsAutomation.ILineStyle~Name.html)

## Availability

DraftSight V1R4.0
