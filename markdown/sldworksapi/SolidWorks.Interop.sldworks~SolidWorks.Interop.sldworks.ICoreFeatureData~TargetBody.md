---
title: "TargetBody Property (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "TargetBody"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~TargetBody.html"
---

# TargetBody Property (ICoreFeatureData)

Gets or sets the target body for this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TargetBody As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim value As Body2

instance.TargetBody = value

value = instance.TargetBody
```

### C#

```csharp
Body2 TargetBody {get; set;}
```

### C++/CLI

```cpp
property Body2^ TargetBody {
   Body2^ get();
   void set (    Body2^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) from which this core will be extracted

## VBA Syntax

See [CoreFeatureData::TargetBody](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~TargetBody.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
