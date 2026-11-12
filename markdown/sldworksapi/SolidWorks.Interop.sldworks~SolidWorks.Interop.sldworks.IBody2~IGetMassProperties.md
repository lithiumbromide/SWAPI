---
title: "IGetMassProperties Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IGetMassProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetMassProperties.html"
---

# IGetMassProperties Method (IBody2)

Gets the mass properties of this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMassProperties( _
   ByVal Density As System.Double _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Density As System.Double
Dim value As System.Double

value = instance.IGetMassProperties(Density)
```

### C#

```csharp
System.double IGetMassProperties(
   System.double Density
)
```

### C++/CLI

```cpp
System.double IGetMassProperties(
   System.double Density
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Density`: Density to use for the mass property calculations on this body

### Return Value

- in-process, unmanaged C++: Pointer to an array of doubles (see **Remarks**)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

This method is intended for obtaining the mass properties of temporary objects but may also be used with the SOLIDWORKS [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object that is created by the user. To get the mass properties of the SOLIDWORKS IBody2 object created by the user, you can also use [IModelDocExtension::IGetMassProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~IGetMassProperties.html), which uses the density currently set for the body's material.

The return value is an array of doubles as follows:

Solid body

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Volume, Area, Mass(Volume*density), MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

Sheet body

```vb
[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Area, Circumference, Mass(Area*density), MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]
```

Wire body

[ CenterOfMassX, CenterOfMassY, CenterOfMassZ, Length, 0, Mass(Length*density), MomXX, MomYY, MomZZ, MomXY, MomZX, MomYZ ]

You can use [ISldWorks::GetUserPreferenceDoubleValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceDoubleValue.html) to get the density used by the SOLIDWORKS part. Consistent with all other SOLIDWORKS API functions, units are metric unless otherwise specified.

SOLIDWORKS returns information (such as the center of mass) in relation to where the body was created. For example, if you create a block in a part file that is centered at (0,0,0), then SOLIDWORKS returns the center of mass as (0,0,0). If you then use this part at some random location within an assembly, and the body is obtained from the assembly component object using [IComponent2::IGetBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IGetBody.html), then SOLIDWORKS still returns the center of mass as (0,0,0). If you need to determine the body's center of mass in relation to the assembly coordinate system, you need to multiply the component transform and the center of mass coordinates (see [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html)).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetMassProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMassProperties.html)
