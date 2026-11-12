---
title: "SelectByPoint Method (ISelectionManager)"
project: ""
interface: "ISelectionManager"
member: "SelectByPoint"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPoint.html"
---

# SelectByPoint Method (ISelectionManager)

Selects an entity at the specified point.

## Syntax

### Visual Basic

```vb
Function SelectByPoint( _
   ByVal Point As MathPoint _
) As System.Boolean
```

### C#

```csharp
System.bool SelectByPoint(
   MathPoint Point
)
```

### JScript

```
function SelectByPoint(
   Point : MathPoint
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool SelectByPoint(
   MathPoint* Point
)
```

### C++/CLI

```cpp
System.bool SelectByPoint(
   MathPoint^ Point
)
```

### Parameters

- `Point`: [Point](Interop.dsAutomation~Interop.dsAutomation.IMathPoint.html)

### Return Value

True if the entity at the specified point is selected, false if not

## Remarks

To select multiple entities, use [ISelectionManager::SelectByPolygon](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByPolygon.html), [ISelectionManager::SelectByWindow](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByWindow.html), or [ISelectionManager::SelectByCrossLine](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~SelectByCrossline.html).

## See Also

[ISelectionManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager.html)
[ISelectionManager Members](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager_members.html)
[ISelectionManager::GetSelectedObject Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObject.html)
[ISelectionManager::GetSelectedObjects Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjects.html)
[ISelectionManager::GetSelectedObjectCount Method ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~GetSelectedObjectCount.html)
[ISelectionManager::ClearSelections](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~ClearSelections.html)
[ISelectionManager::PaperSpaceSelectionEnabled Property ()](Interop.dsAutomation~Interop.dsAutomation.ISelectionManager~PaperSpaceSelectionEnabled.html)

## Availability

DraftSight V1R4.0
