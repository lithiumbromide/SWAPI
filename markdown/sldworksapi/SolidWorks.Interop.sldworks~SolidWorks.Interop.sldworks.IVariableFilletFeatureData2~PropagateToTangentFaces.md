---
title: "PropagateToTangentFaces Property (IVariableFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IVariableFilletFeatureData2"
member: "PropagateToTangentFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~PropagateToTangentFaces.html"
---

# PropagateToTangentFaces Property (IVariableFilletFeatureData2)

Gets or sets whether to extend the fillet to all faces tangent to the selected face or edge.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropagateToTangentFaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IVariableFilletFeatureData2
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

True to extend fillet to all faces tangent to the selected face or edge, false to not

## VBA Syntax

See [VariableFilletFeatureData2::PropagateToTangentFaces](ms-its:sldworksapivb6.chm::/sldworks~VariableFilletFeatureData2~PropagateToTangentFaces.html).

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.html)
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
