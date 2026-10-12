---
title: "UseVector Property (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "UseVector"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~UseVector.html"
---

# UseVector Property (IRuledSurfaceFeatureData)

Gets or sets whether or not use a reference vector for this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseVector As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim value As System.Boolean

instance.UseVector = value

value = instance.UseVector
```

### C#

```csharp
System.bool UseVector {get; set;}
```

### C++/CLI

```cpp
property System.bool UseVector {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use a reference vector, false to not

## VBA Syntax

See [RuledSurfaceFeatureData::UseVector](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~UseVector.html).

## Remarks

This property is only available when [IRuledSurfaceFeatureData::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRuledSurfaceFeatureData~Type.html) is set to swRuledSurfaceType_Sweep.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)
[IRuledSurfaceFeatureData::DirectionVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~DirectionVector.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
