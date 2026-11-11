---
title: "GetDimensionStyleToleranceOptions Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetDimensionStyleToleranceOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleToleranceOptions.html"
---

# GetDimensionStyleToleranceOptions Method (IDimensionStyle)

Gets access to the tolerance options of the DimensionStyle.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleToleranceOptions() As DimensionStyleToleranceOptions
```

### C#

```csharp
DimensionStyleToleranceOptions GetDimensionStyleToleranceOptions()
```

### JScript

```
function GetDimensionStyleToleranceOptions() : DimensionStyleToleranceOptions;
```

### Managed Extensions for C++

```
DimensionStyleToleranceOptions* GetDimensionStyleToleranceOptions();
```

### C++/CLI

```cpp
DimensionStyleToleranceOptions^ GetDimensionStyleToleranceOptions();
```

### Return Value

[Tolerance options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleToleranceOptions.html)

## Examples

[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## Remarks

This method allows you to get or set the tolerance options for all entities. To get or set the tolerance options for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity, use [IDimensionStyleUserData::GetDimensionStyleToleranceOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleToleranceOptions.html).

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)

## Availability

DraftSight V1R1.2
