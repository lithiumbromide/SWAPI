---
title: "MiterGap Property (IHemFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHemFeatureData"
member: "MiterGap"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~MiterGap.html"
---

# MiterGap Property (IHemFeatureData)

Gets or sets the miter gap for this hem feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MiterGap As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IHemFeatureData
Dim value As System.Double

instance.MiterGap = value

value = instance.MiterGap
```

### C#

```csharp
System.double MiterGap {get; set;}
```

### C++/CLI

```cpp
property System.double MiterGap {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Miter gap

## VBA Syntax

See [HemFeatureData::MiterGap](ms-its:sldworksapivb6.chm::/sldworks~HemFeatureData~MiterGap.html).

## See Also

[IHemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData.html)
[IHemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
