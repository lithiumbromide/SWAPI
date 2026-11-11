---
title: "SetLeaderArrow Method (IDimensionStyleArrowsOptions)"
project: ""
interface: "IDimensionStyleArrowsOptions"
member: "SetLeaderArrow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~SetLeaderArrow.html"
---

# SetLeaderArrow Method (IDimensionStyleArrowsOptions)

Sets the type of leader arrow.

## Syntax

### Visual Basic

```vb
Sub SetLeaderArrow( _
   ByVal ArrowType As dsDimensionArrowType_e, _
   ByVal CustomArrowBlockName As System.String _
)
```

### C#

```csharp
void SetLeaderArrow(
   dsDimensionArrowType_e ArrowType,
   System.string CustomArrowBlockName
)
```

### JScript

```
function SetLeaderArrow(
   ArrowType : dsDimensionArrowType_e,
   CustomArrowBlockName : System.String
);
```

### Managed Extensions for C++

```
void SetLeaderArrow(
   dsDimensionArrowType_e ArrowType,
   System.string* CustomArrowBlockName
)
```

### C++/CLI

```cpp
void SetLeaderArrow(
   dsDimensionArrowType_e ArrowType,
   System.String^ CustomArrowBlockName
)
```

### Parameters

- `ArrowType`: Type of leader arrow as defined in [dsDimensionArrowType_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionArrowType_e.html)
- `CustomArrowBlockName`: Block name if ArrowType is set to dsDimensionArrowType_e.dsDimensionArrowType_Custom

## Examples

[Change DimensionStyle Options of Leader (C#)](Change_DimensionStyle_Options_of_Leader_Example_CSharp.htm)
[Change DimensionStyle Options of Leader (VB.NET)](Change_DimensionStyle_Options_of_Leader_Example_VBNET.htm)
[Change DimensionStyle Options of Leader (VBA)](Change_DimensionStyle_Options_of_Leader_Example_VBA.htm)

## See Also

[IDimensionStyleArrowsOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions.html)
[IDimensionStyleArrowsOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions_members.html)
[IDimensionStyleArrowsOptions::GetLeaderArrow Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~GetLeaderArrow.html)

## Availability

DraftSight V1R1.2
