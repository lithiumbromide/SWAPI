---
title: "SelectByMark Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "SelectByMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~SelectByMark.html"
---

# SelectByMark Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::SelectByMark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~SelectByMark.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectByMark( _
   ByVal SelID As System.String, _
   ByVal SelParams As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Mark As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim SelID As System.String
Dim SelParams As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Mark As System.Integer
Dim value As System.Boolean

value = instance.SelectByMark(SelID, SelParams, X, Y, Z, Mark)
```

### C#

```csharp
System.bool SelectByMark(
   System.string SelID,
   System.string SelParams,
   System.double X,
   System.double Y,
   System.double Z,
   System.int Mark
)
```

### C++/CLI

```cpp
System.bool SelectByMark(
   System.String^ SelID,
   System.String^ SelParams,
   System.double X,
   System.double Y,
   System.double Z,
   System.int Mark
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelID`:
- `SelParams`:
- `X`:
- `Y`:
- `Z`:
- `Mark`:

## VBA Syntax

See [ModelDoc::SelectByMark](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~SelectByMark.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
