---
title: "IGetConfigurationParams Method (IConfigurationManager)"
project: "SOLIDWORKS API Help"
interface: "IConfigurationManager"
member: "IGetConfigurationParams"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~IGetConfigurationParams.html"
---

# IGetConfigurationParams Method (IConfigurationManager)

Gets the parameters for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetConfigurationParams( _
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

value = instance.IGetConfigurationParams(ConfigName, ParamCount, ParamNames, ParamValues)
```

### C#

```csharp
System.bool IGetConfigurationParams(
   System.string ConfigName,
   System.int ParamCount,
   out System.string ParamNames,
   out System.string ParamValues
)
```

### C++/CLI

```cpp
System.bool IGetConfigurationParams(
   System.String^ ConfigName,
   System.int ParamCount,
   [Out] System.String^ ParamNames,
   [Out] System.String^ ParamValues
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of the configuration
- `ParamCount`: Number of parameters for this configuration
- `ParamNames`: - in-process, unmanaged C++: Pointer to an an array of the names of the parameters for this configuration of size ParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.
- `ParamValues`: - in-process, unmanaged C++: Pointer to an array of values of the parameters for this configuration of size ParamCount

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

### Return Value

True if successful in getting the names and values of the parameters for this configuration, false if unsuccessful

## Examples

[Get Configuration Parameters (C++)](Get_Configuration_Parameters_Example_CPlusPlus_COM.htm)

## Remarks

Call [IConfgurationManager::GetConfigurationParamsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager~GetConfigurationParamsCount.html) before calling this method to get the value for ParamCount.

The output values may not be accurate if a design table was not added to the model.

## See Also

[IConfigurationManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager.html)
[IConfigurationManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html)
[IConfigurationManager::GetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~GetConfigurationParams.html)
[IConfigurationManager::ISetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ISetConfigurationParams.html)
[IConfigurationManager::SetConfigurationParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~SetConfigurationParams.html)
[IConfigurationManager::ActiveConfiguration Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~ActiveConfiguration.html)
[IConfiguration::SetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.html)
[IConfiguration::ISetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.html)
[IConfiguration::IGetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.html)
[IConfiguration::GetParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.html)
[IConfiguration::GetParameterCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameterCount.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
