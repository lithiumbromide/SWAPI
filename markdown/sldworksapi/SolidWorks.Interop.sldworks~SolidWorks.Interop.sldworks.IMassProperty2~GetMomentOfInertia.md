---
title: "GetMomentOfInertia Method (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "GetMomentOfInertia"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.html"
---

# GetMomentOfInertia Method (IMassProperty2)

Gets the moment of inertia at the specified coordinate system for the selected bodies/components.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMomentOfInertia( _
   ByVal WhereTaken As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim WhereTaken As System.Integer
Dim value As System.Object

value = instance.GetMomentOfInertia(WhereTaken)
```

### C#

```csharp
System.object GetMomentOfInertia(
   System.int WhereTaken
)
```

### C++/CLI

```cpp
System.Object^ GetMomentOfInertia(
   System.int WhereTaken
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhereTaken`: Coordinate system as defined in [swMassPropertyMoment_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMassPropertyMoment_e.html)

### Return Value

Array containing the moment of inertia calculations (see **Remarks**)

## VBA Syntax

See [MassProperty2::GetMomentOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~GetMomentOfInertia.html).

## Examples

See the [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html) examples.

## Remarks

The return value is a 0-based array of nine doubles:

[ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)
[IMassProperty2::PrincipalAxesOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.html)
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.html)
[IMassPropertyOverrideOptions::SetOverrideMomentsOfInertiaValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverrideMomentsOfInertiaValue.html)
[IMassPropertyOverrideOptions::GetOverrideMomentsOfInertiaValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverrideMomentsOfInertiaValue.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
