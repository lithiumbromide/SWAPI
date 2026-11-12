---
title: "SetOverrideMomentsOfInertiaValue Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "SetOverrideMomentsOfInertiaValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMomentsOfInertiaValue.html"
---

# SetOverrideMomentsOfInertiaValue Method (IMassProperty)

Overrides the moments of inertia of the model currently being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetOverrideMomentsOfInertiaValue( _
   ByVal ReferenceFrame As System.Integer, _
   ByVal CoordinateSystemName As System.String, _
   ByVal Value As System.Object, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim ReferenceFrame As System.Integer
Dim CoordinateSystemName As System.String
Dim Value As System.Object
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetOverrideMomentsOfInertiaValue(ReferenceFrame, CoordinateSystemName, Value, Config_option, Config_names)
```

### C#

```csharp
System.bool SetOverrideMomentsOfInertiaValue(
   System.int ReferenceFrame,
   System.string CoordinateSystemName,
   System.object Value,
   System.int Config_option,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetOverrideMomentsOfInertiaValue(
   System.int ReferenceFrame,
   System.String^ CoordinateSystemName,
   System.Object^ Value,
   System.int Config_option,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ReferenceFrame`: Frame of reference as defined in [swMomentsOfInertiaReferenceFrame_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMomentsOfInertiaReferenceFrame_e.html)
- `CoordinateSystemName`: Name of coordinate system; valid only if ReferenceFrame = swMomentsOfInertiaReferenceFrame_e.swMomentsOfInertiaReferenceFrame_UserCoordinateSystem
- `Value`: Array of nine doubles: [ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of configuration names; valid only if Config_option = swInConfigurationOpts_e.swSpecifyConfiguration

### Return Value

True if the moments of inertia are overridden, false if not

## VBA Syntax

See [MassProperty::SetOverrideMomentsOfInertiaValue](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~SetOverrideMomentsOfInertiaValue.html).

## Examples

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::ISetOverrideMomentsOfInertiaValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMomentsOfInertiaValue.html)
[IMassProperty::OverrideMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMomentsOfInertia.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
