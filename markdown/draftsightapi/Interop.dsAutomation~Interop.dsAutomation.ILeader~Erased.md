---
title: "Erased Property (ILeader)"
project: ""
interface: "ILeader"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ILeader~Erased.html"
---

# Erased Property (ILeader)

Gets or sets whether to erase or restore the Leader.

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

True to erase the Leader, false to restore it (see **Remarks**)

## Remarks

| If this property is set to true... | Then the Leader... |
| --- | --- |
| and the drawing remains open | is not displayed and can be restored by setting this property to false. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

## See Also

[ILeader Interface](Interop.dsAutomation~Interop.dsAutomation.ILeader.html)
[ILeader Members](Interop.dsAutomation~Interop.dsAutomation.ILeader_members.html)

## Availability

DraftSight V1R1.2
