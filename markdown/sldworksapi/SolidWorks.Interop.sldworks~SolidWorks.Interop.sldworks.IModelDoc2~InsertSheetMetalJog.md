---
title: "InsertSheetMetalJog Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSheetMetalJog"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalJog.html"
---

# InsertSheetMetalJog Method (IModelDoc2)

Inserts a sheet metal jog in the current model document.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSheetMetalJog( _
   ByVal Angle As System.Double, _
   ByVal Radius As System.Double, _
   ByVal OffsetDist As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal FixProjLen As System.Boolean, _
   ByVal DimPos As System.Short, _
   ByVal BendPos As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Angle As System.Double
Dim Radius As System.Double
Dim OffsetDist As System.Double
Dim FlipDir As System.Boolean
Dim FixProjLen As System.Boolean
Dim DimPos As System.Short
Dim BendPos As System.Short

instance.InsertSheetMetalJog(Angle, Radius, OffsetDist, FlipDir, FixProjLen, DimPos, BendPos)
```

### C#

```csharp
void InsertSheetMetalJog(
   System.double Angle,
   System.double Radius,
   System.double OffsetDist,
   System.bool FlipDir,
   System.bool FixProjLen,
   System.short DimPos,
   System.short BendPos
)
```

### C++/CLI

```cpp
void InsertSheetMetalJog(
   System.double Angle,
   System.double Radius,
   System.double OffsetDist,
   System.bool FlipDir,
   System.bool FixProjLen,
   System.short DimPos,
   System.short BendPos
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Jog angle
- `Radius`: Jog radius
- `OffsetDist`: Offset distance
- `FlipDir`: True flips the jog direction, false does not
- `FixProjLen`: True fixes the projected length, false does not
- `DimPos`: Dimension position
- `BendPos`: Bend position

## VBA Syntax

See [ModelDoc2::InsertSheetMetalJog](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSheetMetalJog.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
