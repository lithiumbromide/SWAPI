---
title: "CustomPropertyManager Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "CustomPropertyManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html"
---

# CustomPropertyManager Property (IModelDocExtension)

Gets the custom properties for this document or configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CustomPropertyManager( _
   ByVal ConfigName As System.String _
) As CustomPropertyManager
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ConfigName As System.String
Dim value As CustomPropertyManager

value = instance.CustomPropertyManager(ConfigName)
```

### C#

```csharp
CustomPropertyManager CustomPropertyManager(
   System.string ConfigName
) {get;}
```

### C++/CLI

```cpp
property CustomPropertyManager^ CustomPropertyManager {
   CustomPropertyManager^ get(System.String^ ConfigName);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of configuration

### Property Value

[ICustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager.html) object

## VBA Syntax

See [ModelDocExtension::CustomPropertyManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~CustomPropertyManager.html).

## Examples

[Get Custom Properties of Referenced Part (C#)](Get_Custom_Properties_of_Referenced_Part_Example_CSharp.htm)
[Get Custom Properties of Referenced Part (VB.NET)](Get_Custom_Properties_of_Referenced_Part_Example_VBNET.htm)
[Get Custom Properties of Referenced Part (VBA)](Get_Custom_Properties_of_Referenced_Part_Example_VB.htm)

## Remarks

File custom information is stored in the document file. It can be:

- General to the file, in which case there is a single value whatever the model's configuration

- or -

- Configuration-specific, in which case a different value may be set for each configuration in the model

To access a general custom information value, set the configuration argument to an empty string. To get a document-level property, pass an empty string ("") to the configuration argument.

As per Microsoft recommendations for OLE support, the file summary information for SOLIDWORKS documents is written as an OLE property set into a stream named "\005Summary Information" off the root storage of the SOLIDWORKS document's compound file.

NOTE: MFC does not currently provide classes that manage summary information. However, the DRAWCLI application shipped with Visual C++ includes a sample implementation, in the form of the class CSummInfo, that you can use as an example when implementing your own. This class is used by the document class CDrawDoc. DRAWCLI also includes property pages for displaying and modifying Summary Information.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IConfiguration::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.html)
[IFeature::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CustomPropertyManager.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
