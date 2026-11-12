---
title: "PrincipleMomentsOfInertia Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "PrincipleMomentsOfInertia"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.html"
---

# PrincipleMomentsOfInertia Property (IMassProperty)

Gets the principal moments of inertia for this model.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property PrincipleMomentsOfInertia As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Object

value = instance.PrincipleMomentsOfInertia
```

### C#

```csharp
System.object PrincipleMomentsOfInertia {get;}
```

### C++/CLI

```cpp
property System.Object^ PrincipleMomentsOfInertia {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of size 3 (see **Remarks**)

## VBA Syntax

See [MassProperty::PrincipleMomentsOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~PrincipleMomentsOfInertia.html).

## Examples

[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get Mass Properties of Multibody Assembly Component (C#)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm)
[Get Mass Properties of Multibody Assembly Component (VB.NET)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm)
[Get Mass Properties of Multibody Assembly Component (VBA)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm)

## Remarks

This property returns metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles:

[ Px, Py, Pz ]

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::GetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~GetMomentOfInertia.html)
[IMassProperty::IGetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetMomentOfInertia.html)
[IMassProperty::IGetPrincipleAxesOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleAxesOfInertia.html)
[IMassProperty::IGetPrincipleMomentsOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleMomentsOfInertia.html)
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.html)
[IMassProperty::OverrideMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMomentsOfInertia.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
