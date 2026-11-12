---
title: "SplitAll Property (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "SplitAll"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitAll.html"
---

# SplitAll Property (ISplitLineFeatureData)

Gets or sets whether to split all targets.

## Syntax

### Visual Basic (Declaration)

```vb
Property SplitAll As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As System.Boolean

instance.SplitAll = value

value = instance.SplitAll
```

### C#

```csharp
System.bool SplitAll {get; set;}
```

### C++/CLI

```cpp
property System.bool SplitAll {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to split all targets, false to not

## VBA Syntax

See [SplitLineFeatureData::SplitAll](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~SplitAll.html).

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)
[ISplitLineFeatureData::GetSplitTargetsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~GetSplitTargetsCount.html)
[ISplitLineFeatureData::IGetSplitTargets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~IGetSplitTargets.html)
[ISplitLineFeatureData::ISetSplitTargets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~ISetSplitTargets.html)
[ISplitLineFeatureData::SplitTargets Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~SplitTargets.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
