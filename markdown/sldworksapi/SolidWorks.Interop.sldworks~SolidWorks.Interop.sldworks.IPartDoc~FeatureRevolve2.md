---
title: "FeatureRevolve2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "FeatureRevolve2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureRevolve2.html"
---

# FeatureRevolve2 Method (IPartDoc)

Obsolete. Superseded by [IFeatureManager::FeatureRevolve](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolve.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureRevolve2( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Merge As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Merge As System.Boolean

instance.FeatureRevolve2(Angle, ReverseDir, Angle2, RevType, Merge)
```

### C#

```csharp
void FeatureRevolve2(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.bool Merge
)
```

### C++/CLI

```cpp
void FeatureRevolve2(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.bool Merge
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `ReverseDir`:
- `Angle2`:
- `RevType`:
- `Merge`:

## VBA Syntax

See [PartDoc::FeatureRevolve2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~FeatureRevolve2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
