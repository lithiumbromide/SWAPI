---
title: "LBDownAt Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "LBDownAt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~LBDownAt.html"
---

# LBDownAt Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::LBDownAt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~LBDownAt.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub LBDownAt( _
   ByVal Flags As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Flags As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double

instance.LBDownAt(Flags, X, Y, Z)
```

### C#

```csharp
void LBDownAt(
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
void LBDownAt(
   System.int Flags,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flags`:
- `X`:
- `Y`:
- `Z`:

## VBA Syntax

See [ModelDoc::LBDownAt](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~LBDownAt.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
