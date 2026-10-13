---
title: "GetConfigurationByName2 Method (ISwDMConfigurationMgr2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfigurationMgr2"
member: "GetConfigurationByName2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationByName2.html"
---

# GetConfigurationByName2 Method (ISwDMConfigurationMgr2)

Gets the specified configuration in the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationByName2( _
   ByVal ConfigurationName As System.String, _
   ByRef result As SwDMConfigurationError _
) As SwDMConfiguration
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfigurationMgr2
Dim ConfigurationName As System.String
Dim result As SwDMConfigurationError
Dim value As SwDMConfiguration

value = instance.GetConfigurationByName2(ConfigurationName, result)
```

### C#

```csharp
SwDMConfiguration GetConfigurationByName2(
   System.string ConfigurationName,
   out SwDMConfigurationError result
)
```

### C++/CLI

```cpp
SwDMConfiguration^ GetConfigurationByName2(
   System.String^ ConfigurationName,
   [Out] SwDMConfigurationError result
)
```

### Parameters

- `ConfigurationName`: Name of configuration to get (see **Remarks**)
- `result`: Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.html)

### Return Value

Pointer to an [ISwDMConfiguration](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration.html) object

## VBA Syntax

See [SwDMConfigurationMgr2::GetConfigurationByName2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfigurationMgr2~GetConfigurationByName2.html).

## Examples

See the [ISwDMConfigurationMgr2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.html) examples.

## Remarks

Call [ISwDMConfigurationMgr2::GetConfigurationNames2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationNames2.html) before calling this method.

## See Also

[ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.html)
[ISwDMConfigurationMgr2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2_members.html)
[ISwDMComponent::ConfigurationName Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.html)
[ISwDMConfiguration::GetParentConfigurationName Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.html)
[ISwDMConfiguration7::Name2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.html)

## Availability

SOLIDWORKS Document Manager API 2019 SP0
