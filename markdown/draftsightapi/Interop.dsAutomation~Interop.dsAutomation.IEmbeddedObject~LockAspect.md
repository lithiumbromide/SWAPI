---
title: "LockAspect Property (IEmbeddedObject)"
project: ""
interface: "IEmbeddedObject"
member: "LockAspect"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~LockAspect.html"
---

# LockAspect Property (IEmbeddedObject)

Gets or sets whether to lock the X/Y scaling of this embedded object.

## Syntax

### Visual Basic

```vb
Property LockAspect As System.Boolean
```

### C#

```csharp
System.bool LockAspect {get; set;}
```

### JScript

```
function get,set LockAspect : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_LockAspect();
__property void set_LockAspect(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool LockAspect {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to lock the X/Y scaling, false to not

## Remarks

If this property is true, then if you change [IEmbeddedObject::ScaleWidth](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~ScaleWidth.html), the [IEmbeddedObject::ScaleHeight](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject~ScaleHeight.html) automatically changes to preserve the aspect ratio.

## See Also

[IEmbeddedObject Interface](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject.html)
[IEmbeddedObject Members](Interop.dsAutomation~Interop.dsAutomation.IEmbeddedObject_members.html)

## Availability

DraftSight 2020 SP2
