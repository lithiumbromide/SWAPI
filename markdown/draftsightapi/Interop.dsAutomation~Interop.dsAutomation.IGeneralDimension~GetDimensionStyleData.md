---
title: "GetDimensionStyleData Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "GetDimensionStyleData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetDimensionStyleData.html"
---

# GetDimensionStyleData Method (IGeneralDimension)

Gets the DimensionStyle of the Dimension.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleData() As DimensionStyle
```

### C#

```csharp
DimensionStyle GetDimensionStyleData()
```

### JScript

```
function GetDimensionStyleData() : DimensionStyle;
```

### Managed Extensions for C++

```
DimensionStyle* GetDimensionStyleData();
```

### C++/CLI

```cpp
DimensionStyle^ GetDimensionStyleData();
```

### Return Value

[DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)

## Remarks

If you change a DimensionStyle, then all entities using that DimensionStyle also change. However, if you use the [IDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html) interface, then you can change the DimensionStyle of a specific Dimension entity and not change all other entities using that DimensionStyle.

## See Also

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)
[IGeneralDimension::DimensionStyle Property](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~DimensionStyle.html)

## Availability

DraftSight V1R1.2
