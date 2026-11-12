---
title: "InsertSheetMetalMiterFlange Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSheetMetalMiterFlange"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSheetMetalMiterFlange.html"
---

# InsertSheetMetalMiterFlange Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertSheetMetalMiterFlange](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalMiterFlange.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSheetMetalMiterFlange( _
   ByVal UseReliefRatio As System.Boolean, _
   ByVal UseDefaultGap As System.Boolean, _
   ByVal UseAutoRelief As System.Boolean, _
   ByVal GlobalRadius As System.Double, _
   ByVal RipGap As System.Double, _
   ByVal AutoReliefRatio As System.Double, _
   ByVal AutoReliefWidth As System.Double, _
   ByVal AutoReliefDepth As System.Double, _
   ByVal ReliefType As System.Integer, _
   ByVal RipLocation As System.Integer, _
   ByVal TrimSideBends As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim UseReliefRatio As System.Boolean
Dim UseDefaultGap As System.Boolean
Dim UseAutoRelief As System.Boolean
Dim GlobalRadius As System.Double
Dim RipGap As System.Double
Dim AutoReliefRatio As System.Double
Dim AutoReliefWidth As System.Double
Dim AutoReliefDepth As System.Double
Dim ReliefType As System.Integer
Dim RipLocation As System.Integer
Dim TrimSideBends As System.Boolean

instance.InsertSheetMetalMiterFlange(UseReliefRatio, UseDefaultGap, UseAutoRelief, GlobalRadius, RipGap, AutoReliefRatio, AutoReliefWidth, AutoReliefDepth, ReliefType, RipLocation, TrimSideBends)
```

### C#

```csharp
void InsertSheetMetalMiterFlange(
   System.bool UseReliefRatio,
   System.bool UseDefaultGap,
   System.bool UseAutoRelief,
   System.double GlobalRadius,
   System.double RipGap,
   System.double AutoReliefRatio,
   System.double AutoReliefWidth,
   System.double AutoReliefDepth,
   System.int ReliefType,
   System.int RipLocation,
   System.bool TrimSideBends
)
```

### C++/CLI

```cpp
void InsertSheetMetalMiterFlange(
   System.bool UseReliefRatio,
   System.bool UseDefaultGap,
   System.bool UseAutoRelief,
   System.double GlobalRadius,
   System.double RipGap,
   System.double AutoReliefRatio,
   System.double AutoReliefWidth,
   System.double AutoReliefDepth,
   System.int ReliefType,
   System.int RipLocation,
   System.bool TrimSideBends
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `UseReliefRatio`:
- `UseDefaultGap`:
- `UseAutoRelief`:
- `GlobalRadius`:
- `RipGap`:
- `AutoReliefRatio`:
- `AutoReliefWidth`:
- `AutoReliefDepth`:
- `ReliefType`:
- `RipLocation`:
- `TrimSideBends`:

## VBA Syntax

See [ModelDoc2::InsertSheetMetalMiterFlange](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSheetMetalMiterFlange.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
