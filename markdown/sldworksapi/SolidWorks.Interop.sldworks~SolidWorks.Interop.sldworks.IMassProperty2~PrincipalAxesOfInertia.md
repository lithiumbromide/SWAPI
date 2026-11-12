---
title: "PrincipalAxesOfInertia Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "PrincipalAxesOfInertia"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalAxesOfInertia.html"
---

# PrincipalAxesOfInertia Property (IMassProperty2)

Gets the principal axis of inertia for the specified axis.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrincipalAxesOfInertia( _
   ByVal Axis As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim Axis As System.Integer
Dim value As System.Object

value = instance.PrincipalAxesOfInertia(Axis)
```

### C#

```csharp
System.object PrincipalAxesOfInertia(
   System.int Axis
) {get;}
```

### C++/CLI

```cpp
property System.Object^ PrincipalAxesOfInertia {
   System.Object^ get(System.int Axis);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Axis`: - 0 = x axis
  - 1 = y axis
  - 2 = z axis

### Property Value

Zero-based array of size 3 (see **Remarks**)

## VBA Syntax

See [MassProperty2::PrincipalAxesOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~PrincipalAxesOfInertia.html).

## Remarks

This method returns:

- A vector that represents the specified Axis: lx, ly, or lz.
- Metric units unless explicitly specified otherwise.

If [IMassPropertyOverrideOptions::OverrideMomentsOfInertia](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~OverrideMomentsOfInertia.html) is true or [IMassProperty2::IncludeHiddenBodiesOrComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~IncludeHiddenBodiesOrComponents.html) is reset, then call [IMassProperty2::Recalculate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~Recalculate.html) before using this property.

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)
[IMassPropertyOverrideOptions::SetOverridePrincipalAxesOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~SetOverridePrincipalAxesOrientation.html)
[IMassProperty2::PrincipalMomentsOfInertia Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~PrincipalMomentsOfInertia.html)
[IMassProperty2::GetMomentOfInertia Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~GetMomentOfInertia.html)
[IMassPropertyOverrideOptions::GetOverridePrincipalAxesOrientation Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions~GetOverridePrincipalAxesOrientation.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
