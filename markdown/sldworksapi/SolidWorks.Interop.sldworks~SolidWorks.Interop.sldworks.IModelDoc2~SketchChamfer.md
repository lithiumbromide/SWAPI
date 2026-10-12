---
title: "SketchChamfer Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchChamfer"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchChamfer.html"
---

# SketchChamfer Method (IModelDoc2)

Obsolete. Superseded by [ISketchManager::CreateChamfer](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchManager~CreateChamfer.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchChamfer( _
   ByVal AngleORdist As System.Double, _
   ByVal Dist1 As System.Double, _
   ByVal Options As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim AngleORdist As System.Double
Dim Dist1 As System.Double
Dim Options As System.Integer

instance.SketchChamfer(AngleORdist, Dist1, Options)
```

### C#

```csharp
void SketchChamfer(
   System.double AngleORdist,
   System.double Dist1,
   System.int Options
)
```

### C++/CLI

```cpp
void SketchChamfer(
   System.double AngleORdist,
   System.double Dist1,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AngleORdist`: Angle of the chamfer if using the Angle-Distance option or the distance of the second distance if using the Distance-Distance option
- `Dist1`: Distance of the chamfer
- `Options`: 0 = Angle - Distance Chamfer

  1 = Distance - Distance Chamfer

## VBA Syntax

See [ModelDoc2::SketchChamfer](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchChamfer.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
