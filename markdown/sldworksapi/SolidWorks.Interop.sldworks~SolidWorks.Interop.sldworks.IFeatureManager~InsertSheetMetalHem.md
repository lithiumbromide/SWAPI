---
title: "InsertSheetMetalHem Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetalHem"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem.html"
---

# InsertSheetMetalHem Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertSheetMetalHem2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalHem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalHem( _
   ByVal Type As System.Integer, _
   ByVal Position As System.Integer, _
   ByVal Reverse As System.Boolean, _
   ByVal DLength As System.Double, _
   ByVal DGap As System.Double, _
   ByVal DAngle As System.Double, _
   ByVal DRad As System.Double, _
   ByVal DMiterGap As System.Double, _
   ByVal PCBA As CustomBendAllowance _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Type As System.Integer
Dim Position As System.Integer
Dim Reverse As System.Boolean
Dim DLength As System.Double
Dim DGap As System.Double
Dim DAngle As System.Double
Dim DRad As System.Double
Dim DMiterGap As System.Double
Dim PCBA As CustomBendAllowance
Dim value As Feature

value = instance.InsertSheetMetalHem(Type, Position, Reverse, DLength, DGap, DAngle, DRad, DMiterGap, PCBA)
```

### C#

```csharp
Feature InsertSheetMetalHem(
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap,
   CustomBendAllowance PCBA
)
```

### C++/CLI

```cpp
Feature^ InsertSheetMetalHem(
   System.int Type,
   System.int Position,
   System.bool Reverse,
   System.double DLength,
   System.double DGap,
   System.double DAngle,
   System.double DRad,
   System.double DMiterGap,
   CustomBendAllowance^ PCBA
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Type`: Type as defined in [swHemTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHemTypes_e.html)
- `Position`: Position as defined in [swHemPositionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHemPositionTypes_e.html)
- `Reverse`: True reverses the direction, false does not
- `DLength`: Hem length; valid only for open or closed hems
- `DGap`: Gap distance; valid only for open hems
- `DAngle`: Hem angle; valid only for tear-drop or rolled hems
- `DRad`: Hem radius; valid only for tear-drop or rolled hems
- `DMiterGap`: Hem miter gap
- `PCBA`:

  | If... | Then... |
  | --- | --- |
  | non-NULL | Pointer to ICustomBendAllowance object for which required values have been set |
  | NULL | Parent bend's bend allowance is used |

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertSheetMetalHem](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetalHem.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
