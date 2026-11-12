---
title: "GetDimensionStyleArrowsOptions Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetDimensionStyleArrowsOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleArrowsOptions.html"
---

# GetDimensionStyleArrowsOptions Method (IDimensionStyle)

Gets access to the arrow options of the DimensionStyle.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleArrowsOptions() As DimensionStyleArrowsOptions
```

### C#

```csharp
DimensionStyleArrowsOptions GetDimensionStyleArrowsOptions()
```

### JScript

```
function GetDimensionStyleArrowsOptions() : DimensionStyleArrowsOptions;
```

### Managed Extensions for C++

```
DimensionStyleArrowsOptions* GetDimensionStyleArrowsOptions();
```

### C++/CLI

```cpp
DimensionStyleArrowsOptions^ GetDimensionStyleArrowsOptions();
```

### Return Value

[Arrow options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## Remarks

This method allows you to get or set the arrow options for all entities. To get or set the arrow options for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity, use [IDimensionStyleUserData::GetDimensionStyleArrowsOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleArrowsOptions.html).

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)

## Availability

DraftSight V1R1.2
