---
title: "CreateCenterLineVB Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateCenterLineVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateCenterLineVB.html"
---

# CreateCenterLineVB Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateCenterLineVB](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateCenterLineVB.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreateCenterLineVB( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double

instance.CreateCenterLineVB(X1, Y1, Z1, X2, Y2, Z2)
```

### C#

```csharp
void CreateCenterLineVB(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

### C++/CLI

```cpp
void CreateCenterLineVB(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `X1`:
- `Y1`:
- `Z1`:
- `X2`:
- `Y2`:
- `Z2`:

## VBA Syntax

See [ModelDoc::CreateCenterLineVB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateCenterLineVB.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
