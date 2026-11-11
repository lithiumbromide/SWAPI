---
title: "SetCommandOptionInt16 Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetCommandOptionInt16"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt16.html"
---

# SetCommandOptionInt16 Method (IDocument)

Sets the 16-bit signed integer, also called Int16, value for the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub SetCommandOptionInt16( _
   ByVal Var As dsCommandOptionInt16_e, _
   ByVal Value As System.Integer, _
   ByRef Result As dsSetCommandOptionResult_e _
)
```

### C#

```csharp
void SetCommandOptionInt16(
   dsCommandOptionInt16_e Var,
   System.int Value,
   out dsSetCommandOptionResult_e Result
)
```

### JScript

```
function SetCommandOptionInt16(
   Var : dsCommandOptionInt16_e,
   Value : System.int,
   Result : dsSetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void SetCommandOptionInt16(
   dsCommandOptionInt16_e Var,
   System.int Value,
   [PARAMFLAG::Out] dsSetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void SetCommandOptionInt16(
   dsCommandOptionInt16_e Var,
   System.int Value,
   [Out] dsSetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionInt16_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt16_e.html)
- `Value`: Int16 value for the specified command option
- `Result`: Status of setting the Int16 value of the command option as defined in [dsSetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetCommandOptionInt16 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt16.html)
[IApplicationOptions::SetApplicationOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionInt16.html)
[IApplicationOptions::GetApplicationOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionInt16.html)

## Availability

DraftSight V1R1.1
