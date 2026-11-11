---
title: "GetEndArrow Method (IDimensionStyleArrowsOptions)"
project: ""
interface: "IDimensionStyleArrowsOptions"
member: "GetEndArrow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~GetEndArrow.html"
---

# GetEndArrow Method (IDimensionStyleArrowsOptions)

Gets the type of end arrow.

## Syntax

### Visual Basic

```vb
Sub GetEndArrow( _
   ByRef ArrowType As dsDimensionArrowType_e, _
   ByRef CustomArrowBlockName As System.String _
)
```

### C#

```csharp
void GetEndArrow(
   out dsDimensionArrowType_e ArrowType,
   out System.string CustomArrowBlockName
)
```

### JScript

```
function GetEndArrow(
   ArrowType : dsDimensionArrowType_e,
   CustomArrowBlockName : System.String
);
```

### Managed Extensions for C++

```
void GetEndArrow(
   [PARAMFLAG::Out] dsDimensionArrowType_e ArrowType,
   [PARAMFLAG::Out] System.string* CustomArrowBlockName
)
```

### C++/CLI

```cpp
void GetEndArrow(
   [Out] dsDimensionArrowType_e ArrowType,
   [Out] System.String^ CustomArrowBlockName
)
```

### Parameters

- `ArrowType`: Type of end arrow as defined in [dsDimensionArrowType_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionArrowType_e.html)
- `CustomArrowBlockName`: Block name if ArrowType is set to dsDimensionArrowType_e.dsDimensionArrowType_Custom

## See Also

[IDimensionStyleArrowsOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions.html)
[IDimensionStyleArrowsOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions_members.html)
[IDimensionStyleArrowsOptions::SetEndArrow Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~SetEndArrow.html)

## Availability

DraftSight V1R1.2
