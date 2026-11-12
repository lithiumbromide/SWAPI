---
title: "Quality Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "Quality"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~Quality.html"
---

# Quality Property (IPrintManager)

Gets or sets print quality.

## Syntax

### Visual Basic

```vb
Property Quality As System.Integer
```

### C#

```csharp
System.int Quality {get; set;}
```

### JScript

```
function get,set Quality : System.int
```

### Managed Extensions for C++

```
__property System.int get_Quality();
__property void set_Quality(
   System.int value
);
```

### C++/CLI

```cpp
property System.int Quality {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Print quality as defined in [dsStandardPrintQuality_e](Interop.dsAutomation~Interop.dsAutomation.dsStandardPrintQuality_e.html)

## Examples

See the [IPrintManager](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html) examples.

## Remarks

Available settings for print quality are dependent on the specified [printer](Interop.dsAutomation~Interop.dsAutomation.IPrintManager~Printer.html).

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1
