---
title: "SelectByWindow Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "SelectByWindow"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByWindow.html"
---

# SelectByWindow Method (ISelectionManager)

Selects only the entities within the selection window or selects all of the entities within and that intersect the selection window.

## Syntax

### Visual Basic

```vb
Function SelectByWindow( _
   ByVal FirstPoint As MathPoint, _
   ByVal SecondPoint As MathPoint, _
   ByVal Crossing As System.Boolean _
) As System.Boolean
```

### C#

```csharp
System.bool SelectByWindow(
   MathPoint FirstPoint,
   MathPoint SecondPoint,
   System.bool Crossing
)
```

### JScript

```
function SelectByWindow(
   FirstPoint : MathPoint,
   SecondPoint : MathPoint,
   Crossing : System.boolean
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SelectByWindow(
   MathPoint* FirstPoint,
   MathPoint* SecondPoint,
   System.bool Crossing
)
```

### C++/CLI

```cpp
System.bool SelectByWindow(
   MathPoint^ FirstPoint,
   MathPoint^ SecondPoint,
   System.bool Crossing
)
```

### Parameters

- `FirstPoint`: First corner that defines the selection window
- `SecondPoint`: Opposite corner that defines the selection window
- `Crossing`:

  | If set to... | Then entities... |
  | --- | --- |
  | True | whose outlines intersect the selection window are within the selection window are selected. |
  | False | whose outlines are within the selection window are selected. |

### Return Value

True if the specified entities in the selection window are selected, false if not

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
[ISelectionManager::GetSelectedObjects Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)
[ISelectionManager::GetSelectedObjectCount Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjectCount.html)
[ISelectionManager::ClearSelections Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~ClearSelections.html)
[ISelectionManager::SelectByCrossline Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByCrossline.html)
[ISelectionManager::SelectByPoint Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPoint.html)
[ISelectionManager::SelectByPolygon Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPolygon.html)

## Availability

DraftSight V1R4.0
