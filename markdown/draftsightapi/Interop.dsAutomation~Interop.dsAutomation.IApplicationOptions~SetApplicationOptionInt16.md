---
title: "SetApplicationOptionInt16 Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "SetApplicationOptionInt16"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionInt16.html"
---

# SetApplicationOptionInt16 Method (IApplicationOptions)

Sets the 16-bit signed integer, also called Int16, value for the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function SetApplicationOptionInt16( _
   ByVal Var As dsApplicationOptionInt16_e, _
   ByVal Value As System.Integer _
) As dsSetApplicationOptionResult_e
```

### C#

```csharp
dsSetApplicationOptionResult_e SetApplicationOptionInt16(
   dsApplicationOptionInt16_e Var,
   System.int Value
)
```

### JScript

```
function SetApplicationOptionInt16(
   Var : dsApplicationOptionInt16_e,
   Value : System.int
) : dsSetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsSetApplicationOptionResult_e SetApplicationOptionInt16(
   dsApplicationOptionInt16_e Var,
   System.int Value
)
```

### C++/CLI

```cpp
dsSetApplicationOptionResult_e SetApplicationOptionInt16(
   dsApplicationOptionInt16_e Var,
   System.int Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionInt16_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionInt16_e.html)
- `Value`: Int16 value for the specified command option

### Return Value

Status of setting the Int16 value of the command option as defined in [dsSetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::GetApplicationOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionInt16.html)
[IDocument::SetCommandOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt16.html)
[IDocument::GetCommandOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt16.html)

## Availability

DraftSight V1R5.0
