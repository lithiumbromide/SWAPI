---
title: "JogAngle Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "JogAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~JogAngle.html"
---

# JogAngle Property (IJogFeatureData)

Gets or sets the jog angle for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property JogAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Double

instance.JogAngle = value

value = instance.JogAngle
```

### C#

```csharp
System.double JogAngle {get; set;}
```

### C++/CLI

```cpp
property System.double JogAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Jog angle

## VBA Syntax

See [JogFeatureData::JogAngle](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~JogAngle.html).

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
