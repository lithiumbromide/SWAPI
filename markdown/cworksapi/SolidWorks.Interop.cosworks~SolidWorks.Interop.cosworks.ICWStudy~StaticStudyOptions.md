---
title: "StaticStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "StaticStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~StaticStudyOptions.html"
---

# StaticStudyOptions Property (ICWStudy)

Gets the options for this static study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StaticStudyOptions As CWStaticStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWStaticStudyOptions

value = instance.StaticStudyOptions
```

### C#

```csharp
CWStaticStudyOptions StaticStudyOptions {get;}
```

### C++/CLI

```cpp
property CWStaticStudyOptions^ StaticStudyOptions {
   CWStaticStudyOptions^ get();
}
```

### Property Value

[Static study options](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html)

## VBA Syntax

See [CWStudy::StaticStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~StaticStudyOptions.html).

## Examples

See the [ICWStaticStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html) examples.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
