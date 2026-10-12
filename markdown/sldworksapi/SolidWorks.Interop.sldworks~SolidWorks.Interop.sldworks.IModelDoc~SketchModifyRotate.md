---
title: "SketchModifyRotate Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchModifyRotate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchModifyRotate.html"
---

# SketchModifyRotate Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchModifyRotate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchModifyRotate.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchModifyRotate( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim Angle As System.Double

instance.SketchModifyRotate(CenterX, CenterY, Angle)
```

### C#

```csharp
void SketchModifyRotate(
   System.double CenterX,
   System.double CenterY,
   System.double Angle
)
```

### C++/CLI

```cpp
void SketchModifyRotate(
   System.double CenterX,
   System.double CenterY,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterX`:
- `CenterY`:
- `Angle`:

## VBA Syntax

See [ModelDoc::SketchModifyRotate](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchModifyRotate.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
