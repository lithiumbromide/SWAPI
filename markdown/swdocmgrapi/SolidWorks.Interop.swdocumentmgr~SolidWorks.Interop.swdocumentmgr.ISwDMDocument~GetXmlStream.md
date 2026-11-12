---
title: "GetXmlStream Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetXmlStream"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetXmlStream.html"
---

# GetXmlStream Method (ISwDMDocument)

Gets the embedded XML data for this assembly and saves it to an XML document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetXmlStream( _
   ByVal xmlFileName As System.String, _
   ByRef result As SwDmXmlDataError _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim xmlFileName As System.String
Dim result As SwDmXmlDataError

instance.GetXmlStream(xmlFileName, result)
```

### C#

```csharp
void GetXmlStream(
   System.string xmlFileName,
   ref SwDmXmlDataError result
)
```

### C++/CLI

```cpp
void GetXmlStream(
   System.String^ xmlFileName,
   SwDmXmlDataError% result
)
```

### Parameters

- `xmlFileName`: Filename for the XML document
- `result`: Success or error code as defined by [SwDMXmlDataError](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.SwDmXmlDataError.html)

## VBA Syntax

See [SwDMDocument::GetXmlStream](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetXmlStream.html).

## Examples

[Get XML Stream (C#)](Get_XML_Stream_Example_CSharp.htm)
[Get XML Stream (VB.NET)](Get_XML_Stream_Example_VBNET.htm)
[Get External References for Part (C#)](Get_External_References_for_Part_Example_CSharp.htm)
[Get External References for Part (VB.NET)](Get_External_References_for_Part_Example_VBNET.htm)

## Remarks

This method only returns data for documents created using SOLIDWORKS 2003 (Version 2200) and later. To get the version of a document, use [ISwDMDocument::GetVersion](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html).

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
