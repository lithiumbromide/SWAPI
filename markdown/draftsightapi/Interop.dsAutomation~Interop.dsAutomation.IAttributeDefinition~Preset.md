---
title: "Preset Property (IAttributeDefinition)"
project: ""
interface: "IAttributeDefinition"
member: "Preset"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition~Preset.html"
---

# Preset Property (IAttributeDefinition)

Gets or sets whether you can create BlockAttributes that accept their default values.

## Syntax

### Visual Basic

```vb
Property Preset As System.Boolean
```

### C#

```csharp
System.bool Preset {get; set;}
```

### JScript

```
function get,set Preset : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Preset();
__property void set_Preset(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Preset {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if you can create BlockAttributes that accept their default values, false if not

## Remarks

If this property is true, then values are not requested when BlockAttributes are selected. However, you can edit BlockAttribute values after insertion.

## See Also

[IAttributeDefinition Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition.html)
[IAttributeDefinition Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeDefinition_members.html)

## Availability

DraftSight V1R2.0
