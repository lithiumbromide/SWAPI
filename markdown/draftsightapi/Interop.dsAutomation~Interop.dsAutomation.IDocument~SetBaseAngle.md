---
title: "SetBaseAngle Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetBaseAngle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetBaseAngle.html"
---

# SetBaseAngle Method (IDocument)

Sets the base angle for the document.

## Syntax

### Visual Basic

```vb
Sub SetBaseAngle( _
   ByVal Angle As System.Double, _
   ByVal Clockwise As System.Boolean _
)
```

### C#

```csharp
void SetBaseAngle(
   System.double Angle,
   System.bool Clockwise
)
```

### JScript

```
function SetBaseAngle(
   Angle : System.double,
   Clockwise : System.boolean
);
```

### Managed Extensions for C++

```
void SetBaseAngle(
   System.double Angle,
   System.bool Clockwise
)
```

### C++/CLI

```cpp
void SetBaseAngle(
   System.double Angle,
   System.bool Clockwise
)
```

### Parameters

- `Angle`: Base angle in radians
- `Clockwise`: True to increase the base angle in the clockwise direction, false to not

## Examples

[Get and Set Document Settings (C#)](Get_and_Set_Document_Settings_Example_CSharp.htm)
[Get and Set Document Settings (VB.NET)](Get_and_Set_Document_Settings_Example_VBNET.htm)
[Get and Set Document Settings (VBA)](Get_and_Set_Document_Settings_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetBaseAngle Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetBaseAngle.html)
[IDocument::GetAngleUnitExpression Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetAngleUnitExpression.html)
[IDocument::SetAngleUnitExpression Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetAngleUnitExpression.html)

## Availability

DraftSight V1R1
