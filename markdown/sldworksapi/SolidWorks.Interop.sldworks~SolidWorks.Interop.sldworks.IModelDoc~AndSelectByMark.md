---
title: "AndSelectByMark Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AndSelectByMark"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AndSelectByMark.html"
---

# AndSelectByMark Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AndSelectByMark](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AndSelectByMark.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AndSelectByMark( _
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

value = instance.AndSelectByMark(SelID, SelParams, X, Y, Z, Mark)
```

### C#

```csharp
System.bool AndSelectByMark(
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
System.bool AndSelectByMark(
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

See [ModelDoc::AndSelectByMark](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AndSelectByMark.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
