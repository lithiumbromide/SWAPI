---
title: "ConfigurationManager Property (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "ConfigurationManager"
kind: "property"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~ConfigurationManager.html"
---

# ConfigurationManager Property (ISwDMDocument)

Gets the ConfigurationMgr for this document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ConfigurationManager As SwDMConfigurationMgr
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As SwDMConfigurationMgr

value = instance.ConfigurationManager
```

### C#

```csharp
SwDMConfigurationMgr ConfigurationManager {get;}
```

### C++/CLI

```cpp
property SwDMConfigurationMgr^ ConfigurationManager {
   SwDMConfigurationMgr^ get();
}
```

### Property Value

Pointer to the [ISwDMConfigurationMgr](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfigurationMgr.html) object

## VBA Syntax

See [SwDMDocument::ConfigurationManager](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~ConfigurationManager.html).

## Examples

[Get Current Name of Configuration of Suppressed Component (VB.NET)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_VBNET.htm)
[Get Current Name of Configuration of Suppressed Component (C#)](Get_Current_Name_of_Configuration_of_Suppressed_Component_Example_CSharp.htm)
[Write Parasolid Partition Stream to File (C++)](Write_Parasolid_Partition_Stream_to_File_Example_CPlusPlus_COM.htm)
[Get Whether Component Is Envelope and Excluded from BOM (C#)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_CSharp.htm)
[Get Whether Component Is Envelope and Excluded from BOM (VB.NET)](Get_Whether_Component_Is_Envelope_And_Excluded_From_BOM_Example_VBNET.htm)
[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)

## Remarks

This method returns:

- data for part and assembly documents.
- NULL for drawing documents.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
