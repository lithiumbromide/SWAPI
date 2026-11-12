---
title: "ISetOverrideCenterOfMassValue Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "ISetOverrideCenterOfMassValue"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideCenterOfMassValue.html"
---

# ISetOverrideCenterOfMassValue Method (IMassProperty)

Overrides the center of mass of the model currently being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetOverrideCenterOfMassValue( _
   ByRef Value As System.Double, _
   ByVal CoordinateSystemName As System.String, _
   ByVal Config_option As System.Integer, _
   ByVal Config_numbers As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Value As System.Double
Dim CoordinateSystemName As System.String
Dim Config_option As System.Integer
Dim Config_numbers As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean

value = instance.ISetOverrideCenterOfMassValue(Value, CoordinateSystemName, Config_option, Config_numbers, Config_names)
```

### C#

```csharp
System.bool ISetOverrideCenterOfMassValue(
   ref System.double Value,
   System.string CoordinateSystemName,
   System.int Config_option,
   System.int Config_numbers,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool ISetOverrideCenterOfMassValue(
   System.double% Value,
   System.String^ CoordinateSystemName,
   System.int Config_option,
   System.int Config_numbers,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: - in-process, unmanaged C++: Pointer to an array of three doubles of the x, y, and z coordinates of the center of mass
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `CoordinateSystemName`: Name of the coordinate system in which the center of mass is defined
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_numbers`: Number of configurations
- `Config_names`: - in-process, unmanaged C++: Pointer to an array of configuration names of size Config_numbers; valid only if Config_option = swInConfigurationOpts_e.swSpecifyConfiguration
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the center of mass is overridden, false if not

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::SetOverrideCenterOfMassValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideCenterOfMassValue.html)
[IMassProperty::OverrideCenterOfMass Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideCenterOfMass.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
