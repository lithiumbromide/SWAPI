---
title: "GetProfilePoints Method (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "GetProfilePoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GetProfilePoints.html"
---

# GetProfilePoints Method (ISpring)

Gets the points for creating the profile sketch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetProfilePoints() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Object

value = instance.GetProfilePoints()
```

### C#

```csharp
System.object GetProfilePoints()
```

### C++/CLI

```cpp
System.Object^ GetProfilePoints();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of points for creating the profile sketch

## VBA Syntax

See [Spring::GetProfilePoints](ms-its:sldworksapivb6.chm::/sldworks~Spring~GetProfilePoints.html).

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::BaseProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~BaseProfile.html)
[ISpring::ProfileParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileParameters.html)
[ISpring::ProfileType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileType.html)
[ISpring::SectionProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile.html)
[ISpring::SectionProfileCenter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
