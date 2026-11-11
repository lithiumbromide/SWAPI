---
title: "GetApplicationOptionBool Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "GetApplicationOptionBool"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionBool.html"
---

# GetApplicationOptionBool Method (IApplicationOptions)

Gets the Boolean value of the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function GetApplicationOptionBool( _
   ByVal Var As dsApplicationOptionBool_e, _
   ByRef Value As System.Boolean _
) As dsGetApplicationOptionResult_e
```

### C#

```csharp
dsGetApplicationOptionResult_e GetApplicationOptionBool(
   dsApplicationOptionBool_e Var,
   out System.bool Value
)
```

### JScript

```
function GetApplicationOptionBool(
   Var : dsApplicationOptionBool_e,
   Value : System.boolean
) : dsGetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsGetApplicationOptionResult_e GetApplicationOptionBool(
   dsApplicationOptionBool_e Var,
   [PARAMFLAG::Out] System.bool Value
)
```

### C++/CLI

```cpp
dsGetApplicationOptionResult_e GetApplicationOptionBool(
   dsApplicationOptionBool_e Var,
   [Out] System.bool Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionBool_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionBool_e.html)
- `Value`: Boolean value of the specified command option

### Return Value

Status of getting the Boolean value of the command option as defined in [dsGetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::SetApplicationOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionBool.html)
[IDocument::GetCommandOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionBool.html)
[IDocument::SetCommandOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionBool.html)

## Availability

DraftSight V1R5.0
