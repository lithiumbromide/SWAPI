---
title: "SelectSketchLine Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectSketchLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectSketchLine.html"
---

# SelectSketchLine Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectSketchLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectSketchLine.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectSketchLine( _
   ByVal X0 As System.Double, _
   ByVal Y0 As System.Double, _
   ByVal Inc0 As System.Integer, _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Inc1 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim X0 As System.Double
Dim Y0 As System.Double
Dim Inc0 As System.Integer
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Inc1 As System.Integer

instance.SelectSketchLine(X0, Y0, Inc0, X1, Y1, Inc1)
```

### C#

```csharp
void SelectSketchLine(
   System.double X0,
   System.double Y0,
   System.int Inc0,
   System.double X1,
   System.double Y1,
   System.int Inc1
)
```

### C++/CLI

```cpp
void SelectSketchLine(
   System.double X0,
   System.double Y0,
   System.int Inc0,
   System.double X1,
   System.double Y1,
   System.int Inc1
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X0`:
- `Y0`:
- `Inc0`:
- `X1`:
- `Y1`:
- `Inc1`:

## VBA Syntax

See [ModelDoc::SelectSketchLine](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectSketchLine.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
