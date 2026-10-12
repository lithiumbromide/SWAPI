---
title: "GetChildren Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetChildren"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html"
---

# GetChildren Method (IFeature)

Gets the child features belonging to this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetChildren() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Object

value = instance.GetChildren()
```

### C#

```csharp
System.object GetChildren()
```

### C++/CLI

```cpp
System.Object^ GetChildren();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of child [features](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [Feature::GetChildren](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetChildren.html).

## Examples

[Get Parent-Child Relationship for Component (VBA)](Get_Parent-Child_Relationship_for_Component_Example_VB.htm)

## Remarks

This method gets the direct children of this feature. It does not get children of children.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::IGetChildCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildCount.html)
[IFeature::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.html)
[IFeature::GetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html)
[IFeature::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.html)
[IFeature::IGetParentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParentCount.html)

## Availability

SOLIDWORKS 99, datecode 1999207
