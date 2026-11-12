---
title: "StartingRevolution Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "StartingRevolution"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingRevolution.html"
---

# StartingRevolution Property (ISpring)

Gets or sets the number of revolutions for the starting section of a compression spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartingRevolution As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.StartingRevolution = value

value = instance.StartingRevolution
```

### C#

```csharp
System.double StartingRevolution {get; set;}
```

### C++/CLI

```cpp
property System.double StartingRevolution {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of revolutions for the starting section

## VBA Syntax

See [Spring::StartingRevolution](ms-its:sldworksapivb6.chm::/sldworks~Spring~StartingRevolution.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::EndingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingPitch.html)
[ISpring::EndingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingRevolution.html)
[ISpring::Height Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Height.html)
[ISpring::Pitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Pitch.html)
[ISpring::Revolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Revolution.html)
[ISpring::StartingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingPitch.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
