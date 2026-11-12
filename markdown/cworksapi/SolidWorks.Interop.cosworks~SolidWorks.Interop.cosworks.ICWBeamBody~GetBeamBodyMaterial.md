---
title: "GetBeamBodyMaterial Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "GetBeamBodyMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetBeamBodyMaterial.html"
---

# GetBeamBodyMaterial Method (ICWBeamBody)

Gets the material applied to the beam for analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBeamBodyMaterial() As CWMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As CWMaterial

value = instance.GetBeamBodyMaterial()
```

### C#

```csharp
CWMaterial GetBeamBodyMaterial()
```

### C++/CLI

```cpp
CWMaterial^ GetBeamBodyMaterial();
```

### Return Value

[Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html)

## VBA Syntax

See [CWBeamBody::GetBeamBodyMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~GetBeamBodyMaterial.html).

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetDefaultMaterial.html)
[ICWBeamBody::SetBeamBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetBeamBodyMaterial.html)
[ICWBeamBody::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetLibraryMaterial.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
