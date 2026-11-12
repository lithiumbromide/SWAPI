---
title: "DirectionVector Property (IRuledSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRuledSurfaceFeatureData"
member: "DirectionVector"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~DirectionVector.html"
---

# DirectionVector Property (IRuledSurfaceFeatureData)

Gets or sets the reference vector for this ruled-surface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DirectionVector As MathVector
```

### Visual Basic (Usage)

```vb
Dim instance As IRuledSurfaceFeatureData
Dim value As MathVector

instance.DirectionVector = value

value = instance.DirectionVector
```

### C#

```csharp
MathVector DirectionVector {get; set;}
```

### C++/CLI

```cpp
property MathVector^ DirectionVector {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Reference vector](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathVector.html)

## VBA Syntax

See [RuledSurfaceFeatureData::DirectionVector](ms-its:sldworksapivb6.chm::/sldworks~RuledSurfaceFeatureData~DirectionVector.html).

## Remarks

This property is only available when [IRuledSurfaceFeatureData::Type](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRuledSurfaceFeatureData~Type.html) is set to swRuledSurfaceType_Sweep.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.html)
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html)
[IRuledSurfaceFeatureData::UseVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~UseVector.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
