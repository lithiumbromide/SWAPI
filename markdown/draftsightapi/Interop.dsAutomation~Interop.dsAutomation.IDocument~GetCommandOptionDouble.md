---
title: "GetCommandOptionDouble Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetCommandOptionDouble"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionDouble.html"
---

# GetCommandOptionDouble Method (IDocument)

Gets the double value of the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub GetCommandOptionDouble( _
   ByVal Var As dsCommandOptionDouble_e, _
   ByRef Value As System.Double, _
   ByRef Result As dsGetCommandOptionResult_e _
)
```

### C#

```csharp
void GetCommandOptionDouble(
   dsCommandOptionDouble_e Var,
   out System.double Value,
   out dsGetCommandOptionResult_e Result
)
```

### JScript

```
function GetCommandOptionDouble(
   Var : dsCommandOptionDouble_e,
   Value : System.double,
   Result : dsGetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void GetCommandOptionDouble(
   dsCommandOptionDouble_e Var,
   [PARAMFLAG::Out] System.double Value,
   [PARAMFLAG::Out] dsGetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void GetCommandOptionDouble(
   dsCommandOptionDouble_e Var,
   [Out] System.double Value,
   [Out] dsGetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionDouble_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionDouble_e.html)
- `Value`: Double value of the specified command option
- `Result`: Status of getting the double value of the command option as defined in [dsGetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::SetCommandOptionDouble Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionDouble.html)
[IApplicationOptions::GetApplicationOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionDouble.html)
[IApplicationOptions::SetApplicationOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionDouble.html)

## Availability

DraftSight V1R1.1
