---
title: "ISetParameters Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "ISetParameters"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html"
---

# ISetParameters Method (IConfiguration)

Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetParameters( _
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

instance.ISetParameters(NParamCount, Params, Values)
```

### C#

```csharp
void ISetParameters(
   System.int NParamCount,
   ref System.string Params,
   ref System.string Values
)
```

### C++/CLI

```cpp
void ISetParameters(
   System.int NParamCount,
   System.String^% Params,
   System.String^% Values
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NParamCount`: Number of parameters
- `Params`: - in-process, unmanaged C++: Pointer to an array of the names of the parameters of size NParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `Values`: - in-process, unmanaged C++: Pointe to an array of the values for the parameters of size NParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

To get the number of parameters to set for this configuration, call [IConfiguration::GetParameterCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetParameterCount.html).

You can control these parameters in a part document:

- Dimension values. Specify the dimension name in params for example, D1@Sketch1) and the value in values (for example, 60.0mm).
- Suppression state of features. Specify the feature name in params (for example, $STATE@Extrude2) and the suppression state in values (S=suppressed or U=Unsuppressed).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html)
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
