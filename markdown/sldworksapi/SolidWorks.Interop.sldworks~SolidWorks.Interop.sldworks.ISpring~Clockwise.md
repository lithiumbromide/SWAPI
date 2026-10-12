---
title: "Clockwise Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "Clockwise"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Clockwise.html"
---

# Clockwise Property (ISpring)

Gets or sets the direction of the coils of the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property Clockwise As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Boolean

instance.Clockwise = value

value = instance.Clockwise
```

### C#

```csharp
System.bool Clockwise {get; set;}
```

### C++/CLI

```cpp
property System.bool Clockwise {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to set the direction of the coils of the spring clockwise, false to set their direction counter-clockwise

## VBA Syntax

See [Spring::Clockwise](ms-its:sldworksapivb6.chm::/sldworks~Spring~Clockwise.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
