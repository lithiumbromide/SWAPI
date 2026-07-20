---
title: "GetCreatedVersion Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetCreatedVersion"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetCreatedVersion.html"
---

# GetCreatedVersion Method (IFeature)

Gets the SOLIDWORKS version number in which the selected feature was created.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCreatedVersion() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.GetCreatedVersion()
```

### C#

```csharp
System.int GetCreatedVersion()
```

### C++/CLI

```cpp
System.int GetCreatedVersion();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Return Value

SOLIDWORKS version number in which feature was createdParamDesc(see**Remarks**)

## VBA Syntax

See

[Feature::GetCreatedVersion](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetCreatedVersion.html)

.

## Examples

[Get SOLIDWORKS Version Number in which Feature Was Created (VBA)](Get_SOLIDWORKS_Version_Number_in_Which_Feature_Was_Created_Example_VB.htm)

## Remarks

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

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

To get the SOLIDWORKS version number in which the feature was last modified, use[IFeature::GetModifiedVersion](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetModifiedVersion.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)

[IModelDoc2::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IVersionHistory.html)

[IModelDoc2::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~VersionHistory.html)

[ISldWorks::IVersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.html)

[ISldWorks::VersionHistory Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.html)

## Availability

SOLIDWORKS 2006 FCS, Revision number 14.0
