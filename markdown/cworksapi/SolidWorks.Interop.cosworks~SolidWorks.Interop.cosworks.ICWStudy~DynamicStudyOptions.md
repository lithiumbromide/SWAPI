---
title: "DynamicStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "DynamicStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DynamicStudyOptions.html"
---

# DynamicStudyOptions Property (ICWStudy)

Gets the options for this dynamic study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DynamicStudyOptions As CWDynamicStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWDynamicStudyOptions

value = instance.DynamicStudyOptions
```

### C#

```csharp
CWDynamicStudyOptions DynamicStudyOptions {get;}
```

### C++/CLI

```cpp
property CWDynamicStudyOptions^ DynamicStudyOptions {
   CWDynamicStudyOptions^ get();
}
```

### Property Value

[Dynamic study options](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicStudyOptions.html)

## VBA Syntax

See [CWStudy::DynamicStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~DynamicStudyOptions.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
