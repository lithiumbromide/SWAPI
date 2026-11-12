---
title: "MoldDraftAnalysis Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "MoldDraftAnalysis"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MoldDraftAnalysis.html"
---

# MoldDraftAnalysis Method (IModelDoc2)

Performs a mold draft analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Sub MoldDraftAnalysis( _
   ByVal Angle As System.Double, _
   ByVal Options As System.Integer, _
   ByVal Colors As System.Object, _
   ByVal Shows As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Angle As System.Double
Dim Options As System.Integer
Dim Colors As System.Object
Dim Shows As System.Integer

instance.MoldDraftAnalysis(Angle, Options, Colors, Shows)
```

### C#

```csharp
void MoldDraftAnalysis(
   System.double Angle,
   System.int Options,
   System.object Colors,
   System.int Shows
)
```

### C++/CLI

```cpp
void MoldDraftAnalysis(
   System.double Angle,
   System.int Options,
   System.Object^ Colors,
   System.int Shows
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Reference draft angle
- `Options`: Analysis options as defined in [swDraftAnalysisOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisOptions_e.html)
- `Colors`: Array of 4 colors (positive draft, negative draft, no draft, straddled faces)
- `Shows`: Show each draft type as defined in [swDraftAnalysisShow_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDraftAnalysisShow_e.html)

## VBA Syntax

See [ModelDoc2::MoldDraftAnalysis](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~MoldDraftAnalysis.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
