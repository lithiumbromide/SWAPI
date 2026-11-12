---
title: "GetApplicationOptionInt32 Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "GetApplicationOptionInt32"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionInt32.html"
---

# GetApplicationOptionInt32 Method (IApplicationOptions)

Gets the 32-bit signed integer, also called Int32, value of the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function GetApplicationOptionInt32( _
   ByVal Var As dsApplicationOptionInt32_e, _
   ByRef Value As System.Integer _
) As dsGetApplicationOptionResult_e
```

### C#

```csharp
dsGetApplicationOptionResult_e GetApplicationOptionInt32(
   dsApplicationOptionInt32_e Var,
   out System.int Value
)
```

### JScript

```
function GetApplicationOptionInt32(
   Var : dsApplicationOptionInt32_e,
   Value : System.int
) : dsGetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsGetApplicationOptionResult_e GetApplicationOptionInt32(
   dsApplicationOptionInt32_e Var,
   [PARAMFLAG::Out] System.int Value
)
```

### C++/CLI

```cpp
dsGetApplicationOptionResult_e GetApplicationOptionInt32(
   dsApplicationOptionInt32_e Var,
   [Out] System.int Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionInt32_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt32_e.html)
- `Value`: Int32 value of the specified command option

### Return Value

Status of getting the Int32 value of the command option as defined in [dsGetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::SetApplicationOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionInt32.html)
[IDocument::GetCommandOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt32.html)
[IDocument::SetCommandOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt32.html)

## Availability

DraftSight V1R5.0
