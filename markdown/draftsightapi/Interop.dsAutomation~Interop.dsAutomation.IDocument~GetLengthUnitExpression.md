---
title: "GetLengthUnitExpression Method (IDocument)"
project: ""
interface: "IDocument"
member: "GetLengthUnitExpression"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDocument~GetLengthUnitExpression.html"
---

# GetLengthUnitExpression Method (IDocument)

Gets the type of linear unit and its precision for the document.

## Syntax

### Visual Basic

```vb
Sub GetLengthUnitExpression( _
   ByRef LengthType As dsLengthType_e, _
   ByRef Precision As dsUnitPrecision_e _
)
```

### C#

```csharp
void GetLengthUnitExpression(
   out dsLengthType_e LengthType,
   out dsUnitPrecision_e Precision
)
```

### JScript

```
function GetLengthUnitExpression(
   LengthType : dsLengthType_e,
   Precision : dsUnitPrecision_e
);
```

### Managed Extensions for C++

```
void GetLengthUnitExpression(
   [PARAMFLAG::Out] dsLengthType_e LengthType,
   [PARAMFLAG::Out] dsUnitPrecision_e Precision
)
```

### C++/CLI

```cpp
void GetLengthUnitExpression(
   [Out] dsLengthType_e LengthType,
   [Out] dsUnitPrecision_e Precision
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
[IDocument::SetLengthUnitExpression Method](Interop.dsAutomation~Interop.dsAutomation.IDocument~SetLengthUnitExpression.html)

## Availability

DraftSight V1R1
