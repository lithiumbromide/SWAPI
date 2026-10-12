---
title: "Pitch Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "Pitch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Pitch.html"
---

# Pitch Property (ISpring)

Gets or sets the pitch of the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property Pitch As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.Pitch = value

value = instance.Pitch
```

### C#

```csharp
System.double Pitch {get; set;}
```

### C++/CLI

```cpp
property System.double Pitch {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pitch

## VBA Syntax

See [Spring::Pitch](ms-its:sldworksapivb6.chm::/sldworks~Spring~Pitch.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::StartingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingRevolution.html)
[ISpring::StartingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingPitch.html)
[ISpring::Revolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Revolution.html)
[ISpring::Height Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Height.html)
[ISpring::EndingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingRevolution.html)
[ISpring::EndingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingPitch.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
