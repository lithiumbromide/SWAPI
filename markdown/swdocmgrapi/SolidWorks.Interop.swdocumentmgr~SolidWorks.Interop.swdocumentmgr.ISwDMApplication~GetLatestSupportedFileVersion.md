---
title: "GetLatestSupportedFileVersion Method (ISwDMApplication)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMApplication"
member: "GetLatestSupportedFileVersion"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication~GetLatestSupportedFileVersion.html"
---

# GetLatestSupportedFileVersion Method (ISwDMApplication)

Gets the latest supported SOLIDWORKS version number that this utility can read.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLatestSupportedFileVersion() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMApplication
Dim value As System.Integer

value = instance.GetLatestSupportedFileVersion()
```

### C#

```csharp
System.int GetLatestSupportedFileVersion()
```

### C++/CLI

```cpp
System.int GetLatestSupportedFileVersion();
```

### Return Value

Latest supported SOLIDWORKS file version number that this utility can read

## VBA Syntax

See [SwDMApplication::GetLatestSupportedFileVersion](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMApplication~GetLatestSupportedFileVersion.html).

## Examples

[Open and Close Document (C++)](Open_and_Close_Document_Example_CPlusCPlus_COM.htm)

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

## See Also

[ISwDMApplication Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication.html)
[ISwDMApplication Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMApplication_members.html)
[ISwDMDocument::GetVersion Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument~GetVersion.html)

## Availability

SOLIDWORKS Document Manager API 2004 FCS
