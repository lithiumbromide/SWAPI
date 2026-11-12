---
title: "SketchOffset2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchOffset2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchOffset2.html"
---

# SketchOffset2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchOffset2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchOffset2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchOffset2( _
   ByVal Offset As System.Double, _
   ByVal BothDirections As System.Boolean, _
   ByVal Chain As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Offset As System.Double
Dim BothDirections As System.Boolean
Dim Chain As System.Boolean
Dim value As System.Boolean

value = instance.SketchOffset2(Offset, BothDirections, Chain)
```

### C#

```csharp
System.bool SketchOffset2(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

### C++/CLI

```cpp
System.bool SketchOffset2(
   System.double Offset,
   System.bool BothDirections,
   System.bool Chain
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Offset`:
- `BothDirections`:
- `Chain`:

## VBA Syntax

See [ModelDoc::SketchOffset2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchOffset2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
