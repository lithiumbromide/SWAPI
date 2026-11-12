---
title: "SetPrintStyleInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "SetPrintStyleInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~SetPrintStyleInViewport.html"
---

# SetPrintStyleInViewport Method (ILayer)

Sets the name of the PrintStyle for this Layer in the specified Viewport.

## Syntax

### Visual Basic

```vb
Sub SetPrintStyleInViewport( _
   ByVal PrintStyle As System.String, _
   ByVal Viewport As Viewport _
)
```

### C#

```csharp
void SetPrintStyleInViewport(
   System.string PrintStyle,
   Viewport Viewport
)
```

### JScript

```
function SetPrintStyleInViewport(
   PrintStyle : System.String,
   Viewport : Viewport
);
```

### Managed Extensions for C++

```
void SetPrintStyleInViewport(
   System.string* PrintStyle,
   Viewport* Viewport
)
```

### C++/CLI

```cpp
void SetPrintStyleInViewport(
   System.String^ PrintStyle,
   Viewport^ Viewport
)
```

### Parameters

- `PrintStyle`: Name of the PrintStyle
- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::GetPrintStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~GetPrintStyleInViewport.html)
[ILayer::RemovePrintStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverride.html)
[ILayer::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverrides.html)
[ILayer::PrintStyle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~PrintStyle.html)

## Availability

DraftSight V1R6.0
