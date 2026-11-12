---
title: "FeatureRevolveThin Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "FeatureRevolveThin"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~FeatureRevolveThin.html"
---

# FeatureRevolveThin Method (IPartDoc)

Obsolete. Superseded by [IFeatureManager::FeatureRevolveThin](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~FeatureRevolveThin.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub FeatureRevolveThin( _
   ByVal Angle As System.Double, _
   ByVal ReverseDir As System.Boolean, _
   ByVal Angle2 As System.Double, _
   ByVal RevType As System.Integer, _
   ByVal Thickness1 As System.Double, _
   ByVal Thickness2 As System.Double, _
   ByVal ReverseThinDir As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Angle As System.Double
Dim ReverseDir As System.Boolean
Dim Angle2 As System.Double
Dim RevType As System.Integer
Dim Thickness1 As System.Double
Dim Thickness2 As System.Double
Dim ReverseThinDir As System.Integer

instance.FeatureRevolveThin(Angle, ReverseDir, Angle2, RevType, Thickness1, Thickness2, ReverseThinDir)
```

### C#

```csharp
void FeatureRevolveThin(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir
)
```

### C++/CLI

```cpp
void FeatureRevolveThin(
   System.double Angle,
   System.bool ReverseDir,
   System.double Angle2,
   System.int RevType,
   System.double Thickness1,
   System.double Thickness2,
   System.int ReverseThinDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Angle`:
- `ReverseDir`:
- `Angle2`:
- `RevType`:
- `Thickness1`:
- `Thickness2`:
- `ReverseThinDir`:

## VBA Syntax

See [PartDoc::FeatureRevolveThin](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~FeatureRevolveThin.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
