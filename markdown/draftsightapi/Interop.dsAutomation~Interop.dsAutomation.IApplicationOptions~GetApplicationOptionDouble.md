---
title: "GetApplicationOptionDouble Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "GetApplicationOptionDouble"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionDouble.html"
---

# GetApplicationOptionDouble Method (IApplicationOptions)

Gets the double value of the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function GetApplicationOptionDouble( _
   ByVal Var As dsApplicationOptionDouble_e, _
   ByRef Value As System.Double _
) As dsGetApplicationOptionResult_e
```

### C#

```csharp
dsGetApplicationOptionResult_e GetApplicationOptionDouble(
   dsApplicationOptionDouble_e Var,
   out System.double Value
)
```

### JScript

```
function GetApplicationOptionDouble(
   Var : dsApplicationOptionDouble_e,
   Value : System.double
) : dsGetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsGetApplicationOptionResult_e GetApplicationOptionDouble(
   dsApplicationOptionDouble_e Var,
   [PARAMFLAG::Out] System.double Value
)
```

### C++/CLI

```cpp
dsGetApplicationOptionResult_e GetApplicationOptionDouble(
   dsApplicationOptionDouble_e Var,
   [Out] System.double Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionDouble_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionDouble_e.html)
- `Value`: Double value of the specified command option

### Return Value

Status of getting the double value of the command option as defined in [dsGetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::SetApplicationOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionDouble.html)
[IDocument::GetCommandOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionDouble.html)
[IDocument::SetCommandOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionDouble.html)

## Availability

DraftSight V1R5.0
