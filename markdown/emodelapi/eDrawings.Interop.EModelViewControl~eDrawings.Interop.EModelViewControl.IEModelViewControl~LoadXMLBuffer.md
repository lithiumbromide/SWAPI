---
title: "LoadXMLBuffer Method (IEModelViewControl)"
project: "eDrawings API Help"
interface: "IEModelViewControl"
member: "LoadXMLBuffer"
kind: "method"
source: "emodelapi/eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl~LoadXMLBuffer.html"
---

# LoadXMLBuffer Method (IEModelViewControl)

Loads the model from data from an XML source.

## Syntax

### Visual Basic (Declaration)

```vb
Sub LoadXMLBuffer( _
   ByVal XMLDoc As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEModelViewControl
Dim XMLDoc As System.Object

instance.LoadXMLBuffer(XMLDoc)
```

### C#

```csharp
void LoadXMLBuffer(
   System.object XMLDoc
)
```

### C++/CLI

```cpp
void LoadXMLBuffer(
   System.Object^ XMLDoc
)
```

### Parameters

- `XMLDoc`: Pointer to the an MSXML DOMDocument object (MSXML2.DOMDocument40)

## VBA Syntax

See [EModelViewControl::LoadXMLBuffer](ms-its:emodelapivb6.chm::/EModelView~EModelViewControl~LoadXMLBuffer.html).

## Examples

```vb
<TITLE>eDrawings 2005 - [square]</TITLE><HTML>
<BODY>
<OBJECT ID="EV" classid="clsid:22945A69-1191-4DCF-9E6F-409BDE94D101" codebase="http://www.solidworks.com/plugins/edrawings/ " width="100%" height="99%"><PARAM name="FullUI" value="1"/></OBJECT>
<font color="#000000" face="Times, Verdana, Helvetica, Arial">Internet Explorer 5.5 or higher is required to view this <a href="http://www.solidworks.com/edrawings">eDrawings</a> file.      Generated with eDrawings 2005.</font>
<SCRIPT>function edwsc(){if(event.srcElement.readyState=="complete")EV.LoadXMLBuffer(event.srcElement.XMLDocument);}</SCRIPT>
<XML ID="EDW1" onreadystatechange="edwsc()">
<EDWData>
<!-- Embedded EDrawing data saved as text --!>  See IPDMWDocument::GetEmbeddedEDWAsBase64
</EDWData>
</XML>
</BODY>
</HTML>
```

## See Also

[IEModelViewControl Interface](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html)
[IEModelViewControl Members](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl_members.html)

## Availability

eDrawings API 2005 SP0
