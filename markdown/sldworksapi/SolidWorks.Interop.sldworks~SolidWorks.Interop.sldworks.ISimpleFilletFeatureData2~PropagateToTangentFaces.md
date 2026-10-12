---
title: "PropagateToTangentFaces Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "PropagateToTangentFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~PropagateToTangentFaces.html"
---

# PropagateToTangentFaces Property (ISimpleFilletFeatureData2)

Gets or sets whether to extend fillet to all faces tangent to the selected face or edge.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateToTangentFaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim value As System.Boolean

instance.PropagateToTangentFaces = value

value = instance.PropagateToTangentFaces
```

### C#

```csharp
System.bool PropagateToTangentFaces {get; set;}
```

### C++/CLI

```cpp
property System.bool PropagateToTangentFaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if simple fillet feature should extend fillet to all faces tangent to the selected face or edge, false if not

## VBA Syntax

See [SimpleFilletFeatureData2::PropagateToTangentFaces](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~PropagateToTangentFaces.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
