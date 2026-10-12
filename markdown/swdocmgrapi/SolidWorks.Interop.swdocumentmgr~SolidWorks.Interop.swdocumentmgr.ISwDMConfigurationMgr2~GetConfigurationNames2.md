---
title: "GetConfigurationNames2 Method (ISwDMConfigurationMgr2)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfigurationMgr2"
member: "GetConfigurationNames2"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationNames2.html"
---

# GetConfigurationNames2 Method (ISwDMConfigurationMgr2)

Gets the names of the configurations in this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationNames2( _
   ByRef result As SwDMConfigurationError _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfigurationMgr2
Dim result As SwDMConfigurationError
Dim value As System.Object

value = instance.GetConfigurationNames2(result)
```

### C#

```csharp
System.object GetConfigurationNames2(
   out SwDMConfigurationError result
)
```

### C++/CLI

```cpp
System.Object^ GetConfigurationNames2(
   [Out] SwDMConfigurationError result
)
```

### Parameters

- `result`: Return code as defined in [swDMConfigurationError](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.SwDMConfigurationError.html)

### Return Value

Array of configuration names

## VBA Syntax

See [SwDMConfigurationMgr2::GetConfigurationNames2](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfigurationMgr2~GetConfigurationNames2.html).

## Examples

See the [ISwDMConfigurationMgr2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.html) examples.

## Remarks

Call this method before calling [ISwDMConfigurationMgr2::GetConfigurationByName2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationByName2.html).

## See Also

[ISwDMConfigurationMgr2 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2.html)
[ISwDMConfigurationMgr2 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2_members.html)
[ISwDMComponent::ConfigurationName Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.html)
[ISwDMConfiguration::GetParentConfigurationName Method ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.html)
[ISwDMConfiguration7::Name2 Property ()](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.html)

## Availability

SOLIDWORKS Document Manager API 2019 SP0
