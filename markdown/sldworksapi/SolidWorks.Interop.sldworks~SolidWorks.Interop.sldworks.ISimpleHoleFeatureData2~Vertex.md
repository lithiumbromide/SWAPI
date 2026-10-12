---
title: "Vertex Property (ISimpleHoleFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleHoleFeatureData2"
member: "Vertex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Vertex.html"
---

# Vertex Property (ISimpleHoleFeatureData2)

Gets or sets the end-condition vertex of this simple hole feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Vertex As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleHoleFeatureData2
Dim value As System.Object

instance.Vertex = value

value = instance.Vertex
```

### C#

```csharp
System.object Vertex {get; set;}
```

### C++/CLI

```cpp
property System.Object^ Vertex {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End-condition [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html) or NULL if the operation fails

## VBA Syntax

See [SimpleHoleFeatureData2::Vertex](ms-its:sldworksapivb6.chm::/sldworks~SimpleHoleFeatureData2~Vertex.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.html)
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html)
[ISimpleHoleFeatureData2::IVertex Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IVertex.html)
[ISimpleHoleFeatureData2::IFace Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~IFace.html)
[ISimpleHoleFeatureData2::Face Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Face.html)
[ISimpleHoleFeatureData2::SetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SetEndConditionReference.html)
[ISimpleHoleFeatureData2::GetEndConditionReference Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~GetEndConditionReference.html)
[ISimpleHoleFeatureData2::Type Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Type.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
