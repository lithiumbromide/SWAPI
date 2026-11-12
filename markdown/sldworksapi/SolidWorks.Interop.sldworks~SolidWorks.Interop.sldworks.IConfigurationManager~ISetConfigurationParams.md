---
title: "ISetConfigurationParams Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "ISetConfigurationParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html"
---

# ISetConfigurationParams Method (IConfigurationManager)

Sets the parameters for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetConfigurationParams( _
   ByVal ConfigName As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamValues As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfigurationManager
Dim ConfigName As System.String
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamValues As System.String
Dim value As System.Boolean

value = instance.ISetConfigurationParams(ConfigName, ParamCount, ParamNames, ParamValues)
```

### C#

```csharp
System.bool ISetConfigurationParams(
   System.string ConfigName,
   System.int ParamCount,
   ref System.string ParamNames,
   ref System.string ParamValues
)
```

### C++/CLI

```cpp
System.bool ISetConfigurationParams(
   System.String^ ConfigName,
   System.int ParamCount,
   System.String^% ParamNames,
   System.String^% ParamValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration
- `ParamCount`: Number of parameters
- `ParamNames`: - in-process, unmanaged C++: Pointer to an array of the names of the parameters for this configuration of size ParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `ParamValues`: - in-process, unmanaged C++: Pointer to an array of values for the parameters for this configuration of size ParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if the names and values of the parameters for this configuration are set, false
if unsuccessful

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::GetConfigurationParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html)
[IConfigurationManager::IGetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html)
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)

## Availability

SOLIDWORKS 2004 SP3, Revision Number 12.3
