---
title: "CCSPerViewport Property (IViewport)"
project: ""
interface: "IViewport"
member: "CCSPerViewport"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~CCSPerViewport.html"
---

# CCSPerViewport Property (IViewport)

Gets or sets whether the [custom coordinate system](Interop.dsAutomation~Interop.dsAutomation.ICustomCoordinateSystem.html) associated with this Viewport becomes active when the Viewport is [activated](Interop.dsAutomation~Interop.dsAutomation.IViewport~Active.html).

## Syntax

### Visual Basic

```vb
Property CCSPerViewport As System.Boolean
```

### C#

```csharp
System.bool CCSPerViewport {get; set;}
```

### JScript

```
function get,set CCSPerViewport : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_CCSPerViewport();
__property void set_CCSPerViewport(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool CCSPerViewport {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True only if the custom coordinate system associated with this Viewport becomes active when the Viewport is activated, false if not

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)

## Availability

DraftSight V1R3.0
