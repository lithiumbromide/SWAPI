---
title: "SetOverrideMassValue Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "SetOverrideMassValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMassValue.html"
---

# SetOverrideMassValue Method (IMassProperty)

Overrides the mass of the model currently being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverrideMassValue( _
   ByVal Value As System.Double, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Value As System.Double
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetOverrideMassValue(Value, Config_option, Config_names)
```

### C#

```csharp
System.bool SetOverrideMassValue(
   System.double Value,
   System.int Config_option,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetOverrideMassValue(
   System.double Value,
   System.int Config_option,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Override mass value (see **Remarks**)
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names (see **Remarks**)

### Return Value

True if the mass value is overridden, false if not

## VBA Syntax

See [MassProperty::SetOverrideMassValue](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~SetOverrideMassValue.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

## Remarks

| If... | Then... |
| --- | --- |
| You are editing a subcomponent | you are overriding the mass for this subcomponent and not for the top-level model. |
| Value > 0 Value < 0 | mass is overridden. mass is calculated. |
| Config_option = swInConfigurationOpts_e .swSpecifyConfiguration | Config_names is used. |

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetOverrideMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMassValue.html)
[IMassProperty::OverrideMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
