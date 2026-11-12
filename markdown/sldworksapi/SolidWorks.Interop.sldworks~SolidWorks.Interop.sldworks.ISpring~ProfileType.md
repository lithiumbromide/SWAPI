---
title: "ProfileType Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "ProfileType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileType.html"
---

# ProfileType Property (ISpring)

Gets or sets the section profile type of the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Integer

instance.ProfileType = value

value = instance.ProfileType
```

### C#

```csharp
System.int ProfileType {get; set;}
```

### C++/CLI

```cpp
property System.int ProfileType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Section profile type as defined in [swSpringProfileType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringProfileType_e.html)

## VBA Syntax

See [Spring::ProfileType](ms-its:sldworksapivb6.chm::/sldworks~Spring~ProfileType.html).

## Remarks

Use [ISpring::ProfileParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISpring~ProfileParameters.html) to set the spring's section profile parameters.

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::BaseProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~BaseProfile.html)
[ISpring::GetProfilePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GetProfilePoints.html)
[ISpring::SectionProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile.html)
[ISpring::SectionProfileCenter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
