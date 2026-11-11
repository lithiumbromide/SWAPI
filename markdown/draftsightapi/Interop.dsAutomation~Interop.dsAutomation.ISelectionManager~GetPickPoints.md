---
title: "GetPickPoints Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "GetPickPoints"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetPickPoints.html"
---

# GetPickPoints Method (ISelectionManager)

Gets the pick points for the selection.

## Syntax

### Visual Basic

```vb
Sub GetPickPoints( _
   ByVal SSType As dsSelectionSetType_e, _
   ByRef CoordinateDblArray As System.Object _
)
```

### C#

```csharp
void GetPickPoints(
   dsSelectionSetType_e SSType,
   out System.object CoordinateDblArray
)
```

### JScript

```
function GetPickPoints(
   SSType : dsSelectionSetType_e,
   CoordinateDblArray : System.Object
);
```

### Managed Extensions for C++

```
void GetPickPoints(
   dsSelectionSetType_e SSType,
   [PARAMFLAG::Out] System.Object* CoordinateDblArray
)
```

### C++/CLI

```cpp
void GetPickPoints(
   dsSelectionSetType_e SSType,
   [Out] System.Object^ CoordinateDblArray
)
```

### Parameters

- `SSType`: Type of selection as defined in [dsSelectionSetType_e](Interop.dsAutomation~Interop.dsAutomation.dsSelectionSetType_e.html)
- `CoordinateDblArray`: Array of doubles of the x, y, and z coordinates of the pick points

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)

## Availability

DraftSight V1R5.0
