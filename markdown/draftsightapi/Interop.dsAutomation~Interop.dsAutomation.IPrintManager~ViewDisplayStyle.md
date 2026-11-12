---
title: "ViewDisplayStyle Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "ViewDisplayStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~ViewDisplayStyle.html"
---

# ViewDisplayStyle Property (IPrintManager)

Gets or sets the display state for Shaded views when printing the Model view.

## Syntax

### Visual Basic

```vb
Property ViewDisplayStyle As dsViewDisplayStyle_e
```

### C#

```csharp
dsViewDisplayStyle_e ViewDisplayStyle {get; set;}
```

### JScript

```
function get,set ViewDisplayStyle : dsViewDisplayStyle_e
```

### Managed Extensions for C++

```
__property dsViewDisplayStyle_e get_ViewDisplayStyle();
__property void set_ViewDisplayStyle(
   dsViewDisplayStyle_e value
);
```

### C++/CLI

```cpp
property dsViewDisplayStyle_e ViewDisplayStyle {
   dsViewDisplayStyle_e get();
   void set (    dsViewDisplayStyle_e value);
}
```

### Property Value

Display state for Shaded model views as defined in [dsViewDisplayStyle_e](Interop.dsAutomation~Interop.dsAutomation.dsViewDisplayStyle_e.html)

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1
