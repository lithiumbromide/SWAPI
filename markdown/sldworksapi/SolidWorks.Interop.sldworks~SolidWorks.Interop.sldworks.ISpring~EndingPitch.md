---
title: "EndingPitch Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "EndingPitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingPitch.html"
---

# EndingPitch Property (ISpring)

Gets or sets pitch of the end section of a compression spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndingPitch As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.EndingPitch = value

value = instance.EndingPitch
```

### C#

```csharp
System.double EndingPitch {get; set;}
```

### C++/CLI

```cpp
property System.double EndingPitch {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pitch of the end section

## VBA Syntax

See [Spring::EndingPitch](ms-its:sldworksapivb6.chm::/sldworks~Spring~EndingPitch.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::EndingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingRevolution.html)
[ISpring::Height Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Height.html)
[ISpring::Pitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Pitch.html)
[ISpring::Revolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Revolution.html)
[ISpring::StartingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingPitch.html)
[ISpring::StartingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingRevolution.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
