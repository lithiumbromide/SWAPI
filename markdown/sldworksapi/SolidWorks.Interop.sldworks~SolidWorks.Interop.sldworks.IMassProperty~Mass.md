---
title: "Mass Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "Mass"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Mass.html"
---

# Mass Property (IMassProperty)

Gets the mass of this model.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Mass As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Double

value = instance.Mass
```

### C#

```csharp
System.double Mass {get;}
```

### C++/CLI

```cpp
property System.double Mass {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Mass

## VBA Syntax

See [MassProperty::Mass](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~Mass.html).

## Examples

[Insert Coordinate System at Center of Mass (VBA)](Insert_Coordinate_System_at_Center_of_Mass_Example_VB.htm)
[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get Mass Properties of Multibody Assembly Component (C#)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm)
[Get Mass Properties of Multibody Assembly Component (VB.NET)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm)
[Get Mass Properties of Multibody Assembly Component (VBA)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm)

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::OverrideMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMass.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
