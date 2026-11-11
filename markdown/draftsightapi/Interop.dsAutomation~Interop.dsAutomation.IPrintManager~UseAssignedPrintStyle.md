---
title: "UseAssignedPrintStyle Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "UseAssignedPrintStyle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UseAssignedPrintStyle.html"
---

# UseAssignedPrintStyle Property (IPrintManager)

Gets or sets whether PrintStyles applied to [Layers](Interop.dsAutomation~Interop.dsAutomation.ILayer.html) and entities are printed.

## Syntax

### Visual Basic

```vb
Property UseAssignedPrintStyle As System.Boolean
```

### C#

```csharp
System.bool UseAssignedPrintStyle {get; set;}
```

### JScript

```
function get,set UseAssignedPrintStyle : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_UseAssignedPrintStyle();
__property void set_UseAssignedPrintStyle(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool UseAssignedPrintStyle {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to print PrintStyles applied to Layers and entities, false to print entities in the [LineWeights assigned in the Layers](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~UseAssignedLineWeight.html)

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1.1
