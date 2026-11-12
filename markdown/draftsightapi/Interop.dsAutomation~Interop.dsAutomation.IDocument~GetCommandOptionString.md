---
title: "GetCommandOptionString Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetCommandOptionString"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionString.html"
---

# GetCommandOptionString Method (IDocument)

Gets the string value for the specified command option in the document.

## Syntax

### Visual Basic

```vb
Sub GetCommandOptionString( _
   ByVal Var As dsCommandOptionString_e, _
   ByRef Value As System.String, _
   ByRef Result As dsGetCommandOptionResult_e _
)
```

### C#

```csharp
void GetCommandOptionString(
   dsCommandOptionString_e Var,
   out System.string Value,
   out dsGetCommandOptionResult_e Result
)
```

### JScript

```
function GetCommandOptionString(
   Var : dsCommandOptionString_e,
   Value : System.String,
   Result : dsGetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void GetCommandOptionString(
   dsCommandOptionString_e Var,
   [PARAMFLAG::Out] System.string* Value,
   [PARAMFLAG::Out] dsGetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void GetCommandOptionString(
   dsCommandOptionString_e Var,
   [Out] System.String^ Value,
   [Out] dsGetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionString_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionString_e.html)
- `Value`: String value of the specified command option
- `Result`: Status of getting the string value of the command option as defined in [dsGetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::SetCommandOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionString.html)
[IApplicationOptions::GetApplicationOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~GetApplicationOptionString.html)
[IApplicationOptions::SetApplicationOptionString Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplicationOptions~SetApplicationOptionString.html)

## Availability

DraftSight V1R1.1
