---
title: "GetConfigurationByName Method (ISwDMConfigurationMgr)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfigurationMgr"
member: "GetConfigurationByName"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationByName.html"
---

# GetConfigurationByName Method (ISwDMConfigurationMgr)

Obsolete. Superseded by [ISwDMConfigurationMgr2::GetConfigurationByName2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationByName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationByName( _
   ByVal ConfigurationName As System.String _
) As SwDMConfiguration
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfigurationMgr
Dim ConfigurationName As System.String
Dim value As SwDMConfiguration

value = instance.GetConfigurationByName(ConfigurationName)
```

### C#

```csharp
SwDMConfiguration GetConfigurationByName(
   System.string ConfigurationName
)
```

### C++/CLI

```cpp
SwDMConfiguration^ GetConfigurationByName(
   System.String^ ConfigurationName
)
```

### Parameters

- `ConfigurationName`: Name of configuration to get (see **Remarks**)

### Return Value

Pointer to an [ISwDMConfiguration](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration.html) object

## VBA Syntax

See [SwDMConfigurationMgr::GetConfigurationByName](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfigurationMgr~GetConfigurationByName.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Write Parasolid Partition Stream to File (C++)](Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm)
[Get Whether Component Is Envelope and Excluded from BOM (C#)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm)
[Get Whether Component Is Envelope and Excluded from BOM (VB.NET)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm)
[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)

## Remarks

Call [ISwDMConfigurationMgr::GetConfigurationNames](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationNames.html) before calling this method.

## See Also

[ISwDMConfigurationMgr Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr.html)
[ISwDMConfigurationMgr Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr_members.html)
[ISwDMComponent::ConfigurationName Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent~ConfigurationName.html)
[ISwDMConfiguration::GetParentConfigurationName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration~GetParentConfigurationName.html)
[ISwDMConfiguration7::Name2 Property](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration7~Name2.html)
[ISwDMConfigurationMgr::GetActiveConfigurationName Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetActiveConfigurationName.html)
[ISwDMConfigurationMgr::GetConfigurationCount Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationCount.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
