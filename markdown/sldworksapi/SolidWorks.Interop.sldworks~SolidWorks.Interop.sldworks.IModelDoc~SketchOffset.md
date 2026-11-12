---
title: "SketchOffset Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchOffset.html"
---

# SketchOffset Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchOffset.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchOffset( _
   ByVal Offset As System.Double, _
   ByVal ContourMode As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Offset As System.Double
Dim ContourMode As System.Boolean

instance.SketchOffset(Offset, ContourMode)
```

### C#

```csharp
void SketchOffset(
   System.double Offset,
   System.bool ContourMode
)
```

### C++/CLI

```cpp
void SketchOffset(
   System.double Offset,
   System.bool ContourMode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`:
- `ContourMode`:

## VBA Syntax

See [ModelDoc::SketchOffset](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchOffset.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
