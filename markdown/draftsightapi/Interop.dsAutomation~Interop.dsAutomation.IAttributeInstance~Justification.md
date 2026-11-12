---
title: "Justification Property (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "Justification"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Justification.html"
---

# Justification Property (IAttributeInstance)

Gets or sets the position and alignment of the BlockAttribute instance's text in relation to the insertion point.

## Syntax

### Visual Basic

```vb
Property Justification As dsTextJustification_e
```

### C#

```csharp
dsTextJustification_e Justification {get; set;}
```

### JScript

```
function get,set Justification : dsTextJustification_e
```

### Managed Extensions for C++

```
__property dsTextJustification_e get_Justification();
__property void set_Justification(
   dsTextJustification_e value
);
```

### C++/CLI

```cpp
property dsTextJustification_e Justification {
   dsTextJustification_e get();
   void set (    dsTextJustification_e value);
}
```

### Property Value

Position and alignment of the BlockAttribute instance's text in relation to the insertion point as defined in [dsTextJustification_e](Interop.dsAutomation~Interop.dsAutomation.dsTextJustification_e.html)

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)
[IAttributeInstance::GetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetPosition.html)
[IAttributeInstance::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetPosition.html)
[IAttributeInstance::GetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~GetAlignmentPoint.html)
[IAttriubteInstance::SetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~SetAlignmentPoint.html)

## Availability

DraftSight V1R2.0
