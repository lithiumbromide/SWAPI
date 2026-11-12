---
title: "GetDimensionStyleUserData Method (IGeneralDimension)"
project: ""
interface: "IGeneralDimension"
member: "GetDimensionStyleUserData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension~GetDimensionStyleUserData.html"
---

# GetDimensionStyleUserData Method (IGeneralDimension)

Gets the DimensionStyle user data, including overrides, of the Dimension.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyleUserData() As DimensionStyleUserData
```

### C#

```csharp
DimensionStyleUserData GetDimensionStyleUserData()
```

### JScript

```
function GetDimensionStyleUserData() : DimensionStyleUserData;
```

### Managed Extensions for C++

```
DimensionStyleUserData* GetDimensionStyleUserData();
```

### C++/CLI

```cpp
DimensionStyleUserData^ GetDimensionStyleUserData();
```

### Return Value

[IDimensionStyleUserData](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleUserData.html)

## Remarks

If you change a [DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html), then all entities using that DimensionStyle also change. However, if you get the IDimensionStyleUserData interface, then you can change the DimensionStyle of a specific Dimension entity and not change all other entities using that DimensionStyle.

## See Also

[IGeneralDimension Interface](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension.html)
[IGeneralDimension Members](Interop.dsAutomation~Interop.dsAutomation.IGeneralDimension_members.html)

## Availability

DraftSight V1R4.0
