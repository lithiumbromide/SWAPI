---
title: "Revolution Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "Revolution"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Revolution.html"
---

# Revolution Property (ISpring)

Gets or sets the number of revolutions for the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property Revolution As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.Revolution = value

value = instance.Revolution
```

### C#

```csharp
System.double Revolution {get; set;}
```

### C++/CLI

```cpp
property System.double Revolution {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of revolutions

## VBA Syntax

See [Spring::Revolution](ms-its:sldworksapivb6.chm::/sldworks~Spring~Revolution.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::EndingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingPitch.html)
[ISpring::EndingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingRevolution.html)
[ISpring::Height Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Height.html)
[ISpring::Pitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Pitch.html)
[ISpring::StartingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingPitch.html)
[ISpring::StartingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingRevolution.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
