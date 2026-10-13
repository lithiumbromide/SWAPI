---
title: "InsertSheetMetal3dBend Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetal3dBend"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetal3dBend.html"
---

# InsertSheetMetal3dBend Method (IFeatureManager)

Inserts a 3D bend in sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetal3dBend( _
   ByVal Angle As System.Double, _
   ByVal BUseDefaultRadius As System.Boolean, _
   ByVal Radius As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal BendPos As System.Short, _
   ByVal PCBA As CustomBendAllowance _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Angle As System.Double
Dim BUseDefaultRadius As System.Boolean
Dim Radius As System.Double
Dim FlipDir As System.Boolean
Dim BendPos As System.Short
Dim PCBA As CustomBendAllowance
Dim value As Feature

value = instance.InsertSheetMetal3dBend(Angle, BUseDefaultRadius, Radius, FlipDir, BendPos, PCBA)
```

### C#

```csharp
Feature InsertSheetMetal3dBend(
   System.double Angle,
   System.bool BUseDefaultRadius,
   System.double Radius,
   System.bool FlipDir,
   System.short BendPos,
   CustomBendAllowance PCBA
)
```

### C++/CLI

```cpp
Feature^ InsertSheetMetal3dBend(
   System.double Angle,
   System.bool BUseDefaultRadius,
   System.double Radius,
   System.bool FlipDir,
   System.short BendPos,
   CustomBendAllowance^ PCBA
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Angle of the bend in radians
- `BUseDefaultRadius`: True to use the default radius, false to use the value specified in radius
- `Radius`: Value for the radius of the bend if bUseDefaultRadius is false
- `FlipDir`: True to flip the bend direction, false to not
- `BendPos`: Bend position:

  - 0 = bend centerline
  - 1 = material inside
  - 2 = material outside
  - 3 = bend outside
- `PCBA`:

  | If... | Then... |
  | --- | --- |
  | non-NULL | Pointer to ICustomBendAllowance object for which required values have been set |
  | NULL | Parent bend's bend allowance is used |

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertSheetMetal3dBend](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetal3dBend.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)
[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
