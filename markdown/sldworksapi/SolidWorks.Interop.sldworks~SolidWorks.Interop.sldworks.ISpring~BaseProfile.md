---
title: "BaseProfile Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "BaseProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~BaseProfile.html"
---

# BaseProfile Property (ISpring)

Gets or sets the base profile of the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property BaseProfile As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As Body2

instance.BaseProfile = value

value = instance.BaseProfile
```

### C#

```csharp
Body2 BaseProfile {get; set;}
```

### C++/CLI

```cpp
property Body2^ BaseProfile {
   Body2^ get();
   void set (    Body2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) (see **Remarks**)

## VBA Syntax

See [Spring::BaseProfile](ms-its:sldworksapivb6.chm::/sldworks~Spring~BaseProfile.html).

## Remarks

This body references an edge that sets the overall diameter of the spring. The profile of the coil (called a section profile) is swept around the radius of this circular edge.

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::GetProfilePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GetProfilePoints.html)
[ISpring::ProfileParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileParameters.html)
[ISpring::ProfileType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileType.html)
[ISpring::SectionProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile.html)
[ISpring::SectionProfileCenter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
