---
title: "Justification Property (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "Justification"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Justification.html"
---

# Justification Property (IAttributeDefinition)

Gets or sets the position and alignment of the BlockAttribute definition's text in relation to the insertion point.

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

Position and alignment of the BlockAttribute definition's text in relation to the insertion point as defined in [dsTextJustification_e](Interop.dsAutomation~Interop.dsAutomation.dsTextJustification_e.html)

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::GetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetPosition.html)
[IAttributeDefinition::SetPosition Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetPosition.html)
[IAttributeDefinition::GetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetAlignmentPoint.html)
[IAttributeDefinition::SetAlignmentPoint Method](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetAlignmentPoint.html)

## Availability

DraftSight V1R2.0
