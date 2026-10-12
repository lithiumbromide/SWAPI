---
title: "CreateEllipse2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreateEllipse2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreateEllipse2.html"
---

# CreateEllipse2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreateEllipse2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreateEllipse2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateEllipse2( _
   ByVal CenterX As System.Double, _
   ByVal CenterY As System.Double, _
   ByVal CenterZ As System.Double, _
   ByVal MajorX As System.Double, _
   ByVal MajorY As System.Double, _
   ByVal MajorZ As System.Double, _
   ByVal MinorX As System.Double, _
   ByVal MinorY As System.Double, _
   ByVal MinorZ As System.Double _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim CenterX As System.Double
Dim CenterY As System.Double
Dim CenterZ As System.Double
Dim MajorX As System.Double
Dim MajorY As System.Double
Dim MajorZ As System.Double
Dim MinorX As System.Double
Dim MinorY As System.Double
Dim MinorZ As System.Double
Dim value As System.Object

value = instance.CreateEllipse2(CenterX, CenterY, CenterZ, MajorX, MajorY, MajorZ, MinorX, MinorY, MinorZ)
```

### C#

```csharp
System.object CreateEllipse2(
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
System.Object^ CreateEllipse2(
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

See [ModelDoc::CreateEllipse2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreateEllipse2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
