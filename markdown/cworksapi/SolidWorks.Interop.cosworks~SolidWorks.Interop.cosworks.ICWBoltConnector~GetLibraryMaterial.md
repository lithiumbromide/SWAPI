---
title: "GetLibraryMaterial Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "GetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetLibraryMaterial.html"
---

# GetLibraryMaterial Method (ICWBoltConnector)

Gets the material for this bolt connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetLibraryMaterial( _
   ByRef SMaterialLibName As System.String, _
   ByRef SMaterialName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim SMaterialLibName As System.String
Dim SMaterialName As System.String

instance.GetLibraryMaterial(SMaterialLibName, SMaterialName)
```

### C#

```csharp
void GetLibraryMaterial(
   out System.string SMaterialLibName,
   out System.string SMaterialName
)
```

### C++/CLI

```cpp
void GetLibraryMaterial(
   [Out] System.String^ SMaterialLibName,
   [Out] System.String^ SMaterialName
)
```

### Parameters

- `SMaterialLibName`: Path to the material library
- `SMaterialName`: Material name in the library

## VBA Syntax

See [CWBoltConnector::GetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~GetLibraryMaterial.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetLibraryMaterial.html)
[ICWBoltConnector::IncludeMass Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeMass.html)
[ICWBoltConnector::MassValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MassValue.html)
[ICWBoltConnector::MaterialSource Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialSource.html)
[ICWBoltConnector::MaterialType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialType.html)
[ICWBoltConnector::MaterialUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialUnit.html)
[ICWBoltConnector::PoissonsRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PoissonsRatio.html)
[ICWBoltConnector::ThermalCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThermalCoefficient.html)
[ICWBoltConnector::YoungModulus Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~YoungModulus.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
