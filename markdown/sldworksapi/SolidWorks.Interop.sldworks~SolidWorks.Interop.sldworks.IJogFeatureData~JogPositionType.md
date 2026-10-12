---
title: "JogPositionType Property (IJogFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IJogFeatureData"
member: "JogPositionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~JogPositionType.html"
---

# JogPositionType Property (IJogFeatureData)

Gets or sets the jog position type for this jog feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property JogPositionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IJogFeatureData
Dim value As System.Integer

instance.JogPositionType = value

value = instance.JogPositionType
```

### C#

```csharp
System.int JogPositionType {get; set;}
```

### C++/CLI

```cpp
property System.int JogPositionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Position type as defined in [swJogPositionType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swJogPositionType_e.html)

## VBA Syntax

See [JogFeatureData::JogPositionType](ms-its:sldworksapivb6.chm::/sldworks~JogFeatureData~JogPositionType.html).

## See Also

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.html)
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
