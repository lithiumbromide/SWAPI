---
title: "Erased Property (IArcAlignedText)"
project: ""
interface: "IArcAlignedText"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText~Erased.html"
---

# Erased Property (IArcAlignedText)

Gets or sets whether to erase or restore the curved text.

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

True to erase the curved text, false to restore it (see **Remarks**)

## Remarks

| If this property is set to true... | Then the curved text... |
| --- | --- |
| and the drawing remains open | is not displayed and can be restored by setting this property to false. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

## See Also

[IArcAlignedText Interface](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText.html)
[IArcAlignedText Members](Interop.dsAutomation~Interop.dsAutomation.IArcAlignedText_members.html)

## Availability

DraftSight 2018 SP2
