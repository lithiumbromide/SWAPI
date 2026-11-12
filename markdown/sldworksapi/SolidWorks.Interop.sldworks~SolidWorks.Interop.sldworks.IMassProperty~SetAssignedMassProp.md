---
title: "SetAssignedMassProp Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "SetAssignedMassProp"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetAssignedMassProp.html"
---

# SetAssignedMassProp Method (IMassProperty)

Sets the mass and center of gravity for the specified configurations for this model being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAssignedMassProp( _
   ByVal Mass As System.Double, _
   ByVal Center_x As System.Double, _
   ByVal Center_y As System.Double, _
   ByVal Center_z As System.Double, _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Mass As System.Double
Dim Center_x As System.Double
Dim Center_y As System.Double
Dim Center_z As System.Double
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetAssignedMassProp(Mass, Center_x, Center_y, Center_z, Config_opt, Config_names)
```

### C#

```csharp
System.bool SetAssignedMassProp(
   System.double Mass,
   System.double Center_x,
   System.double Center_y,
   System.double Center_z,
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetAssignedMassProp(
   System.double Mass,
   System.double Center_x,
   System.double Center_y,
   System.double Center_z,
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mass`: Value for mass
- `Center_x`: x coordinate for center of gravity
- `Center_y`: y coordinate for center of gravity
- `Center_z`: z coordinate for center of gravity
- `Config_opt`: Configuration options as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of the configuration names

### Return Value

True if the mass and center of gravity are set, false if not

## VBA Syntax

See [MassProperty::SetAssignedMassProp](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~SetAssignedMassProp.html).

## Remarks

| If... | Then... |
| --- | --- |
| You are editing a subcomponent | you are setting the mass for this subcomponent and not for the top-level model. |
| You specify a value < 0 for Mass | mass is calculated; it is not user-defined. |
| Config_opt is set to swSpecifyConfiguration | Config_names is used. |

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetAssignedMassProp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetAssignedMassProp.html)
[IMassProperty::Mass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~Mass.html)
[IMassProperty::UserAssigned Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~UserAssigned.html)
[IMassProperty::IGetCenterOfMass Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IGetCenterOfMass.html)
[IMassProperty::CenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~CenterOfMass.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
