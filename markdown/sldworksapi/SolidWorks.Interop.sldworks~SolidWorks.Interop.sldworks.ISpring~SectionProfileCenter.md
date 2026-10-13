---
title: "SectionProfileCenter Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "SectionProfileCenter"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter.html"
---

# SectionProfileCenter Property (ISpring)

Gets or sets the center point of the section profile of the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property SectionProfileCenter As MathPoint
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As MathPoint

instance.SectionProfileCenter = value

value = instance.SectionProfileCenter
```

### C#

```csharp
MathPoint SectionProfileCenter {get; set;}
```

### C++/CLI

```cpp
property MathPoint^ SectionProfileCenter {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Center point](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html)

## VBA Syntax

See [Spring::SectionProfileCenter](ms-its:sldworksapivb6.chm::/sldworks~Spring~SectionProfileCenter.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::BaseProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~BaseProfile.html)
[ISpring::GetProfilePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GetProfilePoints.html)
[ISpring::ProfileParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileParameters.html)
[ISpring::ProfileType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileType.html)
[ISpring::SectionProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
