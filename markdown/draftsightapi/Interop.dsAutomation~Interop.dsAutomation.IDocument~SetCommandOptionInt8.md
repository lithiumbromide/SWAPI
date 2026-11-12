---
title: "SetCommandOptionInt8 Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetCommandOptionInt8"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt8.html"
---

# SetCommandOptionInt8 Method (IDocument)

Sets the 8-bit signed integer, also called Int8, value for the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub SetCommandOptionInt8( _
   ByVal Var As dsCommandOptionInt8_e, _
   ByVal Value As System.Integer, _
   ByRef Result As dsSetCommandOptionResult_e _
)
```

### C#

```csharp
void SetCommandOptionInt8(
   dsCommandOptionInt8_e Var,
   System.int Value,
   out dsSetCommandOptionResult_e Result
)
```

### JScript

```
function SetCommandOptionInt8(
   Var : dsCommandOptionInt8_e,
   Value : System.int,
   Result : dsSetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void SetCommandOptionInt8(
   dsCommandOptionInt8_e Var,
   System.int Value,
   [PARAMFLAG::Out] dsSetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void SetCommandOptionInt8(
   dsCommandOptionInt8_e Var,
   System.int Value,
   [Out] dsSetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionInt8_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt8_e.html)
- `Value`: Int8 value for the specified command option
- `Result`: Status of setting the Int8 value of the command option as defined in [dsSetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetCommandOptionInt8 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt8.html)

## Availability

DraftSight V1R1.1
