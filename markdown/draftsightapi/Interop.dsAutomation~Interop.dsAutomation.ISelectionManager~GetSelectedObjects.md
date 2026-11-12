---
title: "GetSelectedObjects Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "GetSelectedObjects"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html"
---

# GetSelectedObjects Method (ISelectionManager)

Gets the selected entities of the specified entity types.

## Syntax

### Visual Basic

```vb
Function GetSelectedObjects( _
   ByVal SSType As dsSelectionSetType_e, _
   ByRef EntityTypeLongArray As System.Object _
) As System.Object
```

### C#

```csharp
System.object GetSelectedObjects(
   dsSelectionSetType_e SSType,
   out System.object EntityTypeLongArray
)
```

### JScript

```
function GetSelectedObjects(
   SSType : dsSelectionSetType_e,
   EntityTypeLongArray : System.Object
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* GetSelectedObjects(
   dsSelectionSetType_e SSType,
   [PARAMFLAG::Out] System.Object* EntityTypeLongArray
)
```

### C++/CLI

```cpp
System.Object^ GetSelectedObjects(
   dsSelectionSetType_e SSType,
   [Out] System.Object^ EntityTypeLongArray
)
```

### Parameters

- `SSType`: Type of selection as defined in [dsSelectionSetType_e](Interop.dsAutomation~Interop.dsAutomation.dsSelectionSetType_e.html)
- `EntityTypeLongArray`: Array of entity types as defined in [dsObjectType_e](Interop.dsAutomation~Interop.dsAutomation.dsObjectType_e.html)

### Return Value

Array of selected entities of the specified entity types

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
[ISelectionManager::GetSelectedObjectCount Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjectCount.html)

## Availability

DraftSight V1R5.0
