---
title: "DampingOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "DampingOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DampingOptions.html"
---

# DampingOptions Property (ICWStudy)

Gets the damping options for this study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DampingOptions As CWDampingOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWDampingOptions

value = instance.DampingOptions
```

### C#

```csharp
CWDampingOptions DampingOptions {get;}
```

### C++/CLI

```cpp
property CWDampingOptions^ DampingOptions {
   CWDampingOptions^ get();
}
```

### Property Value

[ICWDampingOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDampingOptions.html)

## VBA Syntax

See [CWStudy::DampingOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~DampingOptions.html).

## Examples

[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
