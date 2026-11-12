---
title: "CreateEllipseVB Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreateEllipseVB"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreateEllipseVB.html"
---

# CreateEllipseVB Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreateEllipse2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateEllipse2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateEllipseVB( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal MajorX As System.Double, _
   ByVal MajorY As System.Double, _
   ByVal MajorZ As System.Double, _
   ByVal MinorX As System.Double, _
   ByVal MinorY As System.Double, _
   ByVal MinorZ As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim CenterZ As System.Double
Dim MajorX As System.Double
Dim MajorY As System.Double
Dim MajorZ As System.Double
Dim MinorX As System.Double
Dim MinorY As System.Double
Dim MinorZ As System.Double
Dim value As System.Boolean

value = instance.CreateEllipseVB(CenterX, CenterY, CenterZ, MajorX, MajorY, MajorZ, MinorX, MinorY, MinorZ)
```

### C#

```csharp
System.bool CreateEllipseVB(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double MajorX,
   System.double MajorY,
   System.double MajorZ,
   System.double MinorX,
   System.double MinorY,
   System.double MinorZ
)
```

### C++/CLI

```cpp
System.bool CreateEllipseVB(
   System.double CenterX,
   System.double CenterY,
   System.double CenterZ,
   System.double MajorX,
   System.double MajorY,
   System.double MajorZ,
   System.double MinorX,
   System.double MinorY,
   System.double MinorZ
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CenterX`:
- `CenterY`:
- `CenterZ`:
- `MajorX`:
- `MajorY`:
- `MajorZ`:
- `MinorX`:
- `MinorY`:
- `MinorZ`:

## VBA Syntax

See [ModelDoc2::CreateEllipseVB](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreateEllipseVB.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
