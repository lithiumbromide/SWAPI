---
title: "GetActiveConfigurationName Method (ISwDMConfigurationMgr)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfigurationMgr"
member: "GetActiveConfigurationName"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetActiveConfigurationName.html"
---

# GetActiveConfigurationName Method (ISwDMConfigurationMgr)

Gets the name of the active configuration in the document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActiveConfigurationName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfigurationMgr
Dim value As System.String

value = instance.GetActiveConfigurationName()
```

### C#

```csharp
System.string GetActiveConfigurationName()
```

### C++/CLI

```cpp
System.String^ GetActiveConfigurationName();
```

### Return Value

Name of the active configuration

## VBA Syntax

See [SwDMConfigurationMgr::GetActiveConfigurationName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfigurationMgr~GetActiveConfigurationName.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## See Also

[ISwDMConfigurationMgr Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr.html)
[ISwDMConfigurationMgr Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr_members.html)
[ISwDMComponent::ConfigurationName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.html)
[ISwDMConfiguration::GetParentConfigurationName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.html)
[ISwDMConfiguration7::Name2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.html)
[ISwDMConfigurationMgr::GetConfigurationByName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationByName.html)
[ISwDMConfigurationMgr::GetConfigurationCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationCount.html)
[ISwDMConfigurationMgr::GetConfigurationNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationNames.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
