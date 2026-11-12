---
title: "AutoHide Property (ICustomPropertyControl)"
project: ""
interface: "ICustomPropertyControl"
member: "AutoHide"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl~AutoHide.html"
---

# AutoHide Property (ICustomPropertyControl)

Gets or sets whether to hide the docking pane.

## Syntax

### Visual Basic

```vb
Property AutoHide As System.Boolean
```

### C#

```csharp
System.bool AutoHide {get; set;}
```

### JScript

```
function get,set AutoHide : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_AutoHide();
__property void set_AutoHide(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool AutoHide {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to hide the docking pane, false to not

## Remarks

This property only works after DraftSight is launched.

## See Also

[ICustomPropertyControl Interface](Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl.html)
[ICustomPropertyControl Members](Interop.dsAutomation~Interop.dsAutomation.ICustomPropertyControl_members.html)

## Availability

DraftSight 2023 SP0
