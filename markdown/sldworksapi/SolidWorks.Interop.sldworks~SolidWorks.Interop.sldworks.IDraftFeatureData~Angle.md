---
title: "Angle Property (IDraftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IDraftFeatureData"
member: "Angle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData~Angle.html"
---

# Angle Property (IDraftFeatureData)

Obsolete. Superseded by [IDraftFeatureData2::Angle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDraftFeatureData2~Angle.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Angle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDraftFeatureData
Dim value As System.Double

instance.Angle = value

value = instance.Angle
```

### C#

```csharp
System.double Angle {get; set;}
```

### C++/CLI

```cpp
property System.double Angle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DraftFeatureData::Angle](ms-its:sldworksapivb6.chm::/sldworks~DraftFeatureData~Angle.html).

## See Also

[IDraftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData.html)
[IDraftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData_members.html)
