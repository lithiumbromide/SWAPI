---
title: "GetTableStyle Method (ITableStyleManager)"
project: ""
interface: "ITableStyleManager"
member: "GetTableStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~GetTableStyle.html"
---

# GetTableStyle Method (ITableStyleManager)

Gets the specified TableStyle.

## Syntax

### Visual Basic

```vb
Function GetTableStyle( _
   ByVal Name As System.String _
) As TableStyle
```

### C#

```csharp
TableStyle GetTableStyle(
   System.string Name
)
```

### JScript

```
function GetTableStyle(
   Name : System.String
) : TableStyle;
```

### Managed Extensions for C++

```
TableStyle* GetTableStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
TableStyle^ GetTableStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of TableStyle

### Return Value

[TableStyle](Interop.dsAutomation~Interop.dsAutomation.ITableStyle.html)

## See Also

[ITableStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager.html)
[ITableStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager_members.html)
[ITableStyleManager::GetActiveTableStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~GetActiveTableStyle.html)
[ITableStyleManager::GetTableStyles Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~GetTableStyles.html)
[ITableStyleManager::RemoveTableStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~RemoveTableStyle.html)

## Availability

DraftSight V1R3.0
