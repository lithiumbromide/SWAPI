---
title: "StartingPitch Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "StartingPitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingPitch.html"
---

# StartingPitch Property (ISpring)

Gets the pitch of the starting section of a compression spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property StartingPitch As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.StartingPitch = value

value = instance.StartingPitch
```

### C#

```csharp
System.double StartingPitch {get; set;}
```

### C++/CLI

```cpp
property System.double StartingPitch {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pitch of the starting section

## VBA Syntax

See [Spring::StartingPitch](ms-its:sldworksapivb6.chm::/sldworks~Spring~StartingPitch.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::EndingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingPitch.html)
[ISpring::EndingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingRevolution.html)
[ISpring::Height Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Height.html)
[ISpring::Pitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Pitch.html)
[ISpring::Revolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Revolution.html)
[ISpring::StartingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingRevolution.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
