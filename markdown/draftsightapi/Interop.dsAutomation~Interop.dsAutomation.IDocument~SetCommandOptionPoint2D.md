---
title: "SetCommandOptionPoint2D Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetCommandOptionPoint2D"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionPoint2D.html"
---

# SetCommandOptionPoint2D Method (IDocument)

Sets the command option for the specified 2D point in the document.

## Syntax

### Visual Basic

```vb
Sub SetCommandOptionPoint2D( _
   ByVal Var As dsCommandOptionPoint2d_e, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByRef Result As dsSetCommandOptionResult_e _
)
```

### C#

```csharp
void SetCommandOptionPoint2D(
   dsCommandOptionPoint2d_e Var,
   System.double X,
   System.double Y,
   out dsSetCommandOptionResult_e Result
)
```

### JScript

```
function SetCommandOptionPoint2D(
   Var : dsCommandOptionPoint2d_e,
   X : System.double,
   Y : System.double,
   Result : dsSetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void SetCommandOptionPoint2D(
   dsCommandOptionPoint2d_e Var,
   System.double X,
   System.double Y,
   [PARAMFLAG::Out] dsSetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void SetCommandOptionPoint2D(
   dsCommandOptionPoint2d_e Var,
   System.double X,
   System.double Y,
   [Out] dsSetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionPoint2d_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionPoint2d_e.html)
- `X`: x coordinate of 2D point
- `Y`: y coordinate of 2D point
- `Result`: Status of setting the command option of the 2D point as defined in [dsSetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetCommandOptionPoint2D Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionPoint2D.html)

## Availability

DraftSight V1R1.1
