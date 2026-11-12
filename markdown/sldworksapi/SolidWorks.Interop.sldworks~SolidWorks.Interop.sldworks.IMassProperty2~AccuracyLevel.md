---
title: "AccuracyLevel Property (IMassProperty2)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty2"
member: "AccuracyLevel"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~AccuracyLevel.html"
---

# AccuracyLevel Property (IMassProperty2)

Gets or sets the accuracy level used to calculate mass properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property AccuracyLevel As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty2
Dim value As System.Integer

instance.AccuracyLevel = value

value = instance.AccuracyLevel
```

### C#

```csharp
System.int AccuracyLevel {get; set;}
```

### C++/CLI

```cpp
property System.int AccuracyLevel {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Accuracy level as defined in [swMassPropertyAccuracyLevel_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMassPropertyAccuracyLevel_e.html)

## VBA Syntax

See [MassProperty2::AccuracyLevel](ms-its:sldworksapivb6.chm::/sldworks~MassProperty2~AccuracyLevel.html).

## See Also

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.html)
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
