---
title: "UseAssignedLineWeight Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "UseAssignedLineWeight"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UseAssignedLineWeight.html"
---

# UseAssignedLineWeight Property (IPrintManager)

Gets or sets whether to print entities in the LineWeights assigned in the [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html).

## Syntax

### Visual Basic

```vb
Property UseAssignedLineWeight As System.Boolean
```

### C#

```csharp
System.bool UseAssignedLineWeight {get; set;}
```

### JScript

```
function get,set UseAssignedLineWeight : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_UseAssignedLineWeight();
__property void set_UseAssignedLineWeight(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool UseAssignedLineWeight {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to print entities in the LineWeights assigned in the Layers, false to [use assigned PrintStyles](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UseAssignedPrintStyle.html)

## Remarks

This property is only available if [IPrintManager::UseAssignedPrintStyle](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UseAssignedPrintStyle.html) is false.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1.1
