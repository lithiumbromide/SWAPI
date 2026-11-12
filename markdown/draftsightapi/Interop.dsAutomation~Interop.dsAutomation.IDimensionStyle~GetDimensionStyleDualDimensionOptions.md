---
title: "GetDimensionStyleDualDimensionOptions Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetDimensionStyleDualDimensionOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleDualDimensionOptions.html"
---

# GetDimensionStyleDualDimensionOptions Method (IDimensionStyle)

Gets access to the dual Dimension options of the DimensionStyle.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleDualDimensionOptions() As DimensionStyleDualDimensionOptions
```

### C#

```csharp
DimensionStyleDualDimensionOptions GetDimensionStyleDualDimensionOptions()
```

### JScript

```
function GetDimensionStyleDualDimensionOptions() : DimensionStyleDualDimensionOptions;
```

### Managed Extensions for C++

```
DimensionStyleDualDimensionOptions* GetDimensionStyleDualDimensionOptions();
```

### C++/CLI

```cpp
DimensionStyleDualDimensionOptions^ GetDimensionStyleDualDimensionOptions();
```

### Return Value

[Dual Dimension options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleDualDimensionOptions.html)

## Examples

[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## Remarks

This method allows you to get or set the dual Dimension options for all entities. To get or set the dual Dimension options for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity, use [IDimensionStyleUserData::GetDimensionStyleDualDimensionOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleDualDimensionOptions.html).

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)

## Availability

DraftSight V1R1.2
