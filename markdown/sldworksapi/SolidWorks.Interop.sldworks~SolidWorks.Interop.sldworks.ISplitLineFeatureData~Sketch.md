---
title: "Sketch Property (ISplitLineFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISplitLineFeatureData"
member: "Sketch"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData~Sketch.html"
---

# Sketch Property (ISplitLineFeatureData)

Gets the seed sketch for this split line feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Sketch As Sketch
```

### Visual Basic (Usage)

```vb
Dim instance As ISplitLineFeatureData
Dim value As Sketch

instance.Sketch = value

value = instance.Sketch
```

### C#

```csharp
Sketch Sketch {get; set;}
```

### C++/CLI

```cpp
property Sketch^ Sketch {
   Sketch^ get();
   void set (    Sketch^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Sketch](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html)

## VBA Syntax

See [SplitLineFeatureData::Sketch](ms-its:sldworksapivb6.chm::/sldworks~SplitLineFeatureData~Sketch.html).

## See Also

[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[ISplitLineFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
