---
title: "Thickness Property (IRibFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRibFeatureData"
member: "Thickness"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData~Thickness.html"
---

# Thickness Property (IRibFeatureData)

Obsolete. Superseded by [IRibFeatureData2::Thickness](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRibFeatureData2~Thickness.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Thickness As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRibFeatureData
Dim value As System.Double

instance.Thickness = value

value = instance.Thickness
```

### C#

```csharp
System.double Thickness {get; set;}
```

### C++/CLI

```cpp
property System.double Thickness {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [RibFeatureData::Thickness](ms-its:sldworksapivb6.chm::/sldworks~RibFeatureData~Thickness.html).

## See Also

[IRibFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData.html)
[IRibFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData_members.html)
