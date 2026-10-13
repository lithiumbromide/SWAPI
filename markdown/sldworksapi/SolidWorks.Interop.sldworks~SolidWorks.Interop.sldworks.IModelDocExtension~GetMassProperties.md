---
title: "GetMassProperties Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetMassProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties.html"
---

# GetMassProperties Method (IModelDocExtension)

Obsolete. Superseded by [IModelDocExtension::GetMassProperties2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMassProperties( _
   ByVal Accuracy As System.Integer, _
   ByRef Status As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Accuracy As System.Integer
Dim Status As System.Integer
Dim value As System.Object

value = instance.GetMassProperties(Accuracy, Status)
```

### C#

```csharp
System.object GetMassProperties(
   System.int Accuracy,
   out System.int Status
)
```

### C++/CLI

```cpp
System.Object^ GetMassProperties(
   System.int Accuracy,
   [Out] System.int Status
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Accuracy`: - 0 = as is
  - 1 = default
  - 2 = maximum
- `Status`: Status of the mass property results as defined in [swMassPropertiesStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMassPropertiesStatus_e.html)

### Return Value

Array of size 13 (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::GetMassProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetMassProperties.html).

## Remarks

The return value is a 0-based array of doubles as follows:

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, Area, Mass, MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ, Accuracy ]

You can use [ISldWorks::GetUserPreferenceDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.html) and swMaterialPropertyDensity to get the density of the SOLIDWORKS part. If the user did not explicitly set the density, then SOLIDWORKS uses a value of 1.0. You can also derive the density of the body by calculating:

Density = ( Mass / Volume )

This method returns metric units unless specified otherwise.

| If this object is... | Then... |
| --- | --- |
| An assembly | SOLIDWORKS does not include any suppressed components in the mass property analysis. See IComponent2::GetSuppression to determine the state of each assembly component. This method returns the moments of inertia (MOI) about the assembly center-of-gravity coordinate system aligned with the assembly axes. |
| A part | The calculated origin for the returned values are based on the default coordinate systems of the model document. They are not based on the selected coordinate system. |

This method supports multibody parts.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::CreateMassProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty.html)
[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IModelDocExtension::IGetMassProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMassProperties.html)
[IModelDocExtension::GetMassPropertiesSelectedComp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMassProperties2.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
