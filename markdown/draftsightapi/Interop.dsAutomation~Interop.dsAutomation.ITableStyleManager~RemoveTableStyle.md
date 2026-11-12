---
title: "RemoveTableStyle Method (ITableStyleManager)"
project: ""
interface: "ITableStyleManager"
member: "RemoveTableStyle"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~RemoveTableStyle.html"
---

# RemoveTableStyle Method (ITableStyleManager)

Removes the specified TableStyle.

## Syntax

### Visual Basic

```vb
Function RemoveTableStyle( _
   ByVal Name As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool RemoveTableStyle(
   System.string Name
)
```

### JScript

```
function RemoveTableStyle(
   Name : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool RemoveTableStyle(
   System.string* Name
)
```

### C++/CLI

```cpp
System.bool RemoveTableStyle(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of TableStyle to remove

## See Also

[ITableStyleManager Interface](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager.html)
[ITableStyleManager Members](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager_members.html)
[ITableStyleManager::CreateTableStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~CreateTableStyle.html)
[ITableStyleManager::GetActiveTableStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~GetActiveTableStyle.html)
[ITableStyleManager::GetTableStyle Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~GetTableStyle.html)
[ITableStyleManager::GetTableStyles Method](Interop.dsAutomation~Interop.dsAutomation.ITableStyleManager~GetTableStyles.html)
[ITableStyle::Name Property](Interop.dsAutomation~Interop.dsAutomation.ITableStyle~Name.html)

## Availability

DraftSight V1R3.0
