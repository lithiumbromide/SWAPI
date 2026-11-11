---
title: "GetDimensionStyleArrowsOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleArrowsOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleArrowsOptions.html"
---

# GetDimensionStyleArrowsOptions Method (IDimensionStyleUserData)

Gets access to the arrow options of the DimensionStyle for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

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

[Arrow options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleArrowsOptions.html) of a Dimension, Leader, or geometric Tolerance entity

## Examples

[Change DimensionStyle Options of Leader (C#)](Change_DimensionStyle_Options_of_Leader_Example_CSharp.htm)
[Change DimensionStyle Options of Leader (VB.NET)](Change_DimensionStyle_Options_of_Leader_Example_VBNET.htm)
[Change DimensionStyle Options of Leader (VBA)](Change_DimensionStyle_Options_of_Leader_Example_VBA.htm)

## Remarks

This method allows you to get or set the arrow options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the arrow options for all entities, use [IDimensionStyle::GetDimensionStyleArrowsOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleArrowsOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
