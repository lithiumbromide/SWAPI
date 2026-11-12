---
title: "Height Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "Height"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Height.html"
---

# Height Property (ISpring)

Gets or sets the height of the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property Height As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Double

instance.Height = value

value = instance.Height
```

### C#

```csharp
System.double Height {get; set;}
```

### C++/CLI

```cpp
property System.double Height {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Height

## VBA Syntax

See [Spring::Height](ms-its:sldworksapivb6.chm::/sldworks~Spring~Height.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::EndingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingPitch.html)
[ISpring::EndingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingRevolution.html)
[ISpring::Pitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Pitch.html)
[ISpring::Revolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Revolution.html)
[ISpring::StartingPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingPitch.html)
[ISpring::StartingRevolution Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingRevolution.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
