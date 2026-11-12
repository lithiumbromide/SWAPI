---
title: "LineStyle Property (IMLeader)"
project: ""
interface: "IMLeader"
member: "LineStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IMLeader~LineStyle.html"
---

# LineStyle Property (IMLeader)

Gets or sets the name of the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) for the text and leader of this MLeader.

## Syntax

### Visual Basic

```vb
Property LineStyle As System.String
```

### C#

```csharp
System.string LineStyle {get; set;}
```

### JScript

```
function get,set LineStyle : System.String
```

### Managed Extensions for C++

```
__property System.string* get_LineStyle();
__property void set_LineStyle(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ LineStyle {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the LineStyle

## Remarks

This property may be overridden by [IMLeader::LeaderLineStyle](Interop.dsAutomation~Interop.dsAutomation.IMLeader~LeaderLineStyle.html).

## See Also

[IMLeader Interface](Interop.dsAutomation~Interop.dsAutomation.IMLeader.html)
[IMLeader Members](Interop.dsAutomation~Interop.dsAutomation.IMLeader_members.html)

## Availability

DraftSight 2024 SP4
