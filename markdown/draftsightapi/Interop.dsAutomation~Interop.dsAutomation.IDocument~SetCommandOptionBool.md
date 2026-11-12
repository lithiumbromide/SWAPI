---
title: "SetCommandOptionBool Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetCommandOptionBool"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionBool.html"
---

# SetCommandOptionBool Method (IDocument)

Sets the Boolean value for the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub SetCommandOptionBool( _
   ByVal Var As dsCommandOptionBool_e, _
   ByVal Value As System.Boolean, _
   ByRef Result As dsSetCommandOptionResult_e _
)
```

### C#

```csharp
void SetCommandOptionBool(
   dsCommandOptionBool_e Var,
   System.bool Value,
   out dsSetCommandOptionResult_e Result
)
```

### JScript

```
function SetCommandOptionBool(
   Var : dsCommandOptionBool_e,
   Value : System.boolean,
   Result : dsSetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void SetCommandOptionBool(
   dsCommandOptionBool_e Var,
   System.bool Value,
   [PARAMFLAG::Out] dsSetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void SetCommandOptionBool(
   dsCommandOptionBool_e Var,
   System.bool Value,
   [Out] dsSetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionBool_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionBool_e.html)
- `Value`: Boolean value for the specified command option
- `Result`: Status of setting the Boolean value of the command option as defined in [dsSetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetCommandOptionBool Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionBool.html)
[IApplicationOptions::SetApplicationOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionBool.html)
[IApplicationOptions::GetApplicationOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionBool.html)

## Availability

DraftSight V1R1.1
