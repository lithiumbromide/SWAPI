---
title: "GetParameterCount Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetParameterCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html"
---

# GetParameterCount Method (IConfiguration)

Gets the number of parameters for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParameterCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

value = instance.GetParameterCount()
```

### C#

```csharp
System.int GetParameterCount()
```

### C++/CLI

```cpp
System.int GetParameterCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of parameters

## VBA Syntax

See [Configuration::GetParameterCount](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetParameterCount.html).

## Remarks

Call this method before calling [IConfiguration::IGetParameters](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetParameters.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html)
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
