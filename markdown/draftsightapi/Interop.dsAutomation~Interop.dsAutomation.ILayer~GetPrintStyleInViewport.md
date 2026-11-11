---
title: "GetPrintStyleInViewport Method (ILayer)"
project: ""
interface: "ILayer"
member: "GetPrintStyleInViewport"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~GetPrintStyleInViewport.html"
---

# GetPrintStyleInViewport Method (ILayer)

Gets the name of the PrintStyle for this Layer in the specified Viewport and whether the PrintStyle is overridden in that Viewport.

## Syntax

### Visual Basic

```vb
Function GetPrintStyleInViewport( _
   ByVal Viewport As Viewport, _
   ByRef IsOverride As System.Boolean _
) As System.String
```

### C#

```csharp
System.string GetPrintStyleInViewport(
   Viewport Viewport,
   out System.bool IsOverride
)
```

### JScript

```
function GetPrintStyleInViewport(
   Viewport : Viewport,
   IsOverride : System.boolean
) : System.String;
```

### Managed Extensions for C++

```
System.string* GetPrintStyleInViewport(
   Viewport* Viewport,
   [PARAMFLAG::Out] System.bool IsOverride
)
```

### C++/CLI

```cpp
System.String^ GetPrintStyleInViewport(
   Viewport^ Viewport,
   [Out] System.bool IsOverride
)
```

### Parameters

- `Viewport`: [Viewport](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
- `IsOverride`: True if the PrintStyle for the Layer in the specified Viewport is overridden, false if not

### Return Value

Name of the PrintStyle

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::SetPrintStyleInViewport Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~SetPrintStyleInViewport.html)
[ILayer::RemovePrintStyleOverride Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverride.html)
[ILayer::RemovePrintStyleOverrides Method ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~RemovePrintStyleOverrides.html)
[ILayer::PrintStyle Property ()](Interop.dsAutomation~Interop.dsAutomation.ILayer~PrintStyle.html)

## Availability

DraftSight V1R6.0
