---
title: "SetApplicationOptionInt32 Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "SetApplicationOptionInt32"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionInt32.html"
---

# SetApplicationOptionInt32 Method (IApplicationOptions)

Sets the 32-bit signed integer, also called Int32, value for the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function SetApplicationOptionInt32( _
   ByVal Var As dsApplicationOptionInt32_e, _
   ByVal Value As System.Integer _
) As dsSetApplicationOptionResult_e
```

### C#

```csharp
dsSetApplicationOptionResult_e SetApplicationOptionInt32(
   dsApplicationOptionInt32_e Var,
   System.int Value
)
```

### JScript

```
function SetApplicationOptionInt32(
   Var : dsApplicationOptionInt32_e,
   Value : System.int
) : dsSetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsSetApplicationOptionResult_e SetApplicationOptionInt32(
   dsApplicationOptionInt32_e Var,
   System.int Value
)
```

### C++/CLI

```cpp
dsSetApplicationOptionResult_e SetApplicationOptionInt32(
   dsApplicationOptionInt32_e Var,
   System.int Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionInt32_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt32_e.html)
- `Value`: Int32 value for the specified command option

### Return Value

Status of setting the Int32 value of the command option as defined in [dsSetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::GetApplicationOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionInt32.html)
[IDocument::SetCommandOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt32.html)
[IDocument::GetCommandOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt32.html)

## Availability

DraftSight V1R5.0
