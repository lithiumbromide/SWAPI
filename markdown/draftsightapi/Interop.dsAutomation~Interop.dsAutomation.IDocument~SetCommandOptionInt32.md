---
title: "SetCommandOptionInt32 Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetCommandOptionInt32"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt32.html"
---

# SetCommandOptionInt32 Method (IDocument)

Sets the 32-bit signed integer, also called Int32, value for the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub SetCommandOptionInt32( _
   ByVal Var As dsCommandOptionInt32_e, _
   ByVal Value As System.Integer, _
   ByRef Result As dsSetCommandOptionResult_e _
)
```

### C#

```csharp
void SetCommandOptionInt32(
   dsCommandOptionInt32_e Var,
   System.int Value,
   out dsSetCommandOptionResult_e Result
)
```

### JScript

```
function SetCommandOptionInt32(
   Var : dsCommandOptionInt32_e,
   Value : System.int,
   Result : dsSetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void SetCommandOptionInt32(
   dsCommandOptionInt32_e Var,
   System.int Value,
   [PARAMFLAG::Out] dsSetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void SetCommandOptionInt32(
   dsCommandOptionInt32_e Var,
   System.int Value,
   [Out] dsSetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionInt32_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt32_e.html)
- `Value`: Int32 value for the specified command option
- `Result`: Status of setting the Int32 value of the command option as defined in [dsSetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetCommandOptionInt32 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt32.html)
[IApplicationOptions::SetApplicationOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionInt32.html)
[IApplicationOptions::GetApplicationOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionInt32.html)

## Availability

DraftSight V1R1.1
