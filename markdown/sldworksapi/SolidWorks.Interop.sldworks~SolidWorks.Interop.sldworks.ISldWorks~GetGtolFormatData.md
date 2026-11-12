---
title: "GetGtolFormatData Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetGtolFormatData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFormatData.html"
---

# GetGtolFormatData Method (ISldWorks)

Gets the Gtol format and XML schema versions supported by this version of SOLIDWORKS.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetGtolFormatData( _
   ByRef GtolFormat As System.Integer, _
   ByRef XmlSchemaversion As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim GtolFormat As System.Integer
Dim XmlSchemaversion As System.Integer

instance.GetGtolFormatData(GtolFormat, XmlSchemaversion)
```

### C#

```csharp
void GetGtolFormatData(
   out System.int GtolFormat,
   out System.int XmlSchemaversion
)
```

### C++/CLI

```cpp
void GetGtolFormatData(
   [Out] System.int GtolFormat,
   [Out] System.int XmlSchemaversion
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GtolFormat`: Gtol format as defined by [swGtolFormatType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolFormatType_e.html)
- `XmlSchemaversion`: XML schema version as defined by [swGtolFormatSchemaVersion_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolFormatSchemaVersion_e.html)

## VBA Syntax

See [SldWorks::GetGtolFormatData](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetGtolFormatData.html).

## Remarks

See [Gtol Frame XML Schema](ms-its:sldworksapiprogguide.chm::/Overview/Gtol_Frame_XML_Schema.htm).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetGtolFrameXMLSchema Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetGtolFrameXMLSchema.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
