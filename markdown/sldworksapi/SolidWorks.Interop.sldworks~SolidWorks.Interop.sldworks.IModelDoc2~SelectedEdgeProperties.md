---
title: "SelectedEdgeProperties Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SelectedEdgeProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedEdgeProperties.html"
---

# SelectedEdgeProperties Method (IModelDoc2)

Sets the property values of the selected edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectedEdgeProperties( _
   ByVal EdgeName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim EdgeName As System.String
Dim value As System.Boolean

value = instance.SelectedEdgeProperties(EdgeName)
```

### C#

```csharp
System.bool SelectedEdgeProperties(
   System.string EdgeName
)
```

### C++/CLI

```cpp
System.bool SelectedEdgeProperties(
   System.String^ EdgeName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `EdgeName`: Name of the edge

### Return Value

True if edge properties successfully changed, false if not

## VBA Syntax

See [ModelDoc2::SelectedEdgeProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SelectedEdgeProperties.html).

## Remarks

| If the edge... | Then this method... |
| --- | --- |
| Does not have a name | Sets the name. |
| Has a name | Does not change the name and returns false. This behavior is intended to prevent a program from renaming an edge that is referenced in some other location. For example, if an assembly contains a mate to an edge on a part, then a name is automatically assigned to that edge. If you change that name, then there is no guarantee that the mate remains valid. Therefore, when using entity names, you should first check to see if the entity is already named, and if so, use the existing name. If no name exists for the edge, then you can give the edge a name. |

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SelectedFaceProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFaceProperties.html)
[IModelDoc2::SelectedFeatureProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SelectedFeatureProperties.html)
[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[IModelDoc2::EntityProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EntityProperties.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
