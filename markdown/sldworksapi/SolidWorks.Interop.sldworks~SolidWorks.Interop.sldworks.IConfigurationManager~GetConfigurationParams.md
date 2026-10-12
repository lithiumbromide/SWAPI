---
title: "GetConfigurationParams Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "GetConfigurationParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html"
---

# GetConfigurationParams Method (IConfigurationManager)

Gets the parameters for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationParams( _
   ByVal ConfigName As System.String, _
   ByRef Params As System.Object, _
   ByRef Values As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim ConfigName As System.String
Dim Params As System.Object
Dim Values As System.Object
Dim value As System.Boolean

value = instance.GetConfigurationParams(ConfigName, Params, Values)
```

### C#

```csharp
System.bool GetConfigurationParams(
   System.string ConfigName,
   out System.object Params,
   out System.object Values
)
```

### C++/CLI

```cpp
System.bool GetConfigurationParams(
   System.String^ ConfigName,
   [Out] System.Object^ Params,
   [Out] System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration
- `Params`: Array of the names of the parameters for this configuration
- `Values`: Array of values of the parameters for this configuration

### Return Value

True if successful in getting the names and values of the parameters for this configuration, false if unsuccessful

## VBA Syntax

See [ConfigurationManager::GetConfigurationParams](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~GetConfigurationParams.html).

## Examples

[Extract Configuration-specific Parameters (VBA)](Extract_Configuration-Specific_Parameters_Example_VB.htm)

## Remarks

The output values may not be accurate if a design table was not added to the model.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html)
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html)
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
