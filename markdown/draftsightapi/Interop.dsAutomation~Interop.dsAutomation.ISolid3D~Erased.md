---
title: "Erased Property (ISolid3D)"
project: ""
interface: "ISolid3D"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolid3D~Erased.html"
---

# Erased Property (ISolid3D)

Gets or sets whether to erase or restore this 3D solid.

## Syntax

### Visual Basic

```vb
Property Erased As System.Boolean
```

### C#

```csharp
System.bool Erased {get; set;}
```

### JScript

```
function get,set Erased : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_Erased();
__property void set_Erased(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool Erased {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to erase this 3D solid, false to restore it (see **Remarks**)

## Remarks

| If this property is set to true... | Then the 3D solid... |
| --- | --- |
| and the drawing remains open | is not displayed and can be restored by setting this property to false. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

## See Also

[ISolid3D Interface](Interop.dsAutomation~Interop.dsAutomation.ISolid3D.html)
[ISolid3D Members](Interop.dsAutomation~Interop.dsAutomation.ISolid3D_members.html)

## Availability

DraftSight 2020 SP0
