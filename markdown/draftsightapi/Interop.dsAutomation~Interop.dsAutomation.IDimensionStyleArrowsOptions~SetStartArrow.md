---
title: "SetStartArrow Method (IDimensionStyleArrowsOptions)"
project: ""
interface: "IDimensionStyleArrowsOptions"
member: "SetStartArrow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~SetStartArrow.html"
---

# SetStartArrow Method (IDimensionStyleArrowsOptions)

Sets the type of start arrow.

## Syntax

### Visual Basic

```vb
Sub SetStartArrow( _
   ByVal ArrowType As dsDimensionArrowType_e, _
   ByVal CustomArrowBlockName As System.String _
)
```

### C#

```csharp
void SetStartArrow(
   dsDimensionArrowType_e ArrowType,
   System.string CustomArrowBlockName
)
```

### JScript

```
function SetStartArrow(
   ArrowType : dsDimensionArrowType_e,
   CustomArrowBlockName : System.String
);
```

### Managed Extensions for C++

```
void SetStartArrow(
   dsDimensionArrowType_e ArrowType,
   System.string* CustomArrowBlockName
)
```

### C++/CLI

```cpp
void SetStartArrow(
   dsDimensionArrowType_e ArrowType,
   System.String^ CustomArrowBlockName
)
```

### Parameters

- `ArrowType`: Type of start arrow as defined in [dsDimensionArrowType_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionArrowType_e.html)
- `CustomArrowBlockName`: Block name if ArrowType is set to dsDimensionArrowType_e.dsDimensionArrowType_Custom

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[IDimensionStyleArrowsOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions.html)
[IDimensionStyleArrowsOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions_members.html)
[IDimensionStyleArrowsOptions::GetStartArrow Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~GetStartArrow.html)

## Availability

DraftSight V1R1.2
