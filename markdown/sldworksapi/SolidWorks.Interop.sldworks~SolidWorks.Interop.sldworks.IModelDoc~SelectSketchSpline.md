---
title: "SelectSketchSpline Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectSketchSpline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectSketchSpline.html"
---

# SelectSketchSpline Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectSketchSpline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectSketchSpline.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectSketchSpline( _
   ByVal Size As System.Integer, _
   ByVal X0 As System.Double, _
   ByVal Y0 As System.Double, _
   ByVal Inc0 As System.Integer, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Inc1 As System.Integer, _
   ByVal XC As System.Double, _
   ByVal YC As System.Double, _
   ByVal IncC As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Size As System.Integer
Dim X0 As System.Double
Dim Y0 As System.Double
Dim Inc0 As System.Integer
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Inc1 As System.Integer
Dim XC As System.Double
Dim YC As System.Double
Dim IncC As System.Integer

instance.SelectSketchSpline(Size, X0, Y0, Inc0, X1, Y1, Inc1, XC, YC, IncC)
```

### C#

```csharp
void SelectSketchSpline(
   System.int Size,
   System.double X0,
   System.double Y0,
   System.int Inc0,
   System.double X1,
   System.double Y1,
   System.int Inc1,
   System.double XC,
   System.double YC,
   System.int IncC
)
```

### C++/CLI

```cpp
void SelectSketchSpline(
   System.int Size,
   System.double X0,
   System.double Y0,
   System.int Inc0,
   System.double X1,
   System.double Y1,
   System.int Inc1,
   System.double XC,
   System.double YC,
   System.int IncC
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`:
- `X0`:
- `Y0`:
- `Inc0`:
- `X1`:
- `Y1`:
- `Inc1`:
- `XC`:
- `YC`:
- `IncC`:

## VBA Syntax

See [ModelDoc::SelectSketchSpline](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectSketchSpline.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
