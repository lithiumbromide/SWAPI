---
title: "LineStyle Property (ISolid3D)"
project: ""
interface: "ISolid3D"
member: "LineStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid3D~LineStyle.html"
---

# LineStyle Property (ISolid3D)

Gets or sets the name of the [LineStyle](Interop.dsAutomation~Interop.dsAutomation.ILineStyle.html) for this 3D solid.

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

## Examples

See [Get Properties of Entity (COM native C++).](Get_Properties_of_Entity_CPPCOM.htm)

## See Also

[ISolid3D Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)
[ISolid3D Members](Interop.dsAutomation~Interop.dsAutomation.ISolid3D_members.html)

## Availability

DraftSight 2020 SP0
