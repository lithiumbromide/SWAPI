---
title: "RemoveLineWeightOverride Method (ILayer)"
project: ""
interface: "ILayer"
member: "RemoveLineWeightOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverride.html"
---

# RemoveLineWeightOverride Method (ILayer)

Removes the LineWeight override from this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveLineWeightOverride( _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveLineWeightOverride(
   Viewport Viewport
)
```

### JScript

```
function RemoveLineWeightOverride(
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveLineWeightOverride(
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveLineWeightOverride(
   Viewport^ Viewport
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html) from which to remove the LineWeight override for this Layer

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::RemoveLineWeightOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineWeightOverrides.html)
[ILayer::GetLineWeightInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetLineWeightInViewport.html)
[ILayer::LineWeight Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~LineWeight.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveColorOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverride.html)
[ILayerManager::RemoveColorOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveColorOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
