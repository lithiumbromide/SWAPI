---
title: "ISetOverrideMassValue Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "ISetOverrideMassValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMassValue.html"
---

# ISetOverrideMassValue Method (IMassProperty)

Overrides the mass of the model currently being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetOverrideMassValue( _
   ByVal Value As System.Double, _
   ByVal Config_option As System.Integer, _
   ByVal Config_numbers As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Value As System.Double
Dim Config_option As System.Integer
Dim Config_numbers As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean

value = instance.ISetOverrideMassValue(Value, Config_option, Config_numbers, Config_names)
```

### C#

```csharp
System.bool ISetOverrideMassValue(
   System.double Value,
   System.int Config_option,
   System.int Config_numbers,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool ISetOverrideMassValue(
   System.double Value,
   System.int Config_option,
   System.int Config_numbers,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: Override mass value (see **Remarks**)
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_numbers`: Number of configurations
- `Config_names`: - in-process, unmanaged C++: Pointer to an array of configuration names of size Config_numbers (see **Remarks**)
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the mass value is overridden, false if not

## Remarks

| If... | Then... |
| --- | --- |
| You are editing a subcomponent | you are overriding the mass for this subcomponent and not for the top-level model. |
| Value > 0 Value < 0 | mass is overridden. mass is calculated. |
| Config_option = swInConfigurationOpts_e .swSpecifyConfiguration | Config_names is used. |

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::SetOverrideMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMassValue.html)
[IMassProperty::OverrideMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
