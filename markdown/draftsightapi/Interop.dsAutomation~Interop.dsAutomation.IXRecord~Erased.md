---
title: "Erased Property (IXRecord)"
project: ""
interface: "IXRecord"
member: "Erased"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IXRecord~Erased.html"
---

# Erased Property (IXRecord)

Gets or sets whether to erase or restore an XRecord.

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

True to erase the XRecord from the dictionary, false to restore it (see **Remarks**)

## Remarks

| If this property is set to true... | Then the XRecord... |
| --- | --- |
| and the drawing remains open | can be restored by setting this property to false and calling IDictionary::SetEntry . NOTE : When an XRecord is erased, its entry is removed from the dictionary in which it existed. Restoring an erased XRecord does not add the XRecord's entry to the dictionary in which it previously existed. You must call IDictionary::SetEntry to add the restored XRecord to the dictionary in which it previously existed. |
| when the drawing is closed | is deleted from the drawing and cannot be restored. |

**NOTE**: You can also remove XRecords in a dictionary using [IDictionary::RemoveEntry](Interop.dsAutomation~Interop.dsAutomation.IDictionary~RemoveEntry.html). You do not have to call IDictionary::SetEntry to restore XRecords that were removed by IDictionary::RemoveEntry.

## See Also

[IXRecord Interface](Interop.dsAutomation~Interop.dsAutomation.IXRecord.html)
[IXRecord Members](Interop.dsAutomation~Interop.dsAutomation.IXRecord_members.html)

## Availability

DraftSight V1R4.0
