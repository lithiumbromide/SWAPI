---
title: "Erased Property (IDictionary)"
project: ""
interface: "IDictionary"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDictionary~Erased.html"
---

# Erased Property (IDictionary)

Gets or sets whether to erase or restore a dictionary.

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

True to erase the dictionary and its entity association from the dictionary in which they exist, false to restore the dictionary to the dictionary in which it previously existed (see **Remarks**)

## Remarks

A dictionary does not have to be empty to be erased. Dictionary entries in the erased dictionary do not change.

| If this property is set to true... | Then the dictionary... |
| --- | --- |
| and the drawing remains open | can be restored by setting this property to false and calling IDictionary::SetEntry . NOTE : When a dictionary is erased, its entry and entity association are removed from the dictionary in which it existed. When an erased dictionary is restored, its entry and entity association in the dictionary in which it previously existed are not restored. You must call IDictionary::SetEntry to add the restored entry and entity association to the dictionary in which they previously existed. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

You can also use [IDictionary::RemoveEntry](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html) to remove a dictionary from the dictionary in which it exists. You do not have to call IDictionary::SetEntry to restore a removed dictionary to the dictionary in which it previously existed if the removed dictionary was removed by IDictionary::RemoveEntry.

## See Also

[IDictionary Interface](Interop.dsAutomation~Interop.dsAutomation.IDictionary.html)
[IDictionary Members](Interop.dsAutomation~Interop.dsAutomation.IDictionary_members.html)

## Availability

DraftSight V1R4.0
