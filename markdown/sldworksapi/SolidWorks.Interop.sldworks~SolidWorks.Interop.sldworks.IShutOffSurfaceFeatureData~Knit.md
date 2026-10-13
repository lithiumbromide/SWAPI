---
title: "Knit Property (IShutOffSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IShutOffSurfaceFeatureData"
member: "Knit"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~Knit.html"
---

# Knit Property (IShutOffSurfaceFeatureData)

Gets or sets whether to knit the patches in this shut-off surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Knit As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IShutOffSurfaceFeatureData
Dim value As System.Boolean

instance.Knit = value

value = instance.Knit
```

### C#

```csharp
System.bool Knit {get; set;}
```

### C++/CLI

```cpp
property System.bool Knit {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to knit the patches, false to not

## VBA Syntax

See [ShutOffSurfaceFeatureData::Knit](ms-its:sldworksapivb6.chm::/sldworks~ShutOffSurfaceFeatureData~Knit.html).

## Examples

See [IShutOffSurfaceFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IShutOffSurfaceFeatureData.html) examples.

## See Also

[IShutOffSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData.html)
[IShutOffSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html)
[IShutOffSurfaceFeatureData::SetAllPatchTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~SetAllPatchTypes.html)
[IShutOffSurfaceFeatureData::LoopPatchType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData~LoopPatchType.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
