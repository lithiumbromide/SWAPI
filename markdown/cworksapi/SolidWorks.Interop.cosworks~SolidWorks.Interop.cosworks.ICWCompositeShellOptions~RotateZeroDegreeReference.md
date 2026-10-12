---
title: "RotateZeroDegreeReference Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "RotateZeroDegreeReference"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~RotateZeroDegreeReference.html"
---

# RotateZeroDegreeReference Property (ICWCompositeShellOptions)

Obsolete. Superseded by [ICWCompositeShellOptions::RotateZeroDegreeReference2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~RotateZeroDegreeReference2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property RotateZeroDegreeReference As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Integer

instance.RotateZeroDegreeReference = value

value = instance.RotateZeroDegreeReference
```

### C#

```csharp
System.int RotateZeroDegreeReference {get; set;}
```

### C++/CLI

```cpp
property System.int RotateZeroDegreeReference {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to rotate the 0° ply angle reference, 0 to not

## VBA Syntax

See [CWCompositeShellOptions::RotateZeroDegreeReference](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~RotateZeroDegreeReference.html).

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::GetRotateOrientation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetRotateOrientation.html)
[ICWCompositeShellOptions::SetRotateOrientation Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetRotateOrientation.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
