---
title: "GetCommandOptionInt32 Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetCommandOptionInt32"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionInt32.html"
---

# GetCommandOptionInt32 Method (IDocument)

Gets the 32-bit signed integer, also called Int32, value of the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub GetCommandOptionInt32( _
   ByVal Var As dsCommandOptionInt32_e, _
   ByRef Value As System.Integer, _
   ByRef Result As dsGetCommandOptionResult_e _
)
```

### C#

```csharp
void GetCommandOptionInt32(
   dsCommandOptionInt32_e Var,
   out System.int Value,
   out dsGetCommandOptionResult_e Result
)
```

### JScript

```
function GetCommandOptionInt32(
   Var : dsCommandOptionInt32_e,
   Value : System.int,
   Result : dsGetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void GetCommandOptionInt32(
   dsCommandOptionInt32_e Var,
   [PARAMFLAG::Out] System.int Value,
   [PARAMFLAG::Out] dsGetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void GetCommandOptionInt32(
   dsCommandOptionInt32_e Var,
   [Out] System.int Value,
   [Out] dsGetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionInt32_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionInt32_e.html)
- `Value`: Int32 value of the specified command option
- `Result`: Status of getting the Int32 value of the command option as defined in [dsGetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::SetCommandOptionInt32 Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionInt32.html)
[IApplicationOptions::GetApplicationOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionInt32.html)
[IApplicationOptions::SetApplicationOptionInt32 Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionInt32.html)

## Availability

DraftSight V1R1.1
