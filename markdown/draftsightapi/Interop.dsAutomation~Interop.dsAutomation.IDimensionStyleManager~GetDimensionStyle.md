---
title: "GetDimensionStyle Method (IDimensionStyleManager)"
project: ""
interface: "IDimensionStyleManager"
member: "GetDimensionStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~GetDimensionStyle.html"
---

# GetDimensionStyle Method (IDimensionStyleManager)

Gets the specified DimensionStyle.

## Syntax

### Visual Basic

```vb
Function GetDimensionStyle( _
   ByVal Name As System.String _
) As DimensionStyle
```

### C#

```csharp
DimensionStyle GetDimensionStyle(
   System.string Name
)
```

### JScript

```
function GetDimensionStyle(
   Name : System.String
) : DimensionStyle;
```

### Managed Extensions for C++

```
DimensionStyle* GetDimensionStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
DimensionStyle^ GetDimensionStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of DimensionStyle to get

### Return Value

[DimensionStyle](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyle.html)

## See Also

[IDimensionStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager.html)
[IDimensionStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager_members.html)
[IDimensionStyleManager::GetDimensionStyles Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~GetDimensionStyles.html)
[IDimensionStyleManager::GetActiveDimensionStyle Method](Interop.dsAutomation~Interop.dsAutomation.IDimensionStyleManager~GetActiveDimensionStyle.html)

## Availability

DraftSight V1R1.1
