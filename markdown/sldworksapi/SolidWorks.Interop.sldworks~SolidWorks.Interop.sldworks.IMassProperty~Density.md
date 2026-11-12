---
title: "Density Property (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "Density"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Density.html"
---

# Density Property (IMassProperty)

Gets the density for this model.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Density As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim value As System.Double

value = instance.Density
```

### C#

```csharp
System.double Density {get;}
```

### C++/CLI

```cpp
property System.double Density {
   System.double get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Density

## VBA Syntax

See [MassProperty::Density](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~Density.html).

## Examples

[Set Dimensions to Mid-tolerance (VBA)](Set_Dimensions_to_Mid-Tolerance_Example_VB.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get Mass Properties of Multibody Assembly Component (C#)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm)
[Get Mass Properties of Multibody Assembly Component (VB.NET)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm)
[Get Mass Properties of Multibody Assembly Component (VBA)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm)

## Remarks

You can also:

- Derive the density of the body by calculating Density = ( Mass / Volume ).
- Use [ISldWorks::GetUserPreferenceDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.html) to get the density of the model.

This property returns metric units unless explicitly specified otherwise.

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
