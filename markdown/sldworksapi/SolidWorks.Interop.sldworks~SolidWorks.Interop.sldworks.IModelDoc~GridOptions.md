---
title: "GridOptions Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "GridOptions"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~GridOptions.html"
---

# GridOptions Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::GridOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GridOptions.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GridOptions( _
   ByVal DispGrid As System.Boolean, _
   ByVal GridSpacing As System.Double, _
   ByVal Snap As System.Boolean, _
   ByVal DotStyle As System.Boolean, _
   ByVal NMajor As System.Short, _
   ByVal NMinor As System.Short, _
   ByVal Align2edge As System.Boolean, _
   ByVal AngleSnap As System.Boolean, _
   ByVal AngleUnit As System.Double, _
   ByVal MinorAuto As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim DispGrid As System.Boolean
Dim GridSpacing As System.Double
Dim Snap As System.Boolean
Dim DotStyle As System.Boolean
Dim NMajor As System.Short
Dim NMinor As System.Short
Dim Align2edge As System.Boolean
Dim AngleSnap As System.Boolean
Dim AngleUnit As System.Double
Dim MinorAuto As System.Boolean

instance.GridOptions(DispGrid, GridSpacing, Snap, DotStyle, NMajor, NMinor, Align2edge, AngleSnap, AngleUnit, MinorAuto)
```

### C#

```csharp
void GridOptions(
   System.bool DispGrid,
   System.double GridSpacing,
   System.bool Snap,
   System.bool DotStyle,
   System.short NMajor,
   System.short NMinor,
   System.bool Align2edge,
   System.bool AngleSnap,
   System.double AngleUnit,
   System.bool MinorAuto
)
```

### C++/CLI

```cpp
void GridOptions(
   System.bool DispGrid,
   System.double GridSpacing,
   System.bool Snap,
   System.bool DotStyle,
   System.short NMajor,
   System.short NMinor,
   System.bool Align2edge,
   System.bool AngleSnap,
   System.double AngleUnit,
   System.bool MinorAuto
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `DispGrid`:
- `GridSpacing`:
- `Snap`:
- `DotStyle`:
- `NMajor`:
- `NMinor`:
- `Align2edge`:
- `AngleSnap`:
- `AngleUnit`:
- `MinorAuto`:

## VBA Syntax

See [ModelDoc::GridOptions](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~GridOptions.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
