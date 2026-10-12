---
title: "SketchChamfer Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SketchChamfer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SketchChamfer.html"
---

# SketchChamfer Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SketchChamfer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SketchChamfer.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchChamfer( _
   ByVal AngleORdist As System.Double, _
   ByVal Dist1 As System.Double, _
   ByVal Options As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim AngleORdist As System.Double
Dim Dist1 As System.Double
Dim Options As System.Integer

instance.SketchChamfer(AngleORdist, Dist1, Options)
```

### C#

```csharp
void SketchChamfer(
   System.double AngleORdist,
   System.double Dist1,
   System.int Options
)
```

### C++/CLI

```cpp
void SketchChamfer(
   System.double AngleORdist,
   System.double Dist1,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AngleORdist`:
- `Dist1`:
- `Options`:

## VBA Syntax

See [ModelDoc::SketchChamfer](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SketchChamfer.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
