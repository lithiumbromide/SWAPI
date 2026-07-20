---
title: "IVersionHistory Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IVersionHistory"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IVersionHistory.html"
---

# IVersionHistory Method (IModelDoc2)

Gets an array of strings indicating the versions in which this model document was saved, including the SOLIDWORKS version in which the model document is currently opened and which is the last value returned in the array.

## Syntax

### Visual Basic (Declaration)

```vb
Function IVersionHistory() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.String

value = instance.IVersionHistory()
```

### C#

```csharp
System.string IVersionHistory()
```

### C++/CLI

```cpp
System.String^ IVersionHistory();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

Array of strings showing the history of the document

## VBA Syntax

See

[ModelDoc2::IVersionHistory](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IVersionHistory.html)

.

## Examples

[Document Version History (C++)](Document_Version_History_Example_CPlusPlus_COM.htm)

## Remarks

There is one array entry for each major release of the SOLIDWORKS software in which the document has been saved. The format for each entry is a major release code followed by one or more minor release codes separated by commas:

<major release code>[<minor release code>]

- or -

<major release code>[<minor release code>,<minor release code>...]

where <major release code> equals a number that remains constant through a major release of the SOLIDWORKS software. For example, the following values are returned based on the corresponding major SOLIDWORKS version:

(Table)=========================================================

| SOLIDWORKS Release | Version Number |
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
| SOLIDWORKS 2018 | 11000 |
| SOLIDWORKS 2019 | 12000 |
| SOLIDWORKS 2020 | 13000 |
| SOLIDWORKS 2021 | 14000 |
| SOLIDWORKS 2022 | 15000 |
| SOLIDWORKS 2023 | 16000 |
| SOLIDWORKS 2024 | 17000 |
| SOLIDWORKS 2025 | 18000 |

The <minor release code> equals the year and day of manufacture of a saving version (for example, 1997/320).

Use[IModelDoc2::IGetVersionHistoryCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IGetVersionHistoryCount.html)before callingkadov_tag{{<spaces>}}this method to get the size of the array needed by this method.

To get the version in which a model document was last saved, use[ISldWorks::VersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)

[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

[IModelDoc2::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~VersionHistory.html)

[ISldWorks::RevisionNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.html)

[IModelDocExtension::IsFutureVersion Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsFutureVersion.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
