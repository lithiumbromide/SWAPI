---
title: "SetCommandOptionString Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetCommandOptionString"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionString.html"
---

# SetCommandOptionString Method (IDocument)

Sets the string value for the specified command option in the document.

## Syntax

### Visual Basic

```vb
Sub SetCommandOptionString( _
   ByVal Var As dsCommandOptionString_e, _
   ByVal Value As System.String, _
   ByRef Result As dsSetCommandOptionResult_e _
)
```

### C#

```csharp
void SetCommandOptionString(
   dsCommandOptionString_e Var,
   System.string Value,
   out dsSetCommandOptionResult_e Result
)
```

### JScript

```
function SetCommandOptionString(
   Var : dsCommandOptionString_e,
   Value : System.String,
   Result : dsSetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void SetCommandOptionString(
   dsCommandOptionString_e Var,
   System.string* Value,
   [PARAMFLAG::Out] dsSetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void SetCommandOptionString(
   dsCommandOptionString_e Var,
   System.String^ Value,
   [Out] dsSetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionString_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionString_e.html)
- `Value`: String value for the specified command option
- `Result`: Status of setting the string value of the command option as defined in [dsSetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetCommandOptionString Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html)
[IApplicationOptions::SetApplicationOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionString.html)
[IApplicationOptions::GetApplicationOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionString.html)

## Availability

DraftSight V1R1.1
