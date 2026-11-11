---
title: "Erased Property (ISolidBackground)"
project: ""
interface: "ISolidBackground"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISolidBackground~Erased.html"
---

# Erased Property (ISolidBackground)

Gets or sets whether to erase or restore the solid background.

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

True to erase the solid background, false to restore it (see **Remarks**)

## Remarks

| If this property is set to true... | Then the solid background... |
| --- | --- |
| and the drawing remains open | is not displayed and can be restored by setting this property to false. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

## See Also

[ISolidBackground Interface](Interop.dsAutomation~Interop.dsAutomation.ISolidBackground.html)
[ISolidBackground Members](Interop.dsAutomation~Interop.dsAutomation.ISolidBackground_members.html)

## Availability

DraftSight V1R5.0
