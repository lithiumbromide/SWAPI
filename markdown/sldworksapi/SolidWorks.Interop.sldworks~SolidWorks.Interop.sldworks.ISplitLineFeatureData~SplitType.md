---
title: "SplitType Property (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "SplitType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitType.html"
---

# SplitType Property (ISplitLineFeatureData)

Gets or sets the type of split.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplitType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Integer

instance.SplitType = value

value = instance.SplitType
```

### C#

```csharp
System.int SplitType {get; set;}
```

### C++/CLI

```cpp
property System.int SplitType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of split as defined in [swSplitLineFeatureType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSplitLineFeatureType_e.html)

## VBA Syntax

See [SplitLineFeatureData::SplitType](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~SplitType.html).

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::GetType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetType.html)
