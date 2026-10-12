---
title: "GetGtolFrameXMLSchema Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetGtolFrameXMLSchema"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFrameXMLSchema.html"
---

# GetGtolFrameXMLSchema Method (ISldWorks)

Gets the XML schema for Gtol frame symbol XML.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGtolFrameXMLSchema() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.String

value = instance.GetGtolFrameXMLSchema()
```

### C#

```csharp
System.string GetGtolFrameXMLSchema()
```

### C++/CLI

```cpp
System.String^ GetGtolFrameXMLSchema();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

XML schema for Gtol Frame symbol XML

## VBA Syntax

See [SldWorks::GetGtolFrameXMLSchema](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetGtolFrameXMLSchema.html).

## Remarks

See [Gtol Frame XML Schema](ms-its:sldworksapiprogguide.chm::/Overview/Gtol_Frame_XML_Schema.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IGtolFrame::GetSymbolXml Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetSymbolXml.html)
[IGtolFrame::SetSymbolXml Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetSymbolXml.html)
[ISldWorks::GetGtolFormatData Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFormatData.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
