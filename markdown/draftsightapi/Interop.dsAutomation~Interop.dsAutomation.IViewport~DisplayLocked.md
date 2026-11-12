---
title: "DisplayLocked Property (IViewport)"
project: ""
interface: "IViewport"
member: "DisplayLocked"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IViewport~DisplayLocked.html"
---

# DisplayLocked Property (IViewport)

Gets or sets whether the Viewport is locked in model workspace.

## Syntax

### Visual Basic

```vb
Property DisplayLocked As System.Boolean
```

### C#

```csharp
System.bool DisplayLocked {get; set;}
```

### JScript

```
function get,set DisplayLocked : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_DisplayLocked();
__property void set_DisplayLocked(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool DisplayLocked {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the Viewport is locked in model workspace, false if the Viewport is not locked in model workspace

## Examples

[Create Rectangular Viewport (C#)](Create_Rectangular_Viewport_Example_CSharp.htm)
[Create Rectangular Viewport (VB.NET)](Create_Rectangular_Viewport_Example_VBNET.htm)
[Create Rectangular Viewport (VBA)](Create_Rectangular_Viewport_Example_VBA.htm)
[Create Rectangular Viewport (JavaScript)](Create_Rectangular_Viewport_Example_JS.htm)

## See Also

[IViewport Interface](Interop.dsAutomation~Interop.dsAutomation.IViewport.html)
[IViewport Members](Interop.dsAutomation~Interop.dsAutomation.IViewport_members.html)

## Availability

DraftSight V1R3.0
