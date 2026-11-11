---
title: "GetLineSyleInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "GetLineSyleInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~GetLineSyleInViewport.html"
---

# GetLineSyleInViewport Method (ILayer)

Gets the name of the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) for this Layer in the specified Viewport and whether the LineStyle is overridden in that Viewport.

## Syntax

### Visual Basic

```vb
Function GetLineSyleInViewport( _
   ByVal Viewport As Viewport, _
   ByRef IsOverride As System.Boolean _
) As System.String
```

### C#

```csharp
System.string GetLineSyleInViewport(
   Viewport Viewport,
   out System.bool IsOverride
)
```

### JScript

```
function GetLineSyleInViewport(
   Viewport : Viewport,
   IsOverride : System.boolean
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetLineSyleInViewport(
   Viewport* Viewport,
   [PARAMFLAG::Out] System.bool IsOverride
)
```

### C++/CLI

```cpp
System.String^ GetLineSyleInViewport(
   Viewport^ Viewport,
   [Out] System.bool IsOverride
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
- `IsOverride`: True if the LineStyle for this Layer is overridden in the specified Viewport, false if not

### Return Value

Name of LineStyle

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::SetLineStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetLineStyleInViewport.html)
[ILayer::LineStyle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~LineStyle.html)
[ILayer::RemoveLineStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverride.html)
[ILayer::RemoveLineStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemoveLineStyleOverrides.html)

## Availability

DraftSight V1R6.0
