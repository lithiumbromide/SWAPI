---
title: "PlyRelativeAngle Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "PlyRelativeAngle"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~PlyRelativeAngle.html"
---

# PlyRelativeAngle Property (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::PlyRelativeAngle2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~PlyRelativeAngle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property PlyRelativeAngle As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Integer

instance.PlyRelativeAngle = value

value = instance.PlyRelativeAngle
```

### C#

```csharp
System.int PlyRelativeAngle {get; set;}
```

### C++/CLI

```cpp
property System.int PlyRelativeAngle {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 if ply angles are relative to the angle of ply 1, 0 if not

## VBA Syntax

See [CWCompositeShellOptions::PlyRelativeAngle](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~PlyRelativeAngle.html).

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::GetPlyParameters Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetPlyParameters.html)
[ICWCompositeShellOptions::SetPlyParameters Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlyParameters.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
