---
title: "CenterOfMass Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "CenterOfMass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~CenterOfMass.html"
---

# CenterOfMass Property (IMassProperty)

Gets the center of mass.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CenterOfMass As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Object

value = instance.CenterOfMass
```

### C#

```csharp
System.object CenterOfMass {get;}
```

### C++/CLI

```cpp
property System.Object^ CenterOfMass {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array containing the center of mass coordinates (see **Remarks**)

## VBA Syntax

See [MassProperty::CenterOfMass](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~CenterOfMass.html).

## Examples

[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get Mass Properties of Multibody Assembly Component (C#)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm)
[Get Mass Properties of Multibody Assembly Component (VB.NET)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm)
[Get Mass Properties of Multibody Assembly Component (VBA)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm)

## Remarks

This property returns metric units unless explicitly specified otherwise.

The return value is a 0-based array of doubles:

**[** `x, y, z` **]**.

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::IGetCenterOfMass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetCenterOfMass.html)
[IMassProperty::ISetAssignedMassProp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetAssignedMassProp.html)
[IMassProperty::SetAssignedMassProp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetAssignedMassProp.html)
[IMassProperty::Mass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Mass.html)
[IMassProperty::OverrideCenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideCenterOfMass.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
