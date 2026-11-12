---
title: "SetConfigurationParams Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "SetConfigurationParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html"
---

# SetConfigurationParams Method (IConfigurationManager)

Sets the parameters for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetConfigurationParams( _
   ByVal ConfigName As System.String, _
   ByRef ParamNames As System.Object, _
   ByRef ParamValues As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim ConfigName As System.String
Dim ParamNames As System.Object
Dim ParamValues As System.Object
Dim value As System.Boolean

value = instance.SetConfigurationParams(ConfigName, ParamNames, ParamValues)
```

### C#

```csharp
System.bool SetConfigurationParams(
   System.string ConfigName,
   ref System.object ParamNames,
   ref System.object ParamValues
)
```

### C++/CLI

```cpp
System.bool SetConfigurationParams(
   System.String^ ConfigName,
   System.Object^% ParamNames,
   System.Object^% ParamValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration (see **Remarks**)
- `ParamNames`: Array of the names of the parameters for ConfigName (see **Remarks**)
- `ParamValues`: Array of values for the parameters for ConfigName (see **Remarks**)

### Return Value

True if the names and values of parameters for the specified configuration are set, false if not

## VBA Syntax

See [ConfigurationManager::SetConfigurationParams](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~SetConfigurationParams.html).

## Remarks

In ConfigName, if you specify the name of a configuration that:

- does not exist, this method creates a new configuration with ParamNames and ParamValues.
- exists, this method sets that configuration with ParamNames and ParamValues.

You can control these parameters in a part document:

- Dimension values. Specify the dimension name in ParamNames for example, D1@Sketch1) and the value in ParamValues (for example, 60.0mm).
- Suppression state of features. Specify the feature name in ParamNames (for example, $STATE@Extrude2) and the suppression state in ParamValues (S=Suppressed or R=Resolved).

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html)
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
