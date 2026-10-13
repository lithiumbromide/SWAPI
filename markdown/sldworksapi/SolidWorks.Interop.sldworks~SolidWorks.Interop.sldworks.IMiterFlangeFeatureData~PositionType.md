---
title: "PositionType Property (IMiterFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMiterFlangeFeatureData"
member: "PositionType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~PositionType.html"
---

# PositionType Property (IMiterFlangeFeatureData)

Gets or sets the position for this miter flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property PositionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMiterFlangeFeatureData
Dim value As System.Integer

instance.PositionType = value

value = instance.PositionType
```

### C#

```csharp
System.int PositionType {get; set;}
```

### C++/CLI

```cpp
property System.int PositionType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of position for this mitre flange feature as defined by [swFlangePositionTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangePositionTypes_e.html)

## VBA Syntax

See [MiterFlangeFeatureData::PositionType](ms-its:sldworksapivb6.chm::/sldworks~MiterFlangeFeatureData~PositionType.html).

## See Also

[IMiterFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData.html)
[IMiterFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
