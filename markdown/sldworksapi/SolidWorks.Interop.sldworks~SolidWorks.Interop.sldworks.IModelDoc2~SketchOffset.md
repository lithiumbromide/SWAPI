---
title: "SketchOffset Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffset.html"
---

# SketchOffset Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::SketchOffset2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchOffset2.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::SketchOffset](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchOffset.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
