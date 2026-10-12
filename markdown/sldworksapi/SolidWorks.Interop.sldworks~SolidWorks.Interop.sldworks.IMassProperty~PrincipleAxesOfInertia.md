---
title: "PrincipleAxesOfInertia Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "PrincipleAxesOfInertia"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.html"
---

# PrincipleAxesOfInertia Property (IMassProperty)

Gets the principal axes of inertia for this model.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrincipleAxesOfInertia( _
   ByVal Axis As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Axis As System.Integer
Dim value As System.Object

value = instance.PrincipleAxesOfInertia(Axis)
```

### C#

```csharp
System.object PrincipleAxesOfInertia(
   System.int Axis
) {get;}
```

### C++/CLI

```cpp
property System.Object^ PrincipleAxesOfInertia {
   System.Object^ get(System.int Axis);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Axis`: - 0 = x axis
  - 1 = y axis
  - 2 = z axis

### Property Value

Array of size 3 (see **Remarks**)

## VBA Syntax

See [MassProperty::PrincipleAxesOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~PrincipleAxesOfInertia.html).

## Examples

[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)
[Get Mass Properties of Multibody Assembly Component (C#)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm)
[Get Mass Properties of Multibody Assembly Component (VB.NET)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm)
[Get Mass Properties of Multibody Assembly Component (VBA)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm)

## Remarks

This method returns:

- a vector that represents the requested axis.
- metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles:

[ lx, ly, lz ]

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::GetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~GetMomentOfInertia.html)
[IMassProperty::IGetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetMomentOfInertia.html)
[IMassProperty::IGetPrincipleMomentsOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleMomentsOfInertia.html)
[IMassProperty::PrincipleMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.html)
[IMassProperty::IGetPrincipleAxesOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleAxesOfInertia.html)
[IMassProperty::ISetOverridePrincipleAxesOrientation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverridePrincipleAxesOrientation.html)
[IMassProperty::SetOverridePrincipleAxesOrientation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverridePrincipleAxesOrientation.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
