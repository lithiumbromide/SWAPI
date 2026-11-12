---
title: "SketchOffsetEntities Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchOffsetEntities"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchOffsetEntities.html"
---

# SketchOffsetEntities Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchOffsetEntities](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchOffsetEntities.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::SketchOffsetEntities](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchOffsetEntities.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
