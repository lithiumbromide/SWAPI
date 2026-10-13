---
title: "FeatureDimensionPattern Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "FeatureDimensionPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureDimensionPattern.html"
---

# FeatureDimensionPattern Method (IFeatureManager)

Not implemented.

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureDimensionPattern( _
   ByVal Num1 As System.Integer, _
   ByVal Spacing1 As System.Double, _
   ByVal Num2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal DiagonalOnly As System.Boolean, _
   ByVal DName1 As System.String, _
   ByVal DName2 As System.String, _
   ByVal VaryInstance As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Num1 As System.Integer
Dim Spacing1 As System.Double
Dim Num2 As System.Integer
Dim Spacing2 As System.Double
Dim DiagonalOnly As System.Boolean
Dim DName1 As System.String
Dim DName2 As System.String
Dim VaryInstance As System.Boolean
Dim value As Feature

value = instance.FeatureDimensionPattern(Num1, Spacing1, Num2, Spacing2, DiagonalOnly, DName1, DName2, VaryInstance)
```

### C#

```csharp
Feature FeatureDimensionPattern(
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool DiagonalOnly,
   System.string DName1,
   System.string DName2,
   System.bool VaryInstance
)
```

### C++/CLI

```cpp
Feature^ FeatureDimensionPattern(
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool DiagonalOnly,
   System.String^ DName1,
   System.String^ DName2,
   System.bool VaryInstance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Num1`:
- `Spacing1`:
- `Num2`:
- `Spacing2`:
- `DiagonalOnly`:
- `DName1`:
- `DName2`:
- `VaryInstance`:

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

Not implemented
