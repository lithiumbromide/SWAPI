---
title: "SetOverrideCenterOfMassValue Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "SetOverrideCenterOfMassValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideCenterOfMassValue.html"
---

# SetOverrideCenterOfMassValue Method (IMassProperty)

Overrides the center of mass of the model currently being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverrideCenterOfMassValue( _
   ByVal Value As System.Object, _
   ByVal CoordinateSystemName As System.String, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Value As System.Object
Dim CoordinateSystemName As System.String
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetOverrideCenterOfMassValue(Value, CoordinateSystemName, Config_option, Config_names)
```

### C#

```csharp
System.bool SetOverrideCenterOfMassValue(
   System.object Value,
   System.string CoordinateSystemName,
   System.int Config_option,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetOverrideCenterOfMassValue(
   System.Object^ Value,
   System.String^ CoordinateSystemName,
   System.int Config_option,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Array of three doubles of the x, y, and z coordinates of the center of mass
- `CoordinateSystemName`: Name of the coordinate system in which the center of mass is defined
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names; valid only if Config_option = swInConfigurationOpts_e.swSpecifyConfiguration

### Return Value

True if the center of mass is overridden, false if not

## VBA Syntax

See [MassProperty::SetOverrideCenterOfMassValue](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~SetOverrideCenterOfMassValue.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetOverrideCenterOfMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideCenterOfMassValue.html)
[IMassProperty::OverrideCenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideCenterOfMass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
