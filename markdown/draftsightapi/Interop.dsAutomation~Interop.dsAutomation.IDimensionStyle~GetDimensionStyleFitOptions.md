---
title: "GetDimensionStyleFitOptions Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetDimensionStyleFitOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleFitOptions.html"
---

# GetDimensionStyleFitOptions Method (IDimensionStyle)

Gets access to the fit options of the DimensionStyle.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleFitOptions() As DimensionStyleFitOptions
```

### C#

```csharp
DimensionStyleFitOptions GetDimensionStyleFitOptions()
```

### JScript

```
function GetDimensionStyleFitOptions() : DimensionStyleFitOptions;
```

### Managed Extensions for C++

```
DimensionStyleFitOptions* GetDimensionStyleFitOptions();
```

### C++/CLI

```cpp
DimensionStyleFitOptions^ GetDimensionStyleFitOptions();
```

### Return Value

[Fit options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleFitOptions.html)

## Examples

[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## Remarks

This method allows you to get or set the fit options for all entities. To get or set the fit options for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity, use [IDimensionStyleUserData::GetDimensionStyleFitOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleFitOptions.html).

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)

## Availability

DraftSight V1R1.2
