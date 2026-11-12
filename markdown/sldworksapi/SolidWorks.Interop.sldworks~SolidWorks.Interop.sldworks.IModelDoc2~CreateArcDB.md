---
title: "CreateArcDB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateArcDB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateArcDB.html"
---

# CreateArcDB Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreateArc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateArc2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateArcDB( _
   ByVal X1 As System.Double, _
   ByVal Y1 As System.Double, _
   ByVal Z1 As System.Double, _
   ByVal X2 As System.Double, _
   ByVal Y2 As System.Double, _
   ByVal Z2 As System.Double, _
   ByVal X3 As System.Double, _
   ByVal Y3 As System.Double, _
   ByVal Z3 As System.Double, _
   ByVal Dir As System.Short _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim X1 As System.Double
Dim Y1 As System.Double
Dim Z1 As System.Double
Dim X2 As System.Double
Dim Y2 As System.Double
Dim Z2 As System.Double
Dim X3 As System.Double
Dim Y3 As System.Double
Dim Z3 As System.Double
Dim Dir As System.Short
Dim value As System.Boolean

value = instance.CreateArcDB(X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3, Dir)
```

### C#

```csharp
System.bool CreateArcDB(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3,
   System.short Dir
)
```

### C++/CLI

```cpp
System.bool CreateArcDB(
   System.double X1,
   System.double Y1,
   System.double Z1,
   System.double X2,
   System.double Y2,
   System.double Z2,
   System.double X3,
   System.double Y3,
   System.double Z3,
   System.short Dir
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
- `X3`:
- `Y3`:
- `Z3`:
- `Dir`:

## VBA Syntax

See [ModelDoc2::CreateArcDB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateArcDB.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
