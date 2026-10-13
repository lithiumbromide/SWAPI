---
title: "CosmeticThreads Property (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "CosmeticThreads"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~CosmeticThreads.html"
---

# CosmeticThreads Property (IMirrorPartFeatureData)

Gets or sets whether to import cosmetic threads.

## Syntax

### Visual Basic (Declaration)

```vb
Property CosmeticThreads As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Boolean

instance.CosmeticThreads = value

value = instance.CosmeticThreads
```

### C#

```csharp
System.bool CosmeticThreads {get; set;}
```

### C++/CLI

```cpp
property System.bool CosmeticThreads {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import cosmetic threads, false to not

## VBA Syntax

See [MirrorPartFeatureData::CosmeticThreads](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~CosmeticThreads.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
