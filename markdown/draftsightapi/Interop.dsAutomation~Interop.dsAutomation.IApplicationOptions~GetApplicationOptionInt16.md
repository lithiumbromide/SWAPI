---
title: "GetApplicationOptionInt16 Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "GetApplicationOptionInt16"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionInt16.html"
---

# GetApplicationOptionInt16 Method (IApplicationOptions)

Gets the 16-bit signed integer, also called Int16, value of the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function GetApplicationOptionInt16( _
   ByVal Var As dsApplicationOptionInt16_e, _
   ByRef Value As System.Integer _
) As dsGetApplicationOptionResult_e
```

### C#

```csharp
dsGetApplicationOptionResult_e GetApplicationOptionInt16(
   dsApplicationOptionInt16_e Var,
   out System.int Value
)
```

### JScript

```
function GetApplicationOptionInt16(
   Var : dsApplicationOptionInt16_e,
   Value : System.int
) : dsGetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsGetApplicationOptionResult_e GetApplicationOptionInt16(
   dsApplicationOptionInt16_e Var,
   [PARAMFLAG::Out] System.int Value
)
```

### C++/CLI

```cpp
dsGetApplicationOptionResult_e GetApplicationOptionInt16(
   dsApplicationOptionInt16_e Var,
   [Out] System.int Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionInt16_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt16_e.html)
- `Value`: Int16 value of the specified command option

### Return Value

Status of getting the Int16 value of the command option as defined in [dsGetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::SetApplicationOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionInt16.html)
[IDocument::GetCommandOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt16.html)
[IDocument::SetCommandOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt16.html)

## Availability

DraftSight V1R5.0
