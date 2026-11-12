---
title: "InternalArcEnd Property (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "InternalArcEnd"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~InternalArcEnd.html"
---

# InternalArcEnd Property (IRichLineStyle)

Gets or sets whether to join the ends of the two line elements closest to the outer ones with an arc when there are four or more lines defining the [RichLine](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html) entity.

## Syntax

### Visual Basic

```vb
Property InternalArcEnd As System.Boolean
```

### C#

```csharp
System.bool InternalArcEnd {get; set;}
```

### JScript

```
function get,set InternalArcEnd : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_InternalArcEnd();
__property void set_InternalArcEnd(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool InternalArcEnd {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to join the ends of the two line elements closest to the outer ones with an arc when there are four or more lines defining the RichLine entity, false to not

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::InternalArcStart Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~InternalArcStart.html)
[IRichLineStyle::ExternalArcEnd Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~ExternalArcEnd.html)
[IRichLineStyle::ExternalArcStart Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~ExternalArcStart.html)
[IRichLineStyle::AngleEnd Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~AngleEnd.html)
[IRichLineStyle::AngleStart Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~AngleStart.html)
[IRichLineStyle::LineEnd Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~LineEnd.html)
[IRichLineStyle::LineStart Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~LineStart.html)

## Availability

DraftSight V1R1.3
