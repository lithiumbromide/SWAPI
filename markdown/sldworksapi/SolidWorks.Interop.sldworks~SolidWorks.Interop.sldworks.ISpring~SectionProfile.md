---
title: "SectionProfile Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "SectionProfile"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile.html"
---

# SectionProfile Property (ISpring)

Gets or sets the section profile for the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property SectionProfile As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As Body2

instance.SectionProfile = value

value = instance.SectionProfile
```

### C#

```csharp
Body2 SectionProfile {get; set;}
```

### C++/CLI

```cpp
property Body2^ SectionProfile {
   Body2^ get();
   void set (    Body2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) (see **Remarks**)

## VBA Syntax

See [Spring::SectionProfile](ms-its:sldworksapivb6.chm::/sldworks~Spring~SectionProfile.html).

## Remarks

The profile refers to the body associated with a circular edge that determines the base diameter of the spring. For example, to create a spring on a circular sketch, use [ISketch::GetContourEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetContourEdges.html) or [ISketch::IGetContours](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetContourEdges.html) and [IEdge::GetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge~GetBody.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::BaseProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~BaseProfile.html)
[ISpring::GetProfilePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GetProfilePoints.html)
[ISpring::ProfileParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileParameters.html)
[ISpring::ProfileType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileType.html)
[ISpring::SectionProfileCenter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
