---
title: "MaterialType Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "MaterialType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialType.html"
---

# MaterialType Property (ICWBoltConnector)

Gets or sets the material type.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Integer

instance.MaterialType = value

value = instance.MaterialType
```

### C#

```csharp
System.int MaterialType {get; set;}
```

### C++/CLI

```cpp
property System.int MaterialType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of bolt material as defined in [swsBoltMaterialType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsBoltMaterialType_e.html)

## VBA Syntax

See [CWBoltConnector::MaterialType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~MaterialType.html).

## Examples

[Create and Edit Bolt and Pin Connectors (VBA)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VB.htm)
[Create and Edit Bolt and Pin Connectors (VB.NET)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_VBNET.htm)
[Create and Edit Bolt and Pin Connectors (C#)](Create_and_Edit_Bolt_and_Pin_Connectors_Example_CSharp.htm)

## Remarks

If this property is set to custom, then you must set ICWBoltConnector::PoissonsRatio, ThermalCoefficient, or YoungModulus.

| If this property is set to... | Then set ... |
| --- | --- |
| Custom | ICWBoltConnector::PoissonsRatio , ICWBoltConnector::ThermalCoefficient , or ICWBoltConnector::YoungModulus |
| Library | ICWBoltConnector::SetLibraryMaterial |

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)
[ICWBoltConnector::GetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~GetLibraryMaterial.html)
[ICWBoltConnector::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~SetLibraryMaterial.html)
[ICWBoltConnector::IncludeMass Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~IncludeMass.html)
[ICWBoltConnector::MassValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MassValue.html)
[ICWBoltConnector::MaterialSource Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialSource.html)
[ICWBoltConnector::MaterialUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~MaterialUnit.html)
[ICWBoltConnector::PoissonsRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~PoissonsRatio.html)
[ICWBoltConnector::ThermalCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ThermalCoefficient.html)
[ICWBoltConnector::YoungModulus Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~YoungModulus.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
