---
title: "SetApplicationOptionString Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "SetApplicationOptionString"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionString.html"
---

# SetApplicationOptionString Method (IApplicationOptions)

Sets the string value for the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function SetApplicationOptionString( _
   ByVal Var As dsApplicationOptionString_e, _
   ByVal Value As System.String _
) As dsSetApplicationOptionResult_e
```

### C#

```csharp
dsSetApplicationOptionResult_e SetApplicationOptionString(
   dsApplicationOptionString_e Var,
   System.string Value
)
```

### JScript

```
function SetApplicationOptionString(
   Var : dsApplicationOptionString_e,
   Value : System.String
) : dsSetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsSetApplicationOptionResult_e SetApplicationOptionString(
   dsApplicationOptionString_e Var,
   System.string* Value
)
```

### C++/CLI

```cpp
dsSetApplicationOptionResult_e SetApplicationOptionString(
   dsApplicationOptionString_e Var,
   System.String^ Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionString_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionString_e.html)
- `Value`: String value for the specified command option

### Return Value

Status of setting the string value of the command option as defined in [dsSetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionString_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::GetApplicationOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionString.html)
[IDocument::SetCommandOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionString.html)
[IDocument::GetCommandOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html)

## Availability

DraftSight V1R5.0
