---
title: "GetVersion Method (ISwDMDocument)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMDocument"
member: "GetVersion"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html"
---

# GetVersion Method (ISwDMDocument)

Gets the version of this document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVersion() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMDocument
Dim value As System.Integer

value = instance.GetVersion()
```

### C#

```csharp
System.int GetVersion()
```

### C++/CLI

```cpp
System.int GetVersion();
```

### Return Value

Version

## VBA Syntax

See [SwDMDocument::GetVersion](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMDocument~GetVersion.html).

## Examples

[Get Configuration Information (C#)](Get_Configuration_Information_Example_CSharp.htm)
[Get Configuration Information (VB.NET)](Get_Configuration_Information_Example_VBNET.htm)

## Remarks

| Major SOLIDWORKS Release | Return Value |
| --- | --- |
| SOLIDWORKS 2000 | 1500 |
| SOLIDWORKS 2001 | 1750 |
| SOLIDWORKS 2001Plus | 1950 |
| SOLIDWORKS 2003 | 2200 |
| SOLIDWORKS 2004 | 2500 |
| SOLIDWORKS 2005 | 2800 |
| SOLIDWORKS 2006 | 3100 |
| SOLIDWORKS 2007 | 3400 |
| SOLIDWORKS 2008 | 3800 |
| SOLIDWORKS 2009 | 4100 |
| SOLIDWORKS 2010 | 4400 |
| SOLIDWORKS 2011 | 4700 |
| SOLIDWORKS 2012 | 5000 |
| SOLIDWORKS 2013 | 6000 |
| SOLIDWORKS 2014 | 7000 |
| SOLIDWORKS 2015 | 8000 |
| SOLIDWORKS 2016 | 9000 |
| SOLIDWORKS 2017 | 10000 |
| SOLIDWORKS 2018 | 11000 |
| SOLIDWORKS 2019 | 12000 |
| SOLIDWORKS 2020 | 13000 |
| SOLIDWORKS 2021 | 14000 |
| SOLIDWORKS 2022 | 15000 |
| SOLIDWORKS 2023 | 16000 |
| SOLIDWORKS 2024 | 17000 |
| SOLIDWORKS 2025 | 18000 |
| SOLIDWORKS 2026 | 19000 |

See [ISwDMDocument::GetXmlStream](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMDocument~GetXmlStream.html) and [ISwDMConfiguration::GetMassProperties](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMConfiguration~GetMassProperties.html) for additional version restrictions.

## See Also

[ISwDMDocument Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument.html)
[ISwDMDocument Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument_members.html)
[ISwDMApplication::GetLatestSupportedFileVersion Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetLatestSupportedFileVersion.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
