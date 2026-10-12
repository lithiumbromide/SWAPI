---
title: "OpenSystem2 Property (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "OpenSystem2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~OpenSystem2.html"
---

# OpenSystem2 Property (ICWRadiation)

Gets or sets whether to consider radiation to the ambient (open system).

## Syntax

### Visual Basic (Declaration)

```vb
Property OpenSystem2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
Dim value As System.Boolean

instance.OpenSystem2 = value

value = instance.OpenSystem2
```

### C#

```csharp
System.bool OpenSystem2 {get; set;}
```

### C++/CLI

```cpp
property System.bool OpenSystem2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to consider radiation to the ambient (open system), 0 or false to ignore radiation to the ambient (closed system)

## Examples

See the [ICWRadiation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
