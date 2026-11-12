---
title: "SketchOffsetEntities Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchOffsetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities.html"
---

# SketchOffsetEntities Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::SketchOffsetEntities2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchOffsetEntities( _
   ByVal Offset As System.Double, _
   ByVal Flip As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Offset As System.Double
Dim Flip As System.Boolean

instance.SketchOffsetEntities(Offset, Flip)
```

### C#

```csharp
void SketchOffsetEntities(
   System.double Offset,
   System.bool Flip
)
```

### C++/CLI

```cpp
void SketchOffsetEntities(
   System.double Offset,
   System.bool Flip
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`:
- `Flip`:

## VBA Syntax

See [ModelDoc2::SketchOffsetEntities](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchOffsetEntities.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
