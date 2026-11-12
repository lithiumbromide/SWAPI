---
title: "GetCommandOptionInt8 Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetCommandOptionInt8"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt8.html"
---

# GetCommandOptionInt8 Method (IDocument)

Gets the 8-bit signed integer, also called Int8, value of the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub GetCommandOptionInt8( _
   ByVal Var As dsCommandOptionInt8_e, _
   ByRef Value As System.Integer, _
   ByRef Result As dsGetCommandOptionResult_e _
)
```

### C#

```csharp
void GetCommandOptionInt8(
   dsCommandOptionInt8_e Var,
   out System.int Value,
   out dsGetCommandOptionResult_e Result
)
```

### JScript

```
function GetCommandOptionInt8(
   Var : dsCommandOptionInt8_e,
   Value : System.int,
   Result : dsGetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void GetCommandOptionInt8(
   dsCommandOptionInt8_e Var,
   [PARAMFLAG::Out] System.int Value,
   [PARAMFLAG::Out] dsGetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void GetCommandOptionInt8(
   dsCommandOptionInt8_e Var,
   [Out] System.int Value,
   [Out] dsGetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionInt8_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt8_e.html)
- `Value`: Int8 value of the specified command option
- `Result`: Status of getting the Int8 value of the command option as defined in [dsGetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::SetCommandOptionInt8 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt8.html)

## Availability

DraftSight V1R1.1
