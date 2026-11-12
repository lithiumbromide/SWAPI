---
title: "GetCommandOptionBool Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetCommandOptionBool"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionBool.html"
---

# GetCommandOptionBool Method (IDocument)

Gets the Boolean value of the specified command option for the document.

## Syntax

### Visual Basic

```vb
Sub GetCommandOptionBool( _
   ByVal Var As dsCommandOptionBool_e, _
   ByRef Value As System.Boolean, _
   ByRef Result As dsGetCommandOptionResult_e _
)
```

### C#

```csharp
void GetCommandOptionBool(
   dsCommandOptionBool_e Var,
   out System.bool Value,
   out dsGetCommandOptionResult_e Result
)
```

### JScript

```
function GetCommandOptionBool(
   Var : dsCommandOptionBool_e,
   Value : System.boolean,
   Result : dsGetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void GetCommandOptionBool(
   dsCommandOptionBool_e Var,
   [PARAMFLAG::Out] System.bool Value,
   [PARAMFLAG::Out] dsGetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void GetCommandOptionBool(
   dsCommandOptionBool_e Var,
   [Out] System.bool Value,
   [Out] dsGetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionBool_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionBool_e.html)
- `Value`: Boolean value of the specified command option
- `Result`: Status of getting the Boolean value of the command option as defined in [dsGetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::SetCommandOptionBool Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionBool.html)
[IApplicationOptions::GetApplicationOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionBool.html)
[IApplicationOptions::SetApplicationOptionBool Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionBool.html)

## Availability

DraftSight V1R1.1
