---
title: "GetBaseAngle Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetBaseAngle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBaseAngle.html"
---

# GetBaseAngle Method (IDocument)

Gets the base angle for the document.

## Syntax

### Visual Basic

```vb
Sub GetBaseAngle( _
   ByRef Angle As System.Double, _
   ByRef Clockwise As System.Boolean _
)
```

### C#

```csharp
void GetBaseAngle(
   out System.double Angle,
   out System.bool Clockwise
)
```

### JScript

```
function GetBaseAngle(
   Angle : System.double,
   Clockwise : System.boolean
);
```

### Managed Extensions for C++

```
void GetBaseAngle(
   [PARAMFLAG::Out] System.double Angle,
   [PARAMFLAG::Out] System.bool Clockwise
)
```

### C++/CLI

```cpp
void GetBaseAngle(
   [Out] System.double Angle,
   [Out] System.bool Clockwise
)
```

### Parameters

- `Angle`: Base angle in radians
- `Clockwise`: True if the base angle is increased in the clockwise direction, false if not

## Examples

[Get and Set Document Settings (C#)](Get_and_Set_Document_Settings_Example_CSharp.htm)
[Get and Set Document Settings (VB.NET)](Get_and_Set_Document_Settings_Example_VBNET.htm)
[Get and Set Document Settings (VBA)](Get_and_Set_Document_Settings_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::SetBaseAngle Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetBaseAngle.html)
[IDocument::GetAngleUnitExpression Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetAngleUnitExpression.html)
[IDocument::SetAngleUnitExpression Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetAngleUnitExpression.html)

## Availability

DraftSight V1R1
