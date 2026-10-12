---
title: "InsertCrossBreak Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertCrossBreak"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCrossBreak.html"
---

# InsertCrossBreak Method (IFeatureManager)

Inserts a cross break feature on the selected face in a sheet metal part.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertCrossBreak( _
   ByVal Angle As System.Double, _
   ByVal Radius As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Angle As System.Double
Dim Radius As System.Double
Dim value As Feature

value = instance.InsertCrossBreak(Angle, Radius)
```

### C#

```csharp
Feature InsertCrossBreak(
   System.double Angle,
   System.double Radius
)
```

### C++/CLI

```cpp
Feature^ InsertCrossBreak(
   System.double Angle,
   System.double Radius
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`: Break angle
- `Radius`: Break radius

### Return Value

Cross break [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertCrossBreak](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertCrossBreak.html).

## Examples

[Get Cross Break Feature Data in Sheet Metal Part (C#)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_CSharp.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VB.NET)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VBNET.htm)
[Get Cross Break Feature Data in Sheet Metal Part (VBA)](Get_Cross_Break_Feature_Data_in_Sheet_Metal_Part_Example_VB.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[ICrossBreakFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
