---
title: "SelectSketchPoint Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectSketchPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectSketchPoint.html"
---

# SelectSketchPoint Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectSketchPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectSketchPoint.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectSketchPoint( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Incidence As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim X As System.Double
Dim Y As System.Double
Dim Incidence As System.Integer

instance.SelectSketchPoint(X, Y, Incidence)
```

### C#

```csharp
void SelectSketchPoint(
   System.double X,
   System.double Y,
   System.int Incidence
)
```

### C++/CLI

```cpp
void SelectSketchPoint(
   System.double X,
   System.double Y,
   System.int Incidence
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X`:
- `Y`:
- `Incidence`:

## VBA Syntax

See [ModelDoc::SelectSketchPoint](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectSketchPoint.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
