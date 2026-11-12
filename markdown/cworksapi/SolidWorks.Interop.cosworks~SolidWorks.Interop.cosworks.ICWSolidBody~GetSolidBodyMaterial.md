---
title: "GetSolidBodyMaterial Method (ICWSolidBody)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: "GetSolidBodyMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~GetSolidBodyMaterial.html"
---

# GetSolidBodyMaterial Method (ICWSolidBody)

Gets the material applied to the solid body for analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSolidBodyMaterial() As CWMaterial
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
Dim value As CWMaterial

value = instance.GetSolidBodyMaterial()
```

### C#

```csharp
CWMaterial GetSolidBodyMaterial()
```

### C++/CLI

```cpp
CWMaterial^ GetSolidBodyMaterial();
```

### Return Value

[Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html) applied to the solid body or NULL if no material object was applied

## VBA Syntax

See [CWSolidBody::GetSolidBodyMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody~GetSolidBodyMaterial.html).

## See Also

[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)
[ICWSolidBody::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~GetDefaultMaterial.html)
[ICWSolidBody::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetLibraryMaterial.html)
[ICWSolidBody::SetSolidBodyMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody~SetSolidBodyMaterial.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
