---
title: "Brightness Property (IReferenceImage)"
project: ""
interface: "IReferenceImage"
member: "Brightness"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IReferenceImage~Brightness.html"
---

# Brightness Property (IReferenceImage)

Gets or sets the brightness of light emitted by this Referenced image.

## Syntax

### Visual Basic

```vb
Property Brightness As System.Integer
```

### C#

```csharp
System.int Brightness {get; set;}
```

### JScript

```
function get,set Brightness : System.int
```

### Managed Extensions for C++

```
__property System.int get_Brightness();
__property void set_Brightness(
   System.int value
);
```

### C++/CLI

```cpp
property System.int Brightness {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Value between 0.00 and the maximum value which your system supports (0.00-maximum float, 1.0000 by default)

## See Also

[IReferenceImage Interface](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage.html)
[IReferenceImage Members](Interop.dsAutomation~Interop.dsAutomation.IReferenceImage_members.html)

## Availability

DraftSight V1R1.4
