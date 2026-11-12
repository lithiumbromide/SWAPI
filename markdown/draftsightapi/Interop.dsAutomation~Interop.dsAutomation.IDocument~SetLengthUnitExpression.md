---
title: "SetLengthUnitExpression Method (IDocument)"
project: ""
interface: "IDocument"
member: "SetLengthUnitExpression"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~SetLengthUnitExpression.html"
---

# SetLengthUnitExpression Method (IDocument)

Sets the type of linear unit and its precision for the document.

## Syntax

### Visual Basic

```vb
Sub SetLengthUnitExpression( _
   ByVal LengthType As dsLengthType_e, _
   ByVal Precision As dsUnitPrecision_e _
)
```

### C#

```csharp
void SetLengthUnitExpression(
   dsLengthType_e LengthType,
   dsUnitPrecision_e Precision
)
```

### JScript

```
function SetLengthUnitExpression(
   LengthType : dsLengthType_e,
   Precision : dsUnitPrecision_e
);
```

### Managed Extensions for C++

```
void SetLengthUnitExpression(
   dsLengthType_e LengthType,
   dsUnitPrecision_e Precision
)
```

### C++/CLI

```cpp
void SetLengthUnitExpression(
   dsLengthType_e LengthType,
   dsUnitPrecision_e Precision
)
```

### Parameters

- `LengthType`: Type of linear unit as defined in [dsLengthType_e](Interop.dsAutomation~Interop.dsAutomation.dsLengthType_e.html)
- `Precision`: Precision as defined in [dsUnitPrecision_e](Interop.dsAutomation~Interop.dsAutomation.dsUnitPrecision_e.html)

## Examples

[Get and Set Document Settings (C#)](Get_and_Set_Document_Settings_Example_CSharp.htm)
[Get and Set Document Settings (VB.NET)](Get_and_Set_Document_Settings_Example_VBNET.htm)
[Get and Set Document Settings (VBA)](Get_and_Set_Document_Settings_Example_VBA.htm)

## See Also

[IDocument Interface](Interop.dsAutomation~Interop.dsAutomation.IDocument.html)
[IDocument Members](Interop.dsAutomation~Interop.dsAutomation.IDocument_members.html)
[IDocument::GetLengthUnitExpression Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~GetLengthUnitExpression.html)

## Availability

DraftSight V1R1
