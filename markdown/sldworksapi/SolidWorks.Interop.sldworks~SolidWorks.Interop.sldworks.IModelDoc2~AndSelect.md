---
title: "AndSelect Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "AndSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AndSelect.html"
---

# AndSelect Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::AndSelect](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~AndSelect.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
