---
title: "GetDimensionStyleTextOptions Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetDimensionStyleTextOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleTextOptions.html"
---

# GetDimensionStyleTextOptions Method (IDimensionStyle)

Gets access to the text options of the DimensionStyle.

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

[Text options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleTextOptions.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)
[Insert and Dimension Sketch (JavaScript)](Insert_and_Dimension_Sketch_Example_JS.htm)

## Remarks

This method allows you to get or set the text options for all entities. To get or set the text options for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity, use [IDimensionStyleUserData::GetDimensionStyleTextOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleTextOptions.html).

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)

## Availability

DraftSight V1R1.2
