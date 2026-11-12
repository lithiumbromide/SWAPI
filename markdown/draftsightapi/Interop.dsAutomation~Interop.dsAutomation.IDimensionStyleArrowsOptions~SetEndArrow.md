---
title: "SetEndArrow Method (IDimensionStyleArrowsOptions)"
project: ""
interface: "IDimensionStyleArrowsOptions"
member: "SetEndArrow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~SetEndArrow.html"
---

# SetEndArrow Method (IDimensionStyleArrowsOptions)

Sets the type of end arrow.

## Syntax

### Visual Basic

```vb
Sub SetEndArrow( _
   ByVal ArrowType As dsDimensionArrowType_e, _
   ByVal CustomArrowBlockName As System.String _
)
```

### C#

```csharp
void SetEndArrow(
   dsDimensionArrowType_e ArrowType,
   System.string CustomArrowBlockName
)
```

### JScript

```
function SetEndArrow(
   ArrowType : dsDimensionArrowType_e,
   CustomArrowBlockName : System.String
);
```

### Managed Extensions for C++

```
void SetEndArrow(
   dsDimensionArrowType_e ArrowType,
   System.string* CustomArrowBlockName
)
```

### C++/CLI

```cpp
void SetEndArrow(
   dsDimensionArrowType_e ArrowType,
   System.String^ CustomArrowBlockName
)
```

### Parameters

- `ArrowType`: Type of end arrow as defined in [dsDimensionArrowType_e](Interop.dsAutomation~Interop.dsAutomation.dsDimensionArrowType_e.html)
- `CustomArrowBlockName`: Block name if ArrowType is set to dsDimensionArrowType_e.dsDimensionArrowType_Custom

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## See Also

[IDimensionStyleArrowsOptions Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions.html)
[IDimensionStyleArrowsOptions Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions_members.html)
[IDimensionStyleArrowsOptions::GetEndArrow Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions~GetEndArrow.html)

## Availability

DraftSight V1R1.2
