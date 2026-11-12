---
title: "GetConfigurationParamsCount Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "GetConfigurationParamsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html"
---

# GetConfigurationParamsCount Method (IConfigurationManager)

Gets the number of parameters for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationParamsCount( _
   ByVal ConfigName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim ConfigName As System.String
Dim value As System.Integer

value = instance.GetConfigurationParamsCount(ConfigName)
```

### C#

```csharp
System.int GetConfigurationParamsCount(
   System.string ConfigName
)
```

### C++/CLI

```cpp
System.int GetConfigurationParamsCount(
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration

### Return Value

Number of parameters in this configuration

## VBA Syntax

See [ConfigurationManager::GetConfigurationParamsCount](ms-its:sldworksapivb6.chm::/sldworks~ConfigurationManager~GetConfigurationParamsCount.html).

## Examples

[Get Configuration Parameters (C++)](Get_Configuration_Parameters_Example_CPlusPlus_COM.htm)

## Remarks

Call this method before calling [IConfigurationManager::IGetConfigurationParams](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html).

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
