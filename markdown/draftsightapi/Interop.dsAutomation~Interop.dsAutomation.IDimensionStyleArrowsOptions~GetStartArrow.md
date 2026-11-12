---
title: "GetStartArrow Method (IDimensionStyleArrowsOptions)"
project: ""
interface: "IDimensionStyleArrowsOptions"
member: "GetStartArrow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~GetStartArrow.html"
---

# GetStartArrow Method (IDimensionStyleArrowsOptions)

Gets the type of start arrow.

## Syntax

### Visual Basic

```vb
Sub GetStartArrow( _
   ByRef ArrowType As dsDimensionArrowType_e, _
   ByRef CustomArrowBlockName As System.String _
)
```

### C#

```csharp
void GetStartArrow(
   out dsDimensionArrowType_e ArrowType,
   out System.string CustomArrowBlockName
)
```

### JScript

```
function GetStartArrow(
   ArrowType : dsDimensionArrowType_e,
   CustomArrowBlockName : System.String
);
```

### Managed Extensions for C++

```
void GetStartArrow(
   [PARAMFLAG::Out] dsDimensionArrowType_e ArrowType,
   [PARAMFLAG::Out] System.string* CustomArrowBlockName
)
```

### C++/CLI

```cpp
void GetStartArrow(
   [Out] dsDimensionArrowType_e ArrowType,
   [Out] System.String^ CustomArrowBlockName
)
```

### Parameters

- `ArrowType`: Type of start arrow as defined in [dsDimensionArrowType_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionArrowType_e.html)
- `CustomArrowBlockName`: Block name if ArrowType is set to dsDimensionArrowType_e.dsDimensionArrowType_Custom

## See Also

[IDimensionStyleArrowsOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions.html)
[IDimensionStyleArrowsOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions_members.html)
[IDimensionStyleArrowsOptions::SetStartArrow Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~SetStartArrow.html)

## Availability

DraftSight V1R1.2
