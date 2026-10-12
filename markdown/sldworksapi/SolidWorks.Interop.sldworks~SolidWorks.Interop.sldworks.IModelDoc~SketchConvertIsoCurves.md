---
title: "SketchConvertIsoCurves Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchConvertIsoCurves"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchConvertIsoCurves.html"
---

# SketchConvertIsoCurves Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchConvertIsoCurves](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchConvertIsoCurves.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchConvertIsoCurves( _
   ByVal PercentRatio As System.Double, _
   ByVal VORuDir As System.Boolean, _
   ByVal DoConstrain As System.Boolean, _
   ByVal SkipHoles As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim PercentRatio As System.Double
Dim VORuDir As System.Boolean
Dim DoConstrain As System.Boolean
Dim SkipHoles As System.Boolean

instance.SketchConvertIsoCurves(PercentRatio, VORuDir, DoConstrain, SkipHoles)
```

### C#

```csharp
void SketchConvertIsoCurves(
   System.double PercentRatio,
   System.bool VORuDir,
   System.bool DoConstrain,
   System.bool SkipHoles
)
```

### C++/CLI

```cpp
void SketchConvertIsoCurves(
   System.double PercentRatio,
   System.bool VORuDir,
   System.bool DoConstrain,
   System.bool SkipHoles
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PercentRatio`:
- `VORuDir`:
- `DoConstrain`:
- `SkipHoles`:

## VBA Syntax

See [ModelDoc::SketchConvertIsoCurves](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchConvertIsoCurves.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
