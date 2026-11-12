---
title: "PrintInBackground Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "PrintInBackground"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PrintInBackground.html"
---

# PrintInBackground Property (IPrintManager)

Gets or sets whether to print the drawing in the background.

## Syntax

### Visual Basic

```vb
Property PrintInBackground As System.Boolean
```

### C#

```csharp
System.bool PrintInBackground {get; set;}
```

### JScript

```
function get,set PrintInBackground : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_PrintInBackground();
__property void set_PrintInBackground(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool PrintInBackground {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to print the drawing in the background, false to print the drawing in the foreground (see **Remarks**)

## Remarks

If this property is set to true, then you can continue to work in a drawing while the drawing is printing; otherwise, you must wait for the drawing to print before you can resume working on it.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1.1
