---
title: "AndSelect Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AndSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AndSelect.html"
---

# AndSelect Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AndSelect](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AndSelect.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub AndSelect( _
   ByVal SelID As System.String, _
   ByVal SelParams As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim SelID As System.String
Dim SelParams As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.AndSelect(SelID, SelParams, X, Y, Z)
```

### C#

```csharp
void AndSelect(
   System.string SelID,
   System.string SelParams,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void AndSelect(
   System.String^ SelID,
   System.String^ SelParams,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SelID`:
- `SelParams`:
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [ModelDoc::AndSelect](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AndSelect.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
