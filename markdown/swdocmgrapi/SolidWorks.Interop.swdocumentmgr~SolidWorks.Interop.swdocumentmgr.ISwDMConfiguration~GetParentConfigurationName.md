---
title: "GetParentConfigurationName Method (ISwDMConfiguration)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration"
member: "GetParentConfigurationName"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.html"
---

# GetParentConfigurationName Method (ISwDMConfiguration)

Gets the name of the parent configuration for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParentConfigurationName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration
Dim value As System.String

value = instance.GetParentConfigurationName()
```

### C#

```csharp
System.string GetParentConfigurationName()
```

### C++/CLI

```cpp
System.String^ GetParentConfigurationName();
```

### Return Value

Name of the parent configuration or NULL if no parent configuration exists

## VBA Syntax

See [SwDMConfiguration::GetParentConfigurationName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration~GetParentConfigurationName.html).

## Examples

[Write Parasolid Partition Stream to File (C#)](Write_Parasolid_Partition_Stream_to_File_Example_CSharp.htm)
[Write Parasolid Partition Stream to File (VB.NET)](Write_Parasolid_Partition_Stream_to_File_Example_VBNET.htm)
[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## See Also

[ISwDMConfiguration Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration.html)
[ISwDMConfiguration Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration_members.html)
[ISwDMComponent::ConfigurationName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.html)
[ISwDMConfiguration7::Name2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.html)
[ISwDMConfigurationMgr::GetActiveConfigurationName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetActiveConfigurationName.html)
[ISwDMConfigurationMgr::GetConfigurationByName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationByName.html)
[ISwDMConfigurationMgr::GetConfigurationNames Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationNames.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
