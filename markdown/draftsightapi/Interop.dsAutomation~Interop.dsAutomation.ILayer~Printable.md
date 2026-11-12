---
title: "Printable Property (ILayer)"
project: ""
interface: "ILayer"
member: "Printable"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~Printable.html"
---

# Printable Property (ILayer)

Gets or sets whether the Layer can be printed.

## Syntax

### Visual Basic

```vb
Property Printable As System.Boolean
```

### C#

```csharp
System.bool Printable {get; set;}
```

### JScript

```
function get,set Printable : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Printable();
__property void set_Printable(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Printable {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the Layer can be printed, false if not

## Remarks

If you turn off printing for a Layer, the entities on the Layer are still displayed.

[Hidden](Interop.dsAutomation~Interop.dsAutomation.ILayer~Shown.html) or [frozen Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer~Frozen.html) are not printed regardless of the **Print** setting.

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)

## Availability

DraftSight V1R1.1
