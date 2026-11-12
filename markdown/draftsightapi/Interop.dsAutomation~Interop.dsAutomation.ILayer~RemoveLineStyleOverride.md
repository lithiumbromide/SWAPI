---
title: "RemoveLineStyleOverride Method (ILayer)"
project: ""
interface: "ILayer"
member: "RemoveLineStyleOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverride.html"
---

# RemoveLineStyleOverride Method (ILayer)

Removes the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) override from this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemoveLineStyleOverride( _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemoveLineStyleOverride(
   Viewport Viewport
)
```

### JScript

```
function RemoveLineStyleOverride(
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemoveLineStyleOverride(
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemoveLineStyleOverride(
   Viewport^ Viewport
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html) from which to remove the LineStyle override from this Layer

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverrides.html)
[ILayer::GetLineSyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetLineSyleInViewport.html)
[ILayer::SetLineStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetLineStyleInViewport.html)
[ILayer::LineStyle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~LineStyle.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemoveLineStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineStyleOverride.html)
[ILayerManager::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveLineStyleOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
