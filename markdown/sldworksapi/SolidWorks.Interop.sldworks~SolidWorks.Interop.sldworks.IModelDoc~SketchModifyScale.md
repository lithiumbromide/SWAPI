---
title: "SketchModifyScale Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchModifyScale"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchModifyScale.html"
---

# SketchModifyScale Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchModifyScale](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchModifyScale.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SketchModifyScale( _
   ByVal ScaleFactor As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim ScaleFactor As System.Double
Dim value As System.Boolean

value = instance.SketchModifyScale(ScaleFactor)
```

### C#

```csharp
System.bool SketchModifyScale(
   System.double ScaleFactor
)
```

### C++/CLI

```cpp
System.bool SketchModifyScale(
   System.double ScaleFactor
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ScaleFactor`:

## VBA Syntax

See [ModelDoc::SketchModifyScale](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchModifyScale.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
