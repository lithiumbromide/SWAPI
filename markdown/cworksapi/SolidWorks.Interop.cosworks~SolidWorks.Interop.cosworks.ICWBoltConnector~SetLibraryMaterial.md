---
title: "SetLibraryMaterial Method (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "SetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetLibraryMaterial.html"
---

# SetLibraryMaterial Method (ICWBoltConnector)

Sets the material for this bolt connector.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetLibraryMaterial( _
   ByVal SMaterialLibName As System.String, _
   ByVal SMaterialName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim SMaterialLibName As System.String
Dim SMaterialName As System.String

instance.SetLibraryMaterial(SMaterialLibName, SMaterialName)
```

### C#

```csharp
void SetLibraryMaterial(
   System.string SMaterialLibName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
void SetLibraryMaterial(
   System.String^ SMaterialLibName,
   System.String^ SMaterialName
)
```

### Parameters

- `SMaterialLibName`: Path to the material library
- `SMaterialName`: Material name in the library

## VBA Syntax

See [CWBoltConnector::SetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~SetLibraryMaterial.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::GetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetLibraryMaterial.html)
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
