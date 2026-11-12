---
title: "GetDimensionStyleRadialDiameterDimensionOptions Method (IDimensionStyle)"
project: ""
interface: "IDimensionStyle"
member: "GetDimensionStyleRadialDiameterDimensionOptions"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle~GetDimensionStyleRadialDiameterDimensionOptions.html"
---

# GetDimensionStyleRadialDiameterDimensionOptions Method (IDimensionStyle)

Gets access to radius or diameter Dimension options of the DimensionStyle.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleRadialDiameterDimensionOptions() As DimensionStyleRadialDiameterDimensionOptions
```

### C#

```csharp
DimensionStyleRadialDiameterDimensionOptions GetDimensionStyleRadialDiameterDimensionOptions()
```

### JScript

```
function GetDimensionStyleRadialDiameterDimensionOptions() : DimensionStyleRadialDiameterDimensionOptions;
```

### Managed Extensions for C++

```
DimensionStyleRadialDiameterDimensionOptions* GetDimensionStyleRadialDiameterDimensionOptions();
```

### C++/CLI

```cpp
DimensionStyleRadialDiameterDimensionOptions^ GetDimensionStyleRadialDiameterDimensionOptions();
```

### Return Value

[Radius or diameter Dimension options of the DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleRadialDiameterDimensionOptions.html)

## Examples

[Create and Apply DimensionStyle (C#)](Create_and_Apply_DimensionStyle_Example_CSharp.htm)
[Create and Apply DimensionStyle (VB.NET)](Create_and_Apply_DimensionStyle_Example_VBNET.htm)
[Create and Apply DimensionStyle (VBA)](Create_and_Apply_DimensionStyle_Example_VBA.htm)

## Remarks

This method allows you to get or set the radius or diameter Dimension options for all entities. To get or set the radius or diameter Dimension options for a specific [Dimension](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html), [Leader](Interop.dsAutomation~Interop.dsAutomation.ILeader.html), or [geometric Tolerance](Interop.dsAutomation~Interop.dsAutomation.ITolerance.html) entity, use [IDimensionStyleUserData::GetDimensionStyleRadialDiameterDimensionOptions](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData~GetDimensionStyleRadialDiameterDimensionOptions.html).

## See Also

[IDimensionStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)
[IDimensionStyle Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle_members.html)

## Availability

DraftSight V1R1.2
