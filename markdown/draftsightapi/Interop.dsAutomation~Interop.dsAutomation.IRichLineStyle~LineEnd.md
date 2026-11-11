---
title: "LineEnd Property (IRichLineStyle)"
project: ""
interface: "IRichLineStyle"
member: "LineEnd"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~LineEnd.html"
---

# LineEnd Property (IRichLineStyle)

Gets or sets whether to cap the end of a [RichLine](Interop.dsAutomation~Interop.dsAutomation.IRichLine.html) entity with a line segment.

## Syntax

### Visual Basic

```vb
Property LineEnd As System.Boolean
```

### C#

```csharp
System.bool LineEnd {get; set;}
```

### JScript

```
function get,set LineEnd : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_LineEnd();
__property void set_LineEnd(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool LineEnd {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to cap the end of a RichLine entity with a line segment, false to not

## See Also

[IRichLineStyle Interface](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle.html)
[IRichLineStyle Members](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle_members.html)
[IRichLineStyle::LineStart Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~LineStart.html)
[IRichLineStyle::InternalArcEnd Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~InternalArcEnd.html)
[IRichLineStyle::InternalArcStart Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~InternalArcStart.html)
[IRichLineStyle::ExternalArcEnd Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~ExternalArcEnd.html)
[IRichLineStyle::ExternalArcStart Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~ExternalArcStart.html)
[IRichLineStyle::AngleEnd Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~AngleEnd.html)
[IRichLineStyle::AngleStart Property](Interop.dsAutomation~Interop.dsAutomation.IRichLineStyle~AngleStart.html)

## Availability

DraftSight V1R1.3
