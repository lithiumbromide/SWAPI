---
title: "SetApplicationOptionBool Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "SetApplicationOptionBool"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionBool.html"
---

# SetApplicationOptionBool Method (IApplicationOptions)

Sets the Boolean value for the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function SetApplicationOptionBool( _
   ByVal Var As dsApplicationOptionBool_e, _
   ByVal Value As System.Boolean _
) As dsSetApplicationOptionResult_e
```

### C#

```csharp
dsSetApplicationOptionResult_e SetApplicationOptionBool(
   dsApplicationOptionBool_e Var,
   System.bool Value
)
```

### JScript

```
function SetApplicationOptionBool(
   Var : dsApplicationOptionBool_e,
   Value : System.boolean
) : dsSetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsSetApplicationOptionResult_e SetApplicationOptionBool(
   dsApplicationOptionBool_e Var,
   System.bool Value
)
```

### C++/CLI

```cpp
dsSetApplicationOptionResult_e SetApplicationOptionBool(
   dsApplicationOptionBool_e Var,
   System.bool Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionBool_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionBool_e.html)
- `Value`: Boolean value for the specified command option

### Return Value

Status of setting the Boolean value of the command option as defined in [dsSetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::GetApplicationOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionBool.html)
[IDocument::SetCommandOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionBool.html)
[IDocument::GetCommandOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionBool.html)

## Availability

DraftSight V1R5.0
