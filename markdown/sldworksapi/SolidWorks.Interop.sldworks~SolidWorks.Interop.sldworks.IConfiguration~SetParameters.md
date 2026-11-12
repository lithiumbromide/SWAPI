---
title: "SetParameters Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "SetParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html"
---

# SetParameters Method (IConfiguration)

Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetParameters( _
   ByRef Params As System.Object, _
   ByRef Values As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim Params As System.Object
Dim Values As System.Object

instance.SetParameters(Params, Values)
```

### C#

```csharp
void SetParameters(
   ref System.object Params,
   ref System.object Values
)
```

### C++/CLI

```cpp
void SetParameters(
   System.Object^% Params,
   System.Object^% Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Params`: Array of the names of the parameters
- `Values`: Array of the values for the parameters

## VBA Syntax

See [Configuration::SetParameters](ms-its:sldworksapivb6.chm::/sldworks~Configuration~SetParameters.html).

## Remarks

You can control these parameters in a part document:

- Dimension values. Specify the dimension name in Params for example, D1@Sketch1) and the value in Values (for example, 60.0mm).
- Suppression state of features. Specify the feature name in Params (for example, $STATE@Extrude2) and the suppression state in Values (S=Suppressed or R=Resolved).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html)
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
