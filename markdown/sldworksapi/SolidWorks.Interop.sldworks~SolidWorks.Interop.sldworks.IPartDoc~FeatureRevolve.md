---
title: "FeatureRevolve Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "FeatureRevolve"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureRevolve.html"
---

# FeatureRevolve Method (IPartDoc)

Obsolete. Superseded by [IFeatureManager::FeatureRevolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureRevolve( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer

instance.FeatureRevolve(Angle, ReverseDir, Angle2, RevType)
```

### C#

```csharp
void FeatureRevolve(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
)
```

### C++/CLI

```cpp
void FeatureRevolve(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `ReverseDir`:
- `Angle2`:
- `RevType`:

## VBA Syntax

See [PartDoc::FeatureRevolve](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~FeatureRevolve.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
