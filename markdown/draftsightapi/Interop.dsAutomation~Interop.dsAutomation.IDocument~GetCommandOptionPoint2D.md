---
title: "GetCommandOptionPoint2D Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetCommandOptionPoint2D"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionPoint2D.html"
---

# GetCommandOptionPoint2D Method (IDocument)

Gets the 2D point's coordinates for the specified command option in the document.

## Syntax

### Visual Basic

```vb
Sub GetCommandOptionPoint2D( _
   ByVal Var As dsCommandOptionPoint2d_e, _
   ByRef X As System.Double, _
   ByRef Y As System.Double, _
   ByRef Result As dsGetCommandOptionResult_e _
)
```

### C#

```csharp
void GetCommandOptionPoint2D(
   dsCommandOptionPoint2d_e Var,
   out System.double X,
   out System.double Y,
   out dsGetCommandOptionResult_e Result
)
```

### JScript

```
function GetCommandOptionPoint2D(
   Var : dsCommandOptionPoint2d_e,
   X : System.double,
   Y : System.double,
   Result : dsGetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void GetCommandOptionPoint2D(
   dsCommandOptionPoint2d_e Var,
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y,
   [PARAMFLAG::Out] dsGetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void GetCommandOptionPoint2D(
   dsCommandOptionPoint2d_e Var,
   [Out] System.double X,
   [Out] System.double Y,
   [Out] dsGetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionPoint2d_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionPoint2d_e.html)
- `X`: x coordinate of the 2D point
- `Y`: y coordinate of the 2D point
- `Result`: Status of getting the 2D point's coordinates for the command option as defined in [dsGetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsGetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::SetCommandOptionPoint2D Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionPoint2D.html)

## Availability

DraftSight V1R1.1
