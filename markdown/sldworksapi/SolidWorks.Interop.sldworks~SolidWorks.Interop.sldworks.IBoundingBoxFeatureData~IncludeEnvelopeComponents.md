---
title: "IncludeEnvelopeComponents Property (IBoundingBoxFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBoundingBoxFeatureData"
member: "IncludeEnvelopeComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData~IncludeEnvelopeComponents.html"
---

# IncludeEnvelopeComponents Property (IBoundingBoxFeatureData)

Gets or sets whether to include envelope components in this bounding box feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeEnvelopeComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBoundingBoxFeatureData
Dim value As System.Boolean

instance.IncludeEnvelopeComponents = value

value = instance.IncludeEnvelopeComponents
```

### C#

```csharp
System.bool IncludeEnvelopeComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeEnvelopeComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include envelope components, false to not

## VBA Syntax

See [BoundingBoxFeatureData::IncludeEnvelopeComponents](ms-its:sldworksapivb6.chm::/sldworks~BoundingBoxFeatureData~IncludeEnvelopeComponents.html).

## See Also

[IBoundingBoxFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData.html)
[IBoundingBoxFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
