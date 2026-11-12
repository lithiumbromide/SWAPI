---
title: "StudyResultOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "StudyResultOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~StudyResultOptions.html"
---

# StudyResultOptions Property (ICWStudy)

Gets the result options for this study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StudyResultOptions As CWStudyResultOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWStudyResultOptions

value = instance.StudyResultOptions
```

### C#

```csharp
CWStudyResultOptions StudyResultOptions {get;}
```

### C++/CLI

```cpp
property CWStudyResultOptions^ StudyResultOptions {
   CWStudyResultOptions^ get();
}
```

### Property Value

[Study result options](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudyResultOptions.html)

## VBA Syntax

See [CWStudy::StudyResultOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~StudyResultOptions.html).

## Examples

[Create Linear Dynamic Study (C#)](Create_Dynamic_Harmonic_Study_Example_CSharp.htm)
[Create Linear Dynamic Study (VB.NET)](Create_Dynamic_Harmonic_Study_Example_VBNET.htm)
[Create Linear Dynamic Study (VBA)](Create_Dynamic_Harmonic_Study_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::DropTestResultOptions Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~DropTestResultOptions.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
