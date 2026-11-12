---
title: "SetLibraryMaterial Method (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "SetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SetLibraryMaterial.html"
---

# SetLibraryMaterial Method (ICWPinConnector)

Sets the material for this pin connector.

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
Dim instance As ICWPinConnector
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

See [CWPinConnector::SetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~SetLibraryMaterial.html).

## Remarks

This method is valid only if [ICWPinConnector::IncludeStrengthData](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html) is set to true.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::GetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~GetLibraryMaterial.html)
[ICWPinConnector::MaterialType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialType.html)
[ICWPinConnector::MassValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MassValue.html)
[ICWPinConnector::PoissonsRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PoissonsRatio.html)
[ICWPinConnector::ThermalCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ThermalCoefficient.html)
[ICWPinConnector::YoungModulus Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~YoungModulus.html)
[ICWPinConnector::MaterialUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialUnit.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
