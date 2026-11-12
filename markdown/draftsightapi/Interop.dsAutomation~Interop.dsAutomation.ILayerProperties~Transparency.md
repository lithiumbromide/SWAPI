---
title: "Transparency Property (ILayerProperties)"
project: ""
interface: "ILayerProperties"
member: "Transparency"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILayerProperties~Transparency.html"
---

# Transparency Property (ILayerProperties)

Gets or sets the transparency of this Layer.

## Syntax

### Visual Basic

```vb
Property Transparency As System.Integer
```

### C#

```csharp
System.int Transparency {get; set;}
```

### JScript

```
function get,set Transparency : System.int
```

### Managed Extensions for C++

```
__property System.int get_Transparency();
__property void set_Transparency(
   System.int value
);
```

### C++/CLI

```cpp
property System.int Transparency {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 (opaque) < Transparency percentage < 90

## See Also

[ILayerProperties Interface](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties.html)
[ILayerProperties Members](Interop.dsAutomation~Interop.dsAutomation.ILayerProperties_members.html)

## Availability

DraftSight 2018 SP0
