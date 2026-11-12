---
title: "ProfileParameters Property (ISpring)"
project: "SOLIDWORKS API Help"
interface: "ISpring"
member: "ProfileParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileParameters.html"
---

# ProfileParameters Property (ISpring)

Gets or sets the section profile parameters for the spring.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProfileParameters As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISpring
Dim value As System.Object

instance.ProfileParameters = value

value = instance.ProfileParameters
```

### C#

```csharp
System.object ProfileParameters {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ProfileParameters {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of three doubles (see Remarks)

## VBA Syntax

See [Spring::ProfileParameters](ms-its:sldworksapivb6.chm::/sldworks~Spring~ProfileParameters.html).

## Remarks

The values of the array depend on the type of profile.

| Type of profile | Values |
| --- | --- |
| Circular | [ diameter, 0, 0 ] |
| Square | [ height, width ] |
| Trapezoid | [ height, bottom, top ] |

Use [ISpring::ProfileType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISpring~ProfileType.html) to set the spring's type of profile.

## See Also

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.html)
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html)
[ISpring::BaseProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~BaseProfile.html)
[ISpring::GetProfilePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GetProfilePoints.html)
[ISpring::SectionProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile.html)
[ISpring::SectionProfileCenter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter.html)

## Availability

SOLIDWORKS 2005 SP1, Revision Number 13.1
