---
title: "MakeStyledCurves2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "MakeStyledCurves2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MakeStyledCurves2.html"
---

# MakeStyledCurves2 Method (IFeatureManager)

Fits a spline to the preselected sketch segments to make a smooth edge on the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeStyledCurves2( _
   ByVal Tolerance As System.Double, _
   ByVal Mode As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Tolerance As System.Double
Dim Mode As System.Integer
Dim value As System.Boolean

value = instance.MakeStyledCurves2(Tolerance, Mode)
```

### C#

```csharp
System.bool MakeStyledCurves2(
   System.double Tolerance,
   System.int Mode
)
```

### C++/CLI

```cpp
System.bool MakeStyledCurves2(
   System.double Tolerance,
   System.int Mode
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Tolerance`: Deviation permitted from the selected geometry
- `Mode`: - 1 = Convert the selected geometry to construction geometry
  - 11 = delete the selected geometry

### Return Value

True if fit spline is created, false if not

## VBA Syntax

See [FeatureManager::MakeStyledCurves2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~MakeStyledCurves2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
