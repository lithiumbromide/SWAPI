---
title: "SetCommandOptionPoint3D Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetCommandOptionPoint3D"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetCommandOptionPoint3D.html"
---

# SetCommandOptionPoint3D Method (IDocument)

Sets the command option for the specified 3D point in the document.

## Syntax

### Visual Basic

```vb
Sub SetCommandOptionPoint3D( _
   ByVal Var As dsCommandOptionPoint3d_e, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByRef Result As dsSetCommandOptionResult_e _
)
```

### C#

```csharp
void SetCommandOptionPoint3D(
   dsCommandOptionPoint3d_e Var,
   System.double X,
   System.double Y,
   System.double Z,
   out dsSetCommandOptionResult_e Result
)
```

### JScript

```
function SetCommandOptionPoint3D(
   Var : dsCommandOptionPoint3d_e,
   X : System.double,
   Y : System.double,
   Z : System.double,
   Result : dsSetCommandOptionResult_e
);
```

### Managed Extensions for C++

```
void SetCommandOptionPoint3D(
   dsCommandOptionPoint3d_e Var,
   System.double X,
   System.double Y,
   System.double Z,
   [PARAMFLAG::Out] dsSetCommandOptionResult_e Result
)
```

### C++/CLI

```cpp
void SetCommandOptionPoint3D(
   dsCommandOptionPoint3d_e Var,
   System.double X,
   System.double Y,
   System.double Z,
   [Out] dsSetCommandOptionResult_e Result
)
```

### Parameters

- `Var`: Command option as defined in [dsCommandOptionPoint3d_e](Interop.dsAutomation~Interop.dsAutomation.dsCommandOptionPoint3d_e.html)
- `X`: x coordinate of 3D point
- `Y`: y coordinate of 3D point
- `Z`: z coordinate of 3D point
- `Result`: Status of setting the command option of the 3D point as defined in [dsSetCommandOptionResult_e](Interop.dsAutomation~Interop.dsAutomation.dsSetCommandOptionResult_e.html)

## Examples

[Get and Set Command Options (C#)](Get_and_Set_Command_Options_Example_CSharp.htm)
[Get and Set Command Options (VB.NET)](Get_and_Set_Command_Options_Example_VBNET.htm)
[Get and Set Command Options (VBA)](Get_and_Set_Command_Options_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetCommandOptionPoint3D Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetCommandOptionPoint3D.html)

## Availability

DraftSight V1R1.1
