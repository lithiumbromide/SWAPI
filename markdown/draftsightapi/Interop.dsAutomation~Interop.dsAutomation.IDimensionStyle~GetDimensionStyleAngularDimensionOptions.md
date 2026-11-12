---
title: "GetDimensionStyleAngularDimensionOptions Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetDimensionStyleAngularDimensionOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleAngularDimensionOptions.html"
---

# GetDimensionStyleAngularDimensionOptions Method (IDimensionStyle)

Gets access to the angular Dimension options of the DimensionStyle.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleAngularDimensionOptions() As DimensionStyleAngularDimensionOptions
```

### C#

```csharp
DimensionStyleAngularDimensionOptions GetDimensionStyleAngularDimensionOptions()
```

### JScript

```
function GetDimensionStyleAngularDimensionOptions() : DimensionStyleAngularDimensionOptions;
```

### Managed Extensions for C++

```
DimensionStyleAngularDimensionOptions* GetDimensionStyleAngularDimensionOptions();
```

### C++/CLI

```cpp
DimensionStyleAngularDimensionOptions^ GetDimensionStyleAngularDimensionOptions();
```

### Return Value

[Angular Dimension options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleAngularDimensionOptions.html)

## Examples

[Get DimensionStyle Names and Options (C#)](Get_DimensionStyle_Names_and_Options_Example_CSharp.htm)
[Get DimensionStyle Names and Options (VB.NET)](Get_DimensionStyle_Names_and_Options_Example_VBNET.htm)
[Get DimensionStyle Names and Options (VBA)](Get_DimensionStyle_Names_and_Options_Example_VBA.htm)
[Get DimensionStyle Names and Options (JavaScript)](Get_DimensionStyle_Names_and_Options_Example_JS.htm)

## Remarks

This method allows you to get or set the angular Dimension options for all entities. To get or set the angular Dimension options for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity, use [IDimensionStyleUserData::GetDimensionStyleAngularDimensionOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleAngularDimensionOptions.html).

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)

## Availability

DraftSight V1R1.2
