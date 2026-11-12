---
title: "GetParameters Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html"
---

# GetParameters Method (IConfiguration)

Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetParameters( _
   ByRef Params As System.Object, _
   ByRef Values As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim Params As System.Object
Dim Values As System.Object

instance.GetParameters(Params, Values)
```

### C#

```csharp
void GetParameters(
   out System.object Params,
   out System.object Values
)
```

### C++/CLI

```cpp
void GetParameters(
   [Out] System.Object^ Params,
   [Out] System.Object^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Params`: Array of the names of the parameters
- `Values`: Array of the values of the parameters

## VBA Syntax

See [Configuration::GetParameters](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetParameters.html).

## Remarks

The output values may not be accurate if a design table was not added to the model.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html)
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
