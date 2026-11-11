---
title: "SetCommandOptionDouble Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetCommandOptionDouble"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionDouble.html"
---

# SetCommandOptionDouble Method (IDocument)

Sets the double value for the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub SetCommandOptionDouble( _
   ByVal Var As dsCommandOptionDouble_e, _
   ByVal Value As System.Double, _
   ByRef Result As dsSetCommandOptionResult_e _
)
```

### C#

```csharp
void SetCommandOptionDouble(
   dsCommandOptionDouble_e Var,
   System.double Value,
   out dsSetCommandOptionResult_e Result
)
```

### JScript

```
function SetCommandOptionDouble(
   Var : dsCommandOptionDouble_e,
   Value : System.double,
   Result : dsSetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void SetCommandOptionDouble(
   dsCommandOptionDouble_e Var,
   System.double Value,
   [PARAMFLAG::Out] dsSetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void SetCommandOptionDouble(
   dsCommandOptionDouble_e Var,
   System.double Value,
   [Out] dsSetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionDouble_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionDouble_e.html)
- `Value`: Double value for the specified command option
- `Result`: Status of setting the double value of the command option as defined in [dsSetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)
[Fillet and Stretch Sketch Entities (JavaScript)](Fillet_and_Stretch_Sketch_Entities_Example_JS.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetCommandOptionDouble Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionDouble.html)
[IApplicationOptions::SetApplicationOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionDouble.html)
[IApplicationOptions::GetApplicationOptionDouble Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionDouble.html)

## Availability

DraftSight V1R1.1
