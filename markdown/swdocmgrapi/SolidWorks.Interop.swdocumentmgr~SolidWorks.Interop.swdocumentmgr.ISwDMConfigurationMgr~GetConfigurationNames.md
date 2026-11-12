---
title: "GetConfigurationNames Method (ISwDMConfigurationMgr)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfigurationMgr"
member: "GetConfigurationNames"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationNames.html"
---

# GetConfigurationNames Method (ISwDMConfigurationMgr)

Obsolete. Superseded by [ISwDMConfigurationMgr2::GetConfigurationNames2](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfigurationMgr2~GetConfigurationNames2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurationNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfigurationMgr
Dim value As System.Object

value = instance.GetConfigurationNames()
```

### C#

```csharp
System.object GetConfigurationNames()
```

### C++/CLI

```cpp
System.Object^ GetConfigurationNames();
```

### Return Value

Names of the configurations

## VBA Syntax

See [SwDMConfigurationMgr::GetConfigurationNames](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfigurationMgr~GetConfigurationNames.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Write Parasolid Partition Stream to File (C++)](Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm)
[Get Whether Component Is Envelope and Excluded from BOM (C#)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm)
[Get Whether Component Is Envelope and Excluded from BOM (VB.NET)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm)
[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)

## Remarks

Call this method before calling [ISwDMConfigurationMgr::GetConfigurationByName](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr~GetConfigurationByName.html).

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
