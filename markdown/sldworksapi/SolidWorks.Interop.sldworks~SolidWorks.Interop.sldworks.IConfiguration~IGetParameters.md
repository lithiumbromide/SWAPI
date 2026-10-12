---
title: "IGetParameters Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IGetParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html"
---

# IGetParameters Method (IConfiguration)

Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetParameters( _
   ByVal NParamCount As System.Integer, _
   ByRef Params As System.String, _
   ByRef Values As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim NParamCount As System.Integer
Dim Params As System.String
Dim Values As System.String

instance.IGetParameters(NParamCount, Params, Values)
```

### C#

```csharp
void IGetParameters(
   System.int NParamCount,
   out System.string Params,
   out System.string Values
)
```

### C++/CLI

```cpp
void IGetParameters(
   System.int NParamCount,
   [Out] System.String^ Params,
   [Out] System.String^ Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NParamCount`: Number of parameters
- `Params`: - in-process, unmanaged C++: Pointer to an array of the names of the parameters of size NParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Values`: - in-process, unmanaged C++: Pointer to an array of the values of the parameters of size NParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Call [IConfiguration::GetParameterCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetParameterCount.html) before calling this method.

The output values may not be accurate if a design table was not added to the model.

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
