---
title: "Get3DCCStreamFile Method (ISwDMDocument14)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument14"
member: "Get3DCCStreamFile"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCStreamFile.html"
---

# Get3DCCStreamFile Method (ISwDMDocument14)

Exports an XML file with the 3D Content Central (3DCC) original format configuration rules built into this document by the SOLIDWORKS Configuration Publisher.

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3DCCStreamFile( _
   ByVal xmlFileName As System.String _
) As SwDmXmlDataError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument14
Dim xmlFileName As System.String
Dim value As SwDmXmlDataError

value = instance.Get3DCCStreamFile(xmlFileName)
```

### C#

```csharp
SwDmXmlDataError Get3DCCStreamFile(
   System.string xmlFileName
)
```

### C++/CLI

```cpp
SwDmXmlDataError Get3DCCStreamFile(
   System.String^ xmlFileName
)
```

### Parameters

- `xmlFileName`: Name of file to which to save the configuration rules data

### Return Value

Status as defined in [swDmXmlDataError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmXmlDataError.html)

## VBA Syntax

See [SwDMDocument14::Get3DCCStreamFile](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument14~Get3DCCStreamFile.html).

## Examples

[Get 3D Content Central Stream Files (VB.NET)](Get_3D_Content_Central_Stream_Files_Example_VBNET.htm)
[Get 3D Content Central Stream Files (C#)](Get_3D_Content_Central_Stream_Files_Example_CSharp.htm)

## Remarks

Designers use the SOLIDWORKS Configuration Publisher to build configuration rules into their documents to constrain how the documents are seen by users who download them from [3D Content Central](http://www.3dcontentcentral.com). (To open the Configuration Publisher in SOLIDWORKS, open a document, right-click on the top-level configuration name in the ConfigurationManager, and click **Configuration Publisher**).

Configuration rules are typically functions of the document's design table parameters. These rules specify how to display the document in different configurations. The Configuration Publisher inserts into the document the configuration rules in two formats: original and [generic](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCGenericStreamFile.html).

This method allows user-interface developers to extract configuration rule information in the original format. Developers can then modify the extracted XML file to display the document in a format that differs from the 3D Content Central format.

The Configuration Publisher can also upload documents along with their configuration rules to 3D Content Central. See the 3D Content Central web site to learn more.

## See Also

[ISwDMDocument14 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14.html)
[ISwDMDocument14 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14_members.html)
[ISwDMDocument15::GetPartNumberStreamFile Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetPartNumberStreamFile.html)

## Availability

SOLIDWORKS Document Manager API 2010 SP0
