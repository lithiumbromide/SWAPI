---
title: "GetMassProperties2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetMassProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2.html"
---

# GetMassProperties2 Method (IModelDocExtension)

Obsolete. Superseded by [IMassProperty2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassProperties2( _
   ByVal Accuracy As System.Integer, _
   ByRef Status As System.Integer, _
   ByVal UseSelected As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Accuracy As System.Integer
Dim Status As System.Integer
Dim UseSelected As System.Boolean
Dim value As System.Object

value = instance.GetMassProperties2(Accuracy, Status, UseSelected)
```

### C#

```csharp
System.object GetMassProperties2(
   System.int Accuracy,
   out System.int Status,
   System.bool UseSelected
)
```

### C++/CLI

```cpp
System.Object^ GetMassProperties2(
   System.int Accuracy,
   [Out] System.int Status,
   System.bool UseSelected
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Accuracy`: - 0 = as is
  - 1 = default
  - 2 = maximum
- `Status`: Error code as defined in [swMassPropertiesStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMassPropertiesStatus_e.html)
- `UseSelected`: True to return the mass properties of the selected components only, false to return the mass properties of the entire model, excluding suppressed components

### Return Value

Array of size 12 (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::GetMassProperties2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetMassProperties2.html).

## Examples

[Get Mass Properties (VBA)](Get_Mass_Properties_of_ActiveDoc_Example_VB.htm)
[Get Mass Properties (VB.NET)](Get_Mass_Properties_of_ActiveDoc_Example_VBNET.htm)
[Get Mass Properties (C#)](Get_Mass_Properties_of_ActiveDoc_Example_CSharp.htm)

## Remarks

| If this model is... | Then pre-select... |
| --- | --- |
| An assembly | Components for which to get mass properties. This method returns the center of mass and moments of inertia in the coordinate system of the assembly. |
| A part | Solid bodies for which to get mass properties. The calculated origin for the returned values is based on the default coordinate system of the part. It is not based on the selected coordinate system. |

The return value is a 0-based array of doubles as follows:

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, SurfaceArea, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

Where:

- Mom`NN` = `NN-component` of the moment of inertia taken at the center of mass and aligned with the output coordinate system

You can use [ISldWorks::GetUserPreferenceDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.html) and swMaterialPropertyDensity to get the density of the SOLIDWORKS part. If the user did not explicitly set the density, then SOLIDWORKS uses a value of 1.0. You can also derive the density of the body by calculating:

Density = ( `Mass` / `Volume` )

This method:

- returns values in metric units.
- supports multibody parts.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateMassProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty.html)
[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
