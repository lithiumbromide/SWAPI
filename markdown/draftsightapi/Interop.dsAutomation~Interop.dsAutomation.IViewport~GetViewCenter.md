---
title: "GetViewCenter Method (IViewport)"
project: ""
interface: "IViewport"
member: "GetViewCenter"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~GetViewCenter.html"
---

# GetViewCenter Method (IViewport)

Gets the center coordinates of the view or perspective in this activated Viewport.

## Syntax

### Visual Basic

```vb
Sub GetViewCenter( _
   ByRef X As System.Double, _
   ByRef Y As System.Double _
)
```

### C#

```csharp
void GetViewCenter(
   out System.double X,
   out System.double Y
)
```

### JScript

```
function GetViewCenter(
   X : System.double,
   Y : System.double
);
```

### Managed Extensions for C++

```
void GetViewCenter(
   [PARAMFLAG::Out] System.double X,
   [PARAMFLAG::Out] System.double Y
)
```

### C++/CLI

```cpp
void GetViewCenter(
   [Out] System.double X,
   [Out] System.double Y
)
```

### Parameters

- `X`: x coordinate of the view or perspective center
- `Y`: y coordinate of the view or perspective center

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)
[IViewport::GetCenter Method ()](Interop.dsAutomation~Interop.dsAutomation.IViewport~GetCenter.html)
[IViewport::ViewHeight Property ()](Interop.dsAutomation~Interop.dsAutomation.IViewport~ViewHeight.html)
[IViewport::Active Property ()](Interop.dsAutomation~Interop.dsAutomation.IViewport~Active.html)

## Availability

DraftSight 2017 SP1
