---
title: "WidthFactor Property (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "WidthFactor"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~WidthFactor.html"
---

# WidthFactor Property (IArcAlignedText)

Gets or sets the width factor of this curved text.

## Syntax

### Visual Basic

```vb
Property WidthFactor As System.Double
```

### C#

```csharp
System.double WidthFactor {get; set;}
```

### JScript

```
function get,set WidthFactor : System.double
```

### Managed Extensions for C++

```
__property System.double get_WidthFactor();
__property void set_WidthFactor(
   System.double value
);
```

### C++/CLI

```cpp
property System.double WidthFactor {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.1 <= width factor

## Remarks

The width factor is the aspect ratio that defines the width of characters in relation to their height.

## See Also

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)

## Availability

DraftSight 2018 SP2
