---
title: "StartingEndLength Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "StartingEndLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndLength.html"
---

# StartingEndLength Property (ISpring)

Gets or sets the starting end length of a torsion spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartingEndLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.StartingEndLength = value

value = instance.StartingEndLength
```

### C#

```csharp
System.double StartingEndLength {get; set;}
```

### C++/CLI

```cpp
property System.double StartingEndLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Starting end length

## VBA Syntax

See [Spring::StartingEndLength](ms-its:sldworksapivb6.chm::/sldworks~Spring~StartingEndLength.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::EndingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndLength.html)
[ISpring::EndingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndType.html)
[ISpring::StartingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndType.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
