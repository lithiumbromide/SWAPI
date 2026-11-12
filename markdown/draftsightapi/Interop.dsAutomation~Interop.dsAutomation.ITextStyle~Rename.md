---
title: "Rename Method (ITextStyle)"
project: ""
interface: "ITextStyle"
member: "Rename"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITextStyle~Rename.html"
---

# Rename Method (ITextStyle)

Renames the TextStyle.

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

- `Name`: New name for the TextStyle

### Return Value

Status of renaming the TextStyle as defined in [dsCreateObjectResult_e](Interop.dsAutomation~Interop.dsAutomation.dsCreateObjectResult_e.html)

## See Also

[ITextStyle Interface](Interop.dsAutomation~Interop.dsAutomation.ITextStyle.html)
[ITextStyle Members](Interop.dsAutomation~Interop.dsAutomation.ITextStyle_members.html)
[ITextStyle::Name Property](Interop.dsAutomation~Interop.dsAutomation.ITextStyle~Name.html)

## Availability

DraftSight V1R1.1
