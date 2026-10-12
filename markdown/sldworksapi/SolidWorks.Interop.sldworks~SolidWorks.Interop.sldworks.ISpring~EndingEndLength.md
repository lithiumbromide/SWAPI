---
title: "EndingEndLength Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "EndingEndLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndLength.html"
---

# EndingEndLength Property (ISpring)

Gets or sets the ending end length of a torsion spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndingEndLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.EndingEndLength = value

value = instance.EndingEndLength
```

### C#

```csharp
System.double EndingEndLength {get; set;}
```

### C++/CLI

```cpp
property System.double EndingEndLength {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Ending end length

## VBA Syntax

See [Spring::EndingEndLength](ms-its:sldworksapivb6.chm::/sldworks~Spring~EndingEndLength.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::EndingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndType.html)
[ISpring::StartingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndLength.html)
[ISpring::StartingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndType.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
