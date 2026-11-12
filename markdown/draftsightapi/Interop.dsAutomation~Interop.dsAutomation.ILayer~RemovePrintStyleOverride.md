---
title: "RemovePrintStyleOverride Method (ILayer)"
project: ""
interface: "ILayer"
member: "RemovePrintStyleOverride"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverride.html"
---

# RemovePrintStyleOverride Method (ILayer)

Removes the PrintStyle override from this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub RemovePrintStyleOverride( _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void RemovePrintStyleOverride(
   Viewport Viewport
)
```

### JScript

```
function RemovePrintStyleOverride(
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void RemovePrintStyleOverride(
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void RemovePrintStyleOverride(
   Viewport^ Viewport
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html) from which to remove the PrintStyle override for this Layer

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverrides.html)
[ILayer::GetPrintStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetPrintStyleInViewport.html)
[ILayer::SetPrintStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetPrintStyleInViewport.html)
[ILayer::PrintStyle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~PrintStyle.html)
[ILayerManager::RemoveAllOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveAllOverrides.html)
[ILayerManager::RemovePrintStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverride.html)
[ILayerManager::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemovePrintStyleOverrides.html)
[ILayerManager::RemoveViewportOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayerManager~RemoveViewportOverrides.html)

## Availability

DraftSight V1R6.0
