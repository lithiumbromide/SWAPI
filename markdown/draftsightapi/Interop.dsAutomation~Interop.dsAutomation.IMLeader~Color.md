---
title: "Color Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "Color"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~Color.html"
---

# Color Property (IMLeader)

Gets or sets the general color setting for the text and leader of this MLeader.

## Syntax

### Visual Basic

```vb
Property Color As Color
```

### C#

```csharp
Color Color {get; set;}
```

### JScript

```
function get,set Color : Color
```

### Managed Extensions for C++

```
__property Color* get_Color();
__property void set_Color(
   Color* value
);
```

### C++/CLI

```cpp
property Color^ Color {
   Color^ get();
   void set (    Color^ value);
}
```

### Property Value

[IColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Remarks

This property may be overridden by [IMLeader::LeaderLineColor](Interop.dsAutomation~Interop.dsAutomation.IMLeader~LeaderLineColor.html).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
