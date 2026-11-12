---
title: "ISetOverridePrincipleMomentsOfInertia Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "ISetOverridePrincipleMomentsOfInertia"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverridePrincipleMomentsOfInertia.html"
---

# ISetOverridePrincipleMomentsOfInertia Method (IMassProperty)

Overrides the principal moments of inertia of the model currently being edited in this part or assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetOverridePrincipleMomentsOfInertia( _
   ByRef Value As System.Double, _
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

value = instance.ISetOverridePrincipleMomentsOfInertia(Value, Config_option, Config_numbers, Config_names)
```

### C#

```csharp
System.bool ISetOverridePrincipleMomentsOfInertia(
   ref System.double Value,
   System.int Config_option,
   System.int Config_numbers,
   ref System.string Config_names
)
```

### C++/CLI

```cpp
System.bool ISetOverridePrincipleMomentsOfInertia(
   System.double% Value,
   System.int Config_option,
   System.int Config_numbers,
   System.String^% Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Value`: - in-process, unmanaged C++: Pointer to an array of three doubles of the principal moments of inertia: **[** Px, Py, Pz **]**
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Config_option`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_numbers`: Number of configurations
- `Config_names`: - in-process, unmanaged C++: Pointer to an array of configuration names of size Config_numbers; valid only if Config_option = swInConfigurationOpts_e.swSpecifyConfiguration
  - VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::SetOverridePrincipleMomentsOfInertia Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverridePrincipleMomentsOfInertia.html)
[IMassProperty::OverrideMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMomentsOfInertia.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
