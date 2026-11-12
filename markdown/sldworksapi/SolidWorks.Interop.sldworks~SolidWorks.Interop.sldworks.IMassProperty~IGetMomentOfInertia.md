---
title: "IGetMomentOfInertia Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "IGetMomentOfInertia"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetMomentOfInertia.html"
---

# IGetMomentOfInertia Method (IMassProperty)

Gets the moment of inertia at the specified coordinate system for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMomentOfInertia( _
   ByVal WhereTaken As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim WhereTaken As System.Integer
Dim value As System.Double

value = instance.IGetMomentOfInertia(WhereTaken)
```

### C#

```csharp
System.double IGetMomentOfInertia(
   System.int WhereTaken
)
```

### C++/CLI

```cpp
System.double IGetMomentOfInertia(
   System.int WhereTaken
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhereTaken`: Coordinate system as defined in [swMassPropertyMoment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMassPropertyMoment_e.html)

### Return Value

- in-process, unmanaged C++: Pointer to an array of size 9 containing the moment of inertia calculations (see **Remarks**)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method returns metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles:

[ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::GetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~GetMomentOfInertia.html)
[IMassProperty::IGetPrincipleAxesOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleAxesOfInertia.html)
[IMassProperty::IGetPrincipleMomentsOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleMomentsOfInertia.html)
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.html)
[IMassProperty::PrincipleMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
