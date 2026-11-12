---
title: "GetPartNumberStreamFile Method (ISwDMDocument15)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument15"
member: "GetPartNumberStreamFile"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15~GetPartNumberStreamFile.html"
---

# GetPartNumberStreamFile Method (ISwDMDocument15)

Gets the name of the XML file generated when uploading a model to [3D Content Central](http://www.3dcontentcentral.com). The XML file is only generated if the model has a design table with a part number column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPartNumberStreamFile( _
   ByVal xmlFileName As System.String _
) As SwDmXmlDataError
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument15
Dim xmlFileName As System.String
Dim value As SwDmXmlDataError

value = instance.GetPartNumberStreamFile(xmlFileName)
```

### C#

```csharp
SwDmXmlDataError GetPartNumberStreamFile(
   System.string xmlFileName
)
```

### C++/CLI

```cpp
SwDmXmlDataError GetPartNumberStreamFile(
   System.String^ xmlFileName
)
```

### Parameters

- `xmlFileName`: Name of XML file

### Return Value

Status as defined in [swDmXmlDataError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmXmlDataError.html)

## VBA Syntax

See [SwDMDocument15::GetPartNumberStreamFile](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument15~GetPartNumberStreamFile.html).

## Remarks

Use the SOLIDWORKS Configuration Publisher to upload a model that has a design table with a part number column and other control values. (To open the Configuration Publisher in SOLIDWORKS, open a model document, right-click the top-level configuration name in the ConfigurationManager, and select **Configuration Publisher**.)

## See Also

[ISwDMDocument15 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15.html)
[ISwDMDocument15 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument15_members.html)
[ISwDMDocumentManager14::Get3DCCGenericStreamFile Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCGenericStreamFile.html)
[ISwDMDocumentManager14::Get3DCCStreamFile Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument14~Get3DCCStreamFile.html)

## Availability

SOLIDWORKS Document Manager API 2011 SP0
