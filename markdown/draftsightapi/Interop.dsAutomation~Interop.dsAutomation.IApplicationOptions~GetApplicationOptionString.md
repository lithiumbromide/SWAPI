---
title: "GetApplicationOptionString Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "GetApplicationOptionString"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionString.html"
---

# GetApplicationOptionString Method (IApplicationOptions)

Gets the string value for the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function GetApplicationOptionString( _
   ByVal Var As dsApplicationOptionString_e, _
   ByRef Value As System.String _
) As dsGetApplicationOptionResult_e
```

### C#

```csharp
dsGetApplicationOptionResult_e GetApplicationOptionString(
   dsApplicationOptionString_e Var,
   out System.string Value
)
```

### JScript

```
function GetApplicationOptionString(
   Var : dsApplicationOptionString_e,
   Value : System.String
) : dsGetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsGetApplicationOptionResult_e GetApplicationOptionString(
   dsApplicationOptionString_e Var,
   [PARAMFLAG::Out] System.string* Value
)
```

### C++/CLI

```cpp
dsGetApplicationOptionResult_e GetApplicationOptionString(
   dsApplicationOptionString_e Var,
   [Out] System.String^ Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionString_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionString_e.html)
- `Value`: String value of the specified command option

### Return Value

Status of getting the string value of the command option as defined in [dsGetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::SetApplicationOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionString.html)
[IDocument::GetCommandOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html)
[IDocument::SetCommandOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionString.html)

## Availability

DraftSight V1R5.0
