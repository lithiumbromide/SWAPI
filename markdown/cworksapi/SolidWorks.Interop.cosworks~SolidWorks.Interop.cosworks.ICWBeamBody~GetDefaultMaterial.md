---
title: "GetDefaultMaterial Method (ICWBeamBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBeamBody"
member: "GetDefaultMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetDefaultMaterial.html"
---

# GetDefaultMaterial Method (ICWBeamBody)

Gets the CAD material of the beam.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDefaultMaterial() As CWMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBeamBody
Dim value As CWMaterial

value = instance.GetDefaultMaterial()
```

### C#

```csharp
CWMaterial GetDefaultMaterial()
```

### C++/CLI

```cpp
CWMaterial^ GetDefaultMaterial();
```

### Return Value

[Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html)

## VBA Syntax

See [CWBeamBody::GetDefaultMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBeamBody~GetDefaultMaterial.html).

## See Also

[ICWBeamBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody.html)
[ICWBeamBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody_members.html)
[ICWBeamBody::GetBeamBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~GetBeamBodyMaterial.html)
[ICWBeamBody::SetBeamBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetBeamBodyMaterial.html)
[ICWBeamBody::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBeamBody~SetLibraryMaterial.html)

## Availability

SOLIDWORKS Simulation API 2010 SP0
