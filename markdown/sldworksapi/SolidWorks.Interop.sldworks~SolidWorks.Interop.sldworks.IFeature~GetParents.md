---
title: "GetParents Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetParents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html"
---

# GetParents Method (IFeature)

Gets the parent features for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetParents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetParents()
```

### C#

```csharp
System.object GetParents()
```

### C++/CLI

```cpp
System.Object^ GetParents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array pointers to the parent [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [Feature::GetParents](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetParents.html).

## Examples

[Get Parent Feature Using Collections (VBA)](Find_Parent_Feature_using_Collections_Example_VB.htm)
[Get Parent-Child Relationship for Component (VBA)](Get_Parent-Child_Relationship_for_Component_Example_VB.htm)
[Get Plane Where Sketch Was Created (VBA)](Get_Plane_on_which_Sketch_Created_Example_VB.htm)

## Remarks

This method gets only the direct parents of this feature. It does not get parents of parents.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::GetOwnerFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetOwnerFeature.html)
[IFeature::IGetChildCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildCount.html)
[IFeature::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.html)
[IFeature::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.html)
[IFeature::IGetParentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParentCount.html)

## Availability

SOLIDWORKS 99, datecode 1999207
