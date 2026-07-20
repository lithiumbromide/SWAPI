---
title: "BendEdges Property (IConvertSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IConvertSolidFeatureData"
member: "BendEdges"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~BendEdges.html"
---

# BendEdges Property (IConvertSolidFeatureData)

Gets or sets the bend edges and faces in this convert solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property BendEdges As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IConvertSolidFeatureData
Dim value As System.Object

instance.BendEdges = value

value = instance.BendEdges
```

### C#

```csharp
System.object BendEdges {get; set;}
```

### C++/CLI

```cpp
property System.Object^ BendEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Property Value

Array of bend

[edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)

s

## VBA Syntax

See

[ConvertSolidFeatureData::BendEdges](ms-its:sldworksapivb6.chm::/sldworks~ConvertSolidFeatureData~BendEdges.html)

.

## Examples

See the

[IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

examples.

## See Also

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.html)

[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
