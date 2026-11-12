---
title: "HoleWizard Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "HoleWizard"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard.html"
---

# HoleWizard Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::HoleWizard2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~HoleWizard2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function HoleWizard( _
   ByVal GenericHoleType As System.Integer, _
   ByVal StandardIndex As System.Integer, _
   ByVal FastenerTypeIndex As System.Integer, _
   ByVal SSize As System.String, _
   ByVal EndType As System.Short, _
   ByVal Diameter As System.Double, _
   ByVal Depth As System.Double, _
   ByVal Value1 As System.Double, _
   ByVal Value2 As System.Double, _
   ByVal Value3 As System.Double, _
   ByVal Value4 As System.Double, _
   ByVal Value5 As System.Double, _
   ByVal Value6 As System.Double, _
   ByVal Value7 As System.Double, _
   ByVal Value8 As System.Double, _
   ByVal Value9 As System.Double, _
   ByVal Value10 As System.Double, _
   ByVal Value11 As System.Double, _
   ByVal Value12 As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim GenericHoleType As System.Integer
Dim StandardIndex As System.Integer
Dim FastenerTypeIndex As System.Integer
Dim SSize As System.String
Dim EndType As System.Short
Dim Diameter As System.Double
Dim Depth As System.Double
Dim Value1 As System.Double
Dim Value2 As System.Double
Dim Value3 As System.Double
Dim Value4 As System.Double
Dim Value5 As System.Double
Dim Value6 As System.Double
Dim Value7 As System.Double
Dim Value8 As System.Double
Dim Value9 As System.Double
Dim Value10 As System.Double
Dim Value11 As System.Double
Dim Value12 As System.Double
Dim value As Feature

value = instance.HoleWizard(GenericHoleType, StandardIndex, FastenerTypeIndex, SSize, EndType, Diameter, Depth, Value1, Value2, Value3, Value4, Value5, Value6, Value7, Value8, Value9, Value10, Value11, Value12)
```

### C#

```csharp
Feature HoleWizard(
   System.int GenericHoleType,
   System.int StandardIndex,
   System.int FastenerTypeIndex,
   System.string SSize,
   System.short EndType,
   System.double Diameter,
   System.double Depth,
   System.double Value1,
   System.double Value2,
   System.double Value3,
   System.double Value4,
   System.double Value5,
   System.double Value6,
   System.double Value7,
   System.double Value8,
   System.double Value9,
   System.double Value10,
   System.double Value11,
   System.double Value12
)
```

### C++/CLI

```cpp
Feature^ HoleWizard(
   System.int GenericHoleType,
   System.int StandardIndex,
   System.int FastenerTypeIndex,
   System.String^ SSize,
   System.short EndType,
   System.double Diameter,
   System.double Depth,
   System.double Value1,
   System.double Value2,
   System.double Value3,
   System.double Value4,
   System.double Value5,
   System.double Value6,
   System.double Value7,
   System.double Value8,
   System.double Value9,
   System.double Value10,
   System.double Value11,
   System.double Value12
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `GenericHoleType`:
- `StandardIndex`:
- `FastenerTypeIndex`:
- `SSize`:
- `EndType`:
- `Diameter`:
- `Depth`:
- `Value1`:
- `Value2`:
- `Value3`:
- `Value4`:
- `Value5`:
- `Value6`:
- `Value7`:
- `Value8`:
- `Value9`:
- `Value10`:
- `Value11`:
- `Value12`:

## VBA Syntax

See [FeatureManager::HoleWizard](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~HoleWizard.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
