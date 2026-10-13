---
title: "SketchModifyTranslate Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchModifyTranslate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchModifyTranslate.html"
---

# SketchModifyTranslate Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchModifyTranslate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchModifyTranslate.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchModifyTranslate( _
   ByVal StartX As System.Double, _
   ByVal StartY As System.Double, _
   ByVal EndX As System.Double, _
   ByVal EndY As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim StartX As System.Double
Dim StartY As System.Double
Dim EndX As System.Double
Dim EndY As System.Double

instance.SketchModifyTranslate(StartX, StartY, EndX, EndY)
```

### C#

```csharp
void SketchModifyTranslate(
   System.double StartX,
   System.double StartY,
   System.double EndX,
   System.double EndY
)
```

### C++/CLI

```cpp
void SketchModifyTranslate(
   System.double StartX,
   System.double StartY,
   System.double EndX,
   System.double EndY
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StartX`:
- `StartY`:
- `EndX`:
- `EndY`:

## VBA Syntax

See [ModelDoc::SketchModifyTranslate](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchModifyTranslate.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
