---
title: "GetLeaderArrow Method (IDimensionStyleArrowsOptions)"
project: ""
interface: "IDimensionStyleArrowsOptions"
member: "GetLeaderArrow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~GetLeaderArrow.html"
---

# GetLeaderArrow Method (IDimensionStyleArrowsOptions)

Gets the type of leader arrow.

## Syntax

### Visual Basic

```vb
Sub GetLeaderArrow( _
   ByRef ArrowType As dsDimensionArrowType_e, _
   ByRef CustomArrowBlockName As System.String _
)
```

### C#

```csharp
void GetLeaderArrow(
   out dsDimensionArrowType_e ArrowType,
   out System.string CustomArrowBlockName
)
```

### JScript

```
function GetLeaderArrow(
   ArrowType : dsDimensionArrowType_e,
   CustomArrowBlockName : System.String
);
```

### Managed Extensions for C++

```
void GetLeaderArrow(
   [PARAMFLAG::Out] dsDimensionArrowType_e ArrowType,
   [PARAMFLAG::Out] System.string* CustomArrowBlockName
)
```

### C++/CLI

```cpp
void GetLeaderArrow(
   [Out] dsDimensionArrowType_e ArrowType,
   [Out] System.String^ CustomArrowBlockName
)
```

### Parameters

- `ArrowType`: Type of leader arrow as defined in [dsDimensionArrowType_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionArrowType_e.html)
- `CustomArrowBlockName`: Block name if ArrowType is set to dsDimensionArrowType_e.dsDimensionArrowType_Custom

## See Also

[IDimensionStyleArrowsOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions.html)
[IDimensionStyleArrowsOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions_members.html)
[IDimensionStyleArrowsOptions::SetLeaderArrow Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~SetLeaderArrow.html)

## Availability

DraftSight V1R1.2
