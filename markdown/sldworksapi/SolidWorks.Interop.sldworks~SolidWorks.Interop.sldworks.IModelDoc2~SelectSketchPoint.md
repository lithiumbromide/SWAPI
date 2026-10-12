---
title: "SelectSketchPoint Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectSketchPoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectSketchPoint.html"
---

# SelectSketchPoint Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::SelectSketchPoint](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectSketchPoint.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
