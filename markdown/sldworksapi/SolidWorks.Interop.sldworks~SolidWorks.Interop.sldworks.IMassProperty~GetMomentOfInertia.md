---
title: "GetMomentOfInertia Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "GetMomentOfInertia"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~GetMomentOfInertia.html"
---

# GetMomentOfInertia Method (IMassProperty)

Gets the moment of inertia at the specified coordinate system for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMomentOfInertia( _
   ByVal WhereTaken As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
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

See [MassProperty::GetMomentOfInertia](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~GetMomentOfInertia.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)
[Get Mass Properties of Multibody Assembly Component (C#)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm)
[Get Mass Properties of Multibody Assembly Component (VB.NET)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm)
[Get Mass Properties of Multibody Assembly Component (VBA)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm)

## Remarks

This method returns metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles:

[ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::IGetMomentOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetMomentOfInertia.html)
[IMassProperty::IGetPrincipleAxesOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleAxesOfInertia.html)
[IMassProperty::IGetPrincipleMomentsOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetPrincipleMomentsOfInertia.html)
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.html)
[IMassProperty::PrincipleMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleMomentsOfInertia.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
