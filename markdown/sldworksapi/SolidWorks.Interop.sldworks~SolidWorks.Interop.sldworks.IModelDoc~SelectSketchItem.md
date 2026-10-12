---
title: "SelectSketchItem Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectSketchItem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectSketchItem.html"
---

# SelectSketchItem Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectSketchItem](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectSketchItem.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectSketchItem( _
   ByVal SelOpt As System.Integer, _
   ByVal Name As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim SelOpt As System.Integer
Dim Name As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean

value = instance.SelectSketchItem(SelOpt, Name, X, Y, Z)
```

### C#

```csharp
System.bool SelectSketchItem(
   System.int SelOpt,
   System.string Name,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
System.bool SelectSketchItem(
   System.int SelOpt,
   System.String^ Name,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelOpt`:
- `Name`:
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [ModelDoc::SelectSketchItem](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectSketchItem.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
