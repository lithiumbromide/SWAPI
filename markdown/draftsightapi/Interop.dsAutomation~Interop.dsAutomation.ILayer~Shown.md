---
title: "Shown Property (ILayer)"
project: ""
interface: "ILayer"
member: "Shown"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayer~Shown.html"
---

# Shown Property (ILayer)

Gets or sets whether the Layer is shown or hidden.

## Syntax

### Visual Basic

```vb
Property Shown As System.Boolean
```

### C#

```csharp
System.bool Shown {get; set;}
```

### JScript

```
function get,set Shown : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Shown();
__property void set_Shown(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Shown {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if the Layer is shown, false if hidden

## Remarks

When a Layer is shown, the entities on it are visible. Entities on hidden Layers are not visible.

## See Also

[ILayer Interface](Interop.dsAutomation~Interop.dsAutomation.ILayer.html)
[ILayer Members](Interop.dsAutomation~Interop.dsAutomation.ILayer_members.html)
[ILayer::Frozen Property](Interop.dsAutomation~Interop.dsAutomation.ILayer~Frozen.html)

## Availability

DraftSight V1R1.1
