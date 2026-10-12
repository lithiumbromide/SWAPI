---
title: "ConfigurationName Property (ISwDMComponent)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent"
member: "ConfigurationName"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.html"
---

# ConfigurationName Property (ISwDMComponent)

Gets the name of the configuration for this component.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent
Dim value As System.String

value = instance.ConfigurationName
```

### C#

```csharp
System.string ConfigurationName {get;}
```

### C++/CLI

```cpp
property System.String^ ConfigurationName {
   System.String^ get();
}
```

### Property Value

Name of the configuration for this component

## VBA Syntax

See [SwDMComponent::ConfigurationName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent~ConfigurationName.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)

## Remarks

This property only supports documents saved in SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

## See Also

[ISwDMComponent Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent.html)
[ISwDMComponent Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent_members.html)
[ISwDMComponent::Name Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~Name.html)
[ISwDMConfiguration::GetParentConfigurationName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.html)
[ISwDMConfiguration7::Name2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.html)
[ISwDMConfigurationMgr::GetActiveConfigurationName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetActiveConfigurationName.html)
[ISwDMConfigurationMgr::GetConfigurationByName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationByName.html)

## Availability

SOLIDWORKS Document Manager API 2004 SP1
