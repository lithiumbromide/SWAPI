---
title: "SelectByPolygon Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "SelectByPolygon"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPolygon.html"
---

# SelectByPolygon Method (ISelectionManager)

Selects only the entities within a polygon or selects the entities within and that intersect the polygon.

## Syntax

### Visual Basic

```vb
Function SelectByPolygon( _
   ByVal CoordinateDblArray As System.Object, _
   ByVal Crossing As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool SelectByPolygon(
   System.object CoordinateDblArray,
   System.bool Crossing
)
```

### JScript

```
function SelectByPolygon(
   CoordinateDblArray : System.Object,
   Crossing : System.boolean
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SelectByPolygon(
   System.Object* CoordinateDblArray,
   System.bool Crossing
)
```

### C++/CLI

```cpp
System.bool SelectByPolygon(
   System.Object^ CoordinateDblArray,
   System.bool Crossing
)
```

### Parameters

- `CoordinateDblArray`: Array of x, y, and z coordinates of the points that define the polygon
- `Crossing`:

  | If set to... | Then entities... |
  | --- | --- |
  | True | whose outlines intersect the polygon are within polygon are selected. |
  | False | whose outlines are within the polygon are selected. |

### Return Value

True if the specified entities are selected, false if not

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
[ISelectionManager::GetSelectedObjects Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)
[ISelectionManager::GetSelectedObjectCount Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjectCount.html)
[ISelectionManager::ClearSelections Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~ClearSelections.html)
[ISelectionManager::SelectByCrossline Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByCrossline.html)
[ISelectionManager::SelectByPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPoint.html)
[ISelectionManager::SelectByWindow Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByWindow.html)

## Availability

DraftSight V1R4.0
