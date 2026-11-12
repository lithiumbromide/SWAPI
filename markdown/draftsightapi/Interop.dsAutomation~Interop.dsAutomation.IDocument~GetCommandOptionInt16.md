---
title: "GetCommandOptionInt16 Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetCommandOptionInt16"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt16.html"
---

# GetCommandOptionInt16 Method (IDocument)

Gets the 16-bit signed integer, also called Int16, value of the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub GetCommandOptionInt16( _
   ByVal Var As dsCommandOptionInt16_e, _
   ByRef Value As System.Integer, _
   ByRef Result As dsGetCommandOptionResult_e _
)
```

### C#

```csharp
void GetCommandOptionInt16(
   dsCommandOptionInt16_e Var,
   out System.int Value,
   out dsGetCommandOptionResult_e Result
)
```

### JScript

```
function GetCommandOptionInt16(
   Var : dsCommandOptionInt16_e,
   Value : System.int,
   Result : dsGetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void GetCommandOptionInt16(
   dsCommandOptionInt16_e Var,
   [PARAMFLAG::Out] System.int Value,
   [PARAMFLAG::Out] dsGetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void GetCommandOptionInt16(
   dsCommandOptionInt16_e Var,
   [Out] System.int Value,
   [Out] dsGetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionInt16_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt16_e.html)
- `Value`: Int16 value of the specified command option
- `Result`: Status of getting the Int16 value of the command option as defined in [dsGetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::SetCommandOptionInt16 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt16.html)
[IApplicationOptions::GetApplicationOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionInt16.html)
[IApplicationOptions::SetApplicationOptionInt16 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionInt16.html)

## Availability

DraftSight V1R1.1
