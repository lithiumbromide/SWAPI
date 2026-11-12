---
title: "ISetOverridePrincipleAxesOrientation Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "ISetOverridePrincipleAxesOrientation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverridePrincipleAxesOrientation.html"
---

# ISetOverridePrincipleAxesOrientation Method (IMassProperty)

Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetOverridePrincipleAxesOrientation( _
   ByVal Axis As System.Integer, _
   ByRef Value As System.Double, _
   ByVal Config_option As System.Integer, _
   ByVal Config_numbers As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim Axis As System.Integer
Dim Value As System.Double
Dim Config_option As System.Integer
Dim Config_numbers As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean

value = instance.ISetOverridePrincipleAxesOrientation(Axis, Value, Config_option, Config_numbers, Config_names)
```

### C#

```csharp
System.bool ISetOverridePrincipleAxesOrientation(
   System.int Axis,
   ref System.double Value,
   System.int Config_option,
   System.int Config_numbers,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool ISetOverridePrincipleAxesOrientation(
   System.int Axis,
   System.double% Value,
   System.int Config_option,
   System.int Config_numbers,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Axis`: One of the following principal axes:

  - 0 = X axis
  - 1 = Y axis
  - 2 = Z axis
- `Value`: - in-process, unmanaged C++: Pointer to an array of three doubles of the x, y, and z coordinates of the specified principal Axis
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_numbers`: Number of configurations
- `Config_names`: - in-process, unmanaged C++: Pointer to an array of configuration names of size Config_numbers; valid only if Config_option = swInConfigurationOpts_e.swSpecifyConfiguration
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if orientation of principal axis is overridden, false if not

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::SetOverridePrincipleAxesOrientation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverridePrincipleAxesOrientation.html)
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
