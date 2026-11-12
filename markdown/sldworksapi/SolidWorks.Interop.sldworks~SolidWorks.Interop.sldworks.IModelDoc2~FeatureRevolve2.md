---
title: "FeatureRevolve2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureRevolve2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureRevolve2.html"
---

# FeatureRevolve2 Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::FeatureRevolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FeatureRevolve2( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Options As System.Integer
Dim value As System.Integer

value = instance.FeatureRevolve2(Angle, ReverseDir, Angle2, RevType, Options)
```

### C#

```csharp
System.int FeatureRevolve2(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options
)
```

### C++/CLI

```cpp
System.int FeatureRevolve2(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `ReverseDir`:
- `Angle2`:
- `RevType`:
- `Options`:

## VBA Syntax

See [ModelDoc2::FeatureRevolve2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureRevolve2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
