---
title: "GetDimensionStyleTextOptions Method (IDimensionStyleUserData)"
project: ""
interface: "IDimensionStyleUserData"
member: "GetDimensionStyleTextOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleTextOptions.html"
---

# GetDimensionStyleTextOptions Method (IDimensionStyleUserData)

Gets access to the text options of the DimensionStyle for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleTextOptions() As DimensionStyleTextOptions
```

### C#

```csharp
DimensionStyleTextOptions GetDimensionStyleTextOptions()
```

### JScript

```
function GetDimensionStyleTextOptions() : DimensionStyleTextOptions;
```

### Managed Extensions for C++

```
DimensionStyleTextOptions* GetDimensionStyleTextOptions();
```

### C++/CLI

```cpp
DimensionStyleTextOptions^ GetDimensionStyleTextOptions();
```

### Return Value

[Text options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleTextOptions.html) of a Dimension, Leader, or geometric Tolerance entity

## Examples

[Change DimensionStyle Options of Leader (C#)](Change_DimensionStyle_Options_of_Leader_Example_CSharp.htm)
[Change DimensionStyle Options of Leader (VB.NET)](Change_DimensionStyle_Options_of_Leader_Example_VBNET.htm)
[Change DimensionStyle Options of Leader (VBA)](Change_DimensionStyle_Options_of_Leader_Example_VBA.htm)

## Remarks

This method allows you to get or set the text options of this DimensionStyle for a specific Dimension, Leader, or geometric Tolerance entity. To get or set the text options for all entities, use [IDimensionStyle::GetDimensionStyleTextOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleTextOptions.html).

## See Also

[IDimensionStyleUserData Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)
[IDimensionStyleUserData Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData_members.html)

## Availability

DraftSight V1R4.0
