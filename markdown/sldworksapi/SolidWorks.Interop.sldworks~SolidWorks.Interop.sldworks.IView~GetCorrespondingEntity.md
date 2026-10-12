---
title: "GetCorrespondingEntity Method (IView)"
project: "SOLIDWORKS API Help"
interface: "IView"
member: "GetCorrespondingEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorrespondingEntity.html"
---

# GetCorrespondingEntity Method (IView)

Gets the entity in this drawing view that corresponds to the specified part or assembly entity.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorrespondingEntity( _
   ByVal Entity As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IView
Dim Entity As System.Object
Dim value As System.Object

value = instance.GetCorrespondingEntity(Entity)
```

### C#

```csharp
System.object GetCorrespondingEntity(
   System.object Entity
)
```

### C++/CLI

```cpp
System.Object^ GetCorrespondingEntity(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: Dispatch pointer to a [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) entity in the part or assembly

### Return Value

Corresponding [entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html) in this drawing view; null or Nothing if none found

## VBA Syntax

See [View::GetCorrespondingEntity](ms-its:sldworksapivb6.chm::/sldworks~View~GetCorrespondingEntity.html).

## Examples

[Get Corresponding Entities Between Parts and Drawing Views (VBA)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VB.htm)
[Get Corresponding Entities Between Parts and Drawing Views (VB.NET)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VBNET.htm)
[Get Corresponding Entities Between Parts and Drawing Views (C#)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_CSharp.htm)

## Remarks

Use [IModelDocExtension::GetCorrespondingEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity2.html) to get the part entity that corresponds to a drawing view entity.

## See Also

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.html)
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html)
[IView::GetCorresponding Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorresponding.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
