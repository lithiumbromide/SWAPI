---
title: "VersionHistory Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "VersionHistory"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.html"
---

# VersionHistory Method (ISldWorks)

Gets a list of strings indicating the versions in which a model was saved.

## Syntax

### Visual Basic (Declaration)

```vb
Function VersionHistory( _
   ByVal FileName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Object

value = instance.VersionHistory(FileName)
```

### C#

```csharp
System.object VersionHistory(
   System.string FileName
)
```

### C++/CLI

```cpp
System.Object^ VersionHistory(
   System.String^ FileName
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `FileName`: Full path name of the model for which to get the version history

### Return Value

Array of strings containing the version history

## VBA Syntax

See

[SldWorks::VersionHistory](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~VersionHistory.html)

.

## Examples

[Get Version History (VBA)](Get_Version_History_Example_VB.htm)

## Remarks

This information is retrieved from the file on disk, not from the open document.

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

To get the version history of a document that is currently open, use[IModelDoc2::VersionHistory](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~VersionHistory.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)

[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.html)

[ISldWorks::RevisionNumber Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.html)

[ISldWorks::GetBuildNumbers2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetBuildNumbers2.html)

[IModelDocExtension::IsFutureVersion Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsFutureVersion.html)

## Availability

SOLIDWORKS 98Plus, datecode 1998319
