---
title: "SetApplicationOptionDouble Method (IApplicationOptions)"
project: ""
interface: "IApplicationOptions"
member: "SetApplicationOptionDouble"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionDouble.html"
---

# SetApplicationOptionDouble Method (IApplicationOptions)

Sets the double value for the specified command option for DraftSight.

## Syntax

### Visual Basic

```vb
Function SetApplicationOptionDouble( _
   ByVal Var As dsApplicationOptionDouble_e, _
   ByVal Value As System.Double _
) As dsSetApplicationOptionResult_e
```

### C#

```csharp
dsSetApplicationOptionResult_e SetApplicationOptionDouble(
   dsApplicationOptionDouble_e Var,
   System.double Value
)
```

### JScript

```
function SetApplicationOptionDouble(
   Var : dsApplicationOptionDouble_e,
   Value : System.double
) : dsSetApplicationOptionResult_e;
```

### Managed Extensions for C++

```
dsSetApplicationOptionResult_e SetApplicationOptionDouble(
   dsApplicationOptionDouble_e Var,
   System.double Value
)
```

### C++/CLI

```cpp
dsSetApplicationOptionResult_e SetApplicationOptionDouble(
   dsApplicationOptionDouble_e Var,
   System.double Value
)
```

### Parameters

- `Var`: Command option as defined in [dsApplicationOptionDouble_e](Interop.dsAutomation~Interop.dsAutomation.dsApplicationOptionDouble_e.html)
- `Value`: Double value for the specified command option

### Return Value

Status of setting the double value of the command option as defined in [dsSetApplicationOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetApplicationOptionResult_e.html)

## See Also

[IApplicationOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions.html)
[IApplicationOptions Members](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions_members.html)
[IApplicationOptions::GetApplicationOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionDouble.html)
[IDocument::SetCommandOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionDouble.html)
[IDocument::GetCommandOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionDouble.html)

## Availability

DraftSight V1R5.0
