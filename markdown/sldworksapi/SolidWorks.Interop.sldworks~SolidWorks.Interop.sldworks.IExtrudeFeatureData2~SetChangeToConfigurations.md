---
title: "SetChangeToConfigurations Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "SetChangeToConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetChangeToConfigurations.html"
---

# SetChangeToConfigurations Method (IExtrudeFeatureData2)

Applies changes made to this extrude feature to the specified configurations.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetChangeToConfigurations( _
   ByVal Config_opt As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Config_opt As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean

value = instance.SetChangeToConfigurations(Config_opt, Config_names)
```

### C#

```csharp
System.bool SetChangeToConfigurations(
   System.int Config_opt,
   System.object Config_names
)
```

### C++/CLI

```cpp
System.bool SetChangeToConfigurations(
   System.int Config_opt,
   System.Object^ Config_names
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Config_opt`: Configuration option as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)
- `Config_names`: Array of the names of the configurations to modify

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [ExtrudeFeatureData2::SetChangeToConfigurations](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~SetChangeToConfigurations.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::ISetChangeToConfigurations Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetChangeToConfigurations.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
