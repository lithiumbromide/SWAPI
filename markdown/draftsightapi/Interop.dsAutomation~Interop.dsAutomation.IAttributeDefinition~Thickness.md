---
title: "Thickness Property (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "Thickness"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Thickness.html"
---

# Thickness Property (IAttributeDefinition)

Gets or sets the thickness of this BlockAttribute definition.

## Syntax

### Visual Basic

```vb
Property Thickness As System.Double
```

### C#

```csharp
System.double Thickness {get; set;}
```

### JScript

```
function get,set Thickness : System.double
```

### Managed Extensions for C++

```
__property System.double get_Thickness();
__property void set_Thickness(
   System.double value
);
```

### C++/CLI

```cpp
property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Thickness; 0 for no thickness, a positive value for an upward extrusion, a negative value for a downward extrusion (see **Remarks**)

## Remarks

Thickness is the extrusion depth along the [vector normal](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~GetNormal.html) to this entity.

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)
[IAttributeDefinition::SetNormal Method ()](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~SetNormal.html)

## Availability

DraftSight V1R1.4
