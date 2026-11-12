---
title: "ConeParams2 Property (ISurface)"
project: "SOLIDWORKS API Help"
interface: "ISurface"
member: "ConeParams2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~ConeParams2.html"
---

# ConeParams2 Property (ISurface)

Gets the parameters of a conical surface.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConeParams2 As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISurface
Dim value As System.Object

value = instance.ConeParams2
```

### C#

```csharp
System.object ConeParams2 {get;}
```

### C++/CLI

```cpp
property System.Object^ ConeParams2 {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of doubles describing the parameters of a conical surface

## VBA Syntax

See [Surface::ConeParams2](ms-its:sldworksapivb6.chm::/sldworks~Surface~ConeParams2.html).

## Examples

[Get Parameters of Conical Surface (VBA)](Get_Parameters_of_Conical_Surface_Example_VB.htm)
[Get Parameters of Conical Surface (VB.NET)](Get_Parameters_of_Conical_Surface_Example_VBNET.htm)
[Get Parameters of Conical Surface (C#)](Get_Parameters_of_Conical_Surface_Example_CSharp.htm)

## Remarks

Returns an array of 11 doubles:

- origin.x
- origin.y
- origin.z
- axis.x
- axis.y
- axis.z
- radius
- half angle
- reference_direction.x
- reference_direction.y
- reference_direction.z

Half angle element is in radians. Origin, radius, and reference direction elements are in meters.

## See Also

[ISurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.html)
[ISurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html)
[ISurface::IsCone Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface~IsCone.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
