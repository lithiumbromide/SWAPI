---
title: "SelectByCrossline Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "SelectByCrossline"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByCrossline.html"
---

# SelectByCrossline Method (ISelectionManager)

Selects the entities that intersect the specified line.

## Syntax

### Visual Basic

```vb
Function SelectByCrossline( _
   ByVal CoordinateDblArray As System.Object _
) As System.Boolean
```

### C#

```csharp
System.bool SelectByCrossline(
   System.object CoordinateDblArray
)
```

### JScript

```
function SelectByCrossline(
   CoordinateDblArray : System.Object
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SelectByCrossline(
   System.Object* CoordinateDblArray
)
```

### C++/CLI

```cpp
System.bool SelectByCrossline(
   System.Object^ CoordinateDblArray
)
```

### Parameters

- `CoordinateDblArray`: Array of the x, y, and z coordinates of the points that define the line

### Return Value

True if the entities intersecting the line are selected, false if not

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
[ISelectionManager::GetSelectedObjects Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)
[ISelectionManager::GetSelectedObjectCount Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjectCount.html)
[ISelectionManager::ClearSelections Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~ClearSelections.html)
[ISelectionManager::SelectByPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPoint.html)
[ISelectionManager::SelectByPolygon Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPolygon.html)
[ISelectionManager::SelectByWindow Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByWindow.html)

## Availability

DraftSight V1R4.0
