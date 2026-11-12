---
title: "GetAngleUnitExpression Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetAngleUnitExpression"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetAngleUnitExpression.html"
---

# GetAngleUnitExpression Method (IDocument)

Gets the type of angular unit and its precision for the document.

## Syntax

### Visual Basic

```vb
Sub GetAngleUnitExpression( _
   ByRef AngleType As dsAngleType_e, _
   ByRef Precision As dsUnitPrecision_e _
)
```

### C#

```csharp
void GetAngleUnitExpression(
   out dsAngleType_e AngleType,
   out dsUnitPrecision_e Precision
)
```

### JScript

```
function GetAngleUnitExpression(
   AngleType : dsAngleType_e,
   Precision : dsUnitPrecision_e
);
```

### Managed Extensions for C++

```
void GetAngleUnitExpression(
   [PARAMFLAG::Out] dsAngleType_e AngleType,
   [PARAMFLAG::Out] dsUnitPrecision_e Precision
)
```

### C++/CLI

```cpp
void GetAngleUnitExpression(
   [Out] dsAngleType_e AngleType,
   [Out] dsUnitPrecision_e Precision
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
[IDocument::SetAngleUnitExpression Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetAngleUnitExpression.html)

## Availability

DraftSight V1R1
