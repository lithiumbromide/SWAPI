---
title: "GetDimensionStyleLinearDimensionOptions Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetDimensionStyleLinearDimensionOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleLinearDimensionOptions.html"
---

# GetDimensionStyleLinearDimensionOptions Method (IDimensionStyle)

Gets access to the linear Dimension options of the DimensionStyle.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleLinearDimensionOptions() As DimensionStyleLinearDimensionOptions
```

### C#

```csharp
DimensionStyleLinearDimensionOptions GetDimensionStyleLinearDimensionOptions()
```

### JScript

```
function GetDimensionStyleLinearDimensionOptions() : DimensionStyleLinearDimensionOptions;
```

### Managed Extensions for C++

```
DimensionStyleLinearDimensionOptions* GetDimensionStyleLinearDimensionOptions();
```

### C++/CLI

```cpp
DimensionStyleLinearDimensionOptions^ GetDimensionStyleLinearDimensionOptions();
```

### Return Value

[Linear Dimension options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleLinearDimensionOptions.html)

## Examples

[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## Remarks

This method allows you to get or set the linear Dimension options for all entities. To get or set the linear Dimension options for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity, use [IDimensionStyleUserData::GetDimensionStyleLinearDimensionOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleLinearDimensionOptions.html).

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)

## Availability

DraftSight V1R1.2
