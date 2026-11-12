---
title: "SolidWorksVersion Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "SolidWorksVersion"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~SolidWorksVersion.html"
---

# SolidWorksVersion Property (IPDMWDocument)

Gets the SOLIDWORKS version of the document.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property SolidWorksVersion As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.Integer

value = instance.SolidWorksVersion
```

### C#

```csharp
System.int SolidWorksVersion {get;}
```

### C++/CLI

```cpp
property System.int SolidWorksVersion {
   System.int get();
}
```

### Property Value

SOLIDWORKS version

## VBA Syntax

See [PDMWDocument::SOLIDWORKSVersion](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~SOLIDWORKSVersion.html).

## Remarks

| Major SOLIDWORKS Release | Version Number |
| --- | --- |
| SOLIDWORKS 95 | 44 |
| SOLIDWORKS 96 | 243 |
| SOLIDWORKS 97 | 483 |
| SOLIDWORKS 97Plus | 629 |
| SOLIDWORKS 98 | 822 |
| SOLIDWORKS 98Plus | 1008 |
| SOLIDWORKS 99 | 1137 |
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

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2005 FCS
