---
title: "EndingRevolution Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "EndingRevolution"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingRevolution.html"
---

# EndingRevolution Property (ISpring)

Gets or sets the number of revolutions for the end section of a compression spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndingRevolution As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.EndingRevolution = value

value = instance.EndingRevolution
```

### C#

```csharp
System.double EndingRevolution {get; set;}
```

### C++/CLI

```cpp
property System.double EndingRevolution {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of revolutions for the end section

## VBA Syntax

See [Spring::EndingRevolution](ms-its:sldworksapivb6.chm::/sldworks~Spring~EndingRevolution.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::StartingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingRevolution.html)
[ISpring::StartingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingPitch.html)
[ISpring::Revolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Revolution.html)
[ISpring::Pitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Pitch.html)
[ISpring::Height Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Height.html)
[ISpring::EndingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingPitch.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
