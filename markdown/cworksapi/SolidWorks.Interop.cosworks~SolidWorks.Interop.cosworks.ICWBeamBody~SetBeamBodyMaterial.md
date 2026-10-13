---
title: "SetBeamBodyMaterial Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "SetBeamBodyMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetBeamBodyMaterial.html"
---

# SetBeamBodyMaterial Method (ICWBeamBody)

Sets the material for the beam for analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetBeamBodyMaterial( _
   ByVal RetVal As CWMaterial _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim RetVal As CWMaterial
Dim value As System.Integer

value = instance.SetBeamBodyMaterial(RetVal)
```

### C#

```csharp
System.int SetBeamBodyMaterial(
   CWMaterial RetVal
)
```

### C++/CLI

```cpp
System.int SetBeamBodyMaterial(
   CWMaterial^ RetVal
)
```

### Parameters

- `RetVal`: [Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html)

### Return Value

Error or warning as defined in [swsMaterialErrorWarning_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialErrorWarning_e.html)

## VBA Syntax

See [CWBeamBody::SetBeamBodyMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~SetBeamBodyMaterial.html).

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::GetBeamBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetBeamBodyMaterial.html)
[ICWBeamBody::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetDefaultMaterial.html)
[ICWBeamBody::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetLibraryMaterial.html)
[ICWBeamBody::SetFavMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetFavMaterial.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
