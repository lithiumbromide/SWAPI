---
title: "SetOverridePrincipleAxesOrientation Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "SetOverridePrincipleAxesOrientation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverridePrincipleAxesOrientation.html"
---

# SetOverridePrincipleAxesOrientation Method (IMassProperty)

Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverridePrincipleAxesOrientation( _
   ByVal Axis As System.Integer, _
   ByVal Value As System.Object, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Axis As System.Integer
Dim Value As System.Object
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetOverridePrincipleAxesOrientation(Axis, Value, Config_option, Config_names)
```

### C#

```csharp
System.bool SetOverridePrincipleAxesOrientation(
   System.int Axis,
   System.object Value,
   System.int Config_option,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetOverridePrincipleAxesOrientation(
   System.int Axis,
   System.Object^ Value,
   System.int Config_option,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Axis`: One of the following principal axes:

  - 0 = X axis
  - 1 = Y axis
  - 2 = Z axis
- `Value`: An array of three doubles of the x, y, and z coordinates of Axis
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names; valid only if Config_option = swInConfigurationOpts_e.swSpecifyConfiguration

### Return Value

True if orientation of principal axis is overridden, false if not

## VBA Syntax

See [MassProperty::SetOverridePrincipleAxesOrientation](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~SetOverridePrincipleAxesOrientation.html).

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetOverridePrincipleAxesOrientation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverridePrincipleAxesOrientation.html)
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
