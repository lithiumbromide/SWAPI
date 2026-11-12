---
title: "SetAngleUnitExpression Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetAngleUnitExpression"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetAngleUnitExpression.html"
---

# SetAngleUnitExpression Method (IDocument)

Sets the type of angular unit and its precision for the document.

## Syntax

### Visual Basic

```vb
Sub SetAngleUnitExpression( _
   ByVal AngleType As dsAngleType_e, _
   ByVal Precision As dsUnitPrecision_e _
)
```

### C#

```csharp
void SetAngleUnitExpression(
   dsAngleType_e AngleType,
   dsUnitPrecision_e Precision
)
```

### JScript

```
function SetAngleUnitExpression(
   AngleType : dsAngleType_e,
   Precision : dsUnitPrecision_e
);
```

### Managed Extensions for C++

```
void SetAngleUnitExpression(
   dsAngleType_e AngleType,
   dsUnitPrecision_e Precision
)
```

### C++/CLI

```cpp
void SetAngleUnitExpression(
   dsAngleType_e AngleType,
   dsUnitPrecision_e Precision
)
```

### Parameters

- `AngleType`: Type of angular unit as defined in [dsAngleType_e](Interop.dsAutomation~Interop.dsAutomation.dsAngleType_e.html)
- `Precision`: Precision as defined in [dsUnitPrecision_e](Interop.dsAutomation~Interop.dsAutomation.dsUnitPrecision_e.html)

## Examples

[Get and Set Document Settings (C#)](Get_and_Set_Document_Settings_Example_CSharp.htm)
[Get and Set Document Settings (VB.NET)](Get_and_Set_Document_Settings_Example_VBNET.htm)
[Get and Set Document Settings (VBA)](Get_and_Set_Document_Settings_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetAngleUnitExpression Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetAngleUnitExpression.html)

## Availability

DraftSight V1R1
