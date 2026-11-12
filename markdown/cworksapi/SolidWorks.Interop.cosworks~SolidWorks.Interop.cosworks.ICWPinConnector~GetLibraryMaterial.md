---
title: "GetLibraryMaterial Method (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "GetLibraryMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~GetLibraryMaterial.html"
---

# GetLibraryMaterial Method (ICWPinConnector)

Gets the material for this pin connector.

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
Dim instance As ICWPinConnector
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

See [CWPinConnector::GetLibraryMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~GetLibraryMaterial.html).

## Examples

See the [ICWPinConnector](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html) examples.

## Remarks

This method is valid only if [ICWPinConnector::IncludeStrengthData](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~IncludeStrengthData.html) is set to true.

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)
[ICWPinConnector::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~SetLibraryMaterial.html)
[ICWPinConnector::MaterialType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialType.html)
[ICWPinConnector::MassValue Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MassValue.html)
[ICWPinConnector::MaterialUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~MaterialUnit.html)
[ICWPinConnector::PoissonsRatio Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~PoissonsRatio.html)
[ICWPinConnector::ThermalCoefficient Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ThermalCoefficient.html)
[ICWPinConnector::YoungModulus Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~YoungModulus.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
