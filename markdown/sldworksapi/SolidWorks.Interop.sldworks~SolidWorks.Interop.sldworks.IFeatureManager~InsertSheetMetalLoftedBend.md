---
title: "InsertSheetMetalLoftedBend Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertSheetMetalLoftedBend"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalLoftedBend.html"
---

# InsertSheetMetalLoftedBend Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertSheetMetalLoftedBend2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSheetMetalLoftedBend2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSheetMetalLoftedBend( _
   ByVal ThickDirType As System.Integer, _
   ByVal Thickness As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim ThickDirType As System.Integer
Dim Thickness As System.Double
Dim value As Feature

value = instance.InsertSheetMetalLoftedBend(ThickDirType, Thickness)
```

### C#

```csharp
Feature InsertSheetMetalLoftedBend(
   System.int ThickDirType,
   System.double Thickness
)
```

### C++/CLI

```cpp
Feature^ InsertSheetMetalLoftedBend(
   System.int ThickDirType,
   System.double Thickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ThickDirType`: Toggles the thickening direction:

  - 0 = outside
  - 1 = inside (default value)
- `Thickness`: Thickness of the bend

### Return Value

Pointer to the lofted-bend [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) in the sheet metal part

## VBA Syntax

See [FeatureManager::InsertSheetMetalLoftedBend](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertSheetMetalLoftedBend.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
