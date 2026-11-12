---
title: "SetLineStyleInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "SetLineStyleInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~SetLineStyleInViewport.html"
---

# SetLineStyleInViewport Method (ILayer)

Sets the name of the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) for this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub SetLineStyleInViewport( _
   ByVal LineStyle As System.String, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void SetLineStyleInViewport(
   System.string LineStyle,
   Viewport Viewport
)
```

### JScript

```
function SetLineStyleInViewport(
   LineStyle : System.String,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void SetLineStyleInViewport(
   System.string* LineStyle,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void SetLineStyleInViewport(
   System.String^ LineStyle,
   Viewport^ Viewport
)
```

### Parameters

- `LineStyle`: Name of the LineStyle
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetLineSyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetLineSyleInViewport.html)
[ILayer::RemoveLineStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverride.html)
[ILayer::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverrides.html)
[ILayer::LineStyle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~LineStyle.html)

## Availability

DraftSight V1R6.0
