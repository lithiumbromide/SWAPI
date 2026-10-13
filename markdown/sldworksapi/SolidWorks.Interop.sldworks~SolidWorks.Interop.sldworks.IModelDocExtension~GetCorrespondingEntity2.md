---
title: "GetCorrespondingEntity2 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCorrespondingEntity2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorrespondingEntity2.html"
---

# GetCorrespondingEntity2 Method (IModelDocExtension)

Gets the entity in the underlying part or subassembly that corresponds to the specified entity in this assembly or drawing view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCorrespondingEntity2( _
   ByVal Entity As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Entity As System.Object
Dim value As System.Object

value = instance.GetCorrespondingEntity2(Entity)
```

### C#

```csharp
System.object GetCorrespondingEntity2(
   System.object Entity
)
```

### C++/CLI

```cpp
System.Object^ GetCorrespondingEntity2(
   System.Object^ Entity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Entity`: Dispatch pointer to a [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html), or [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) entity in this drawing view or assembly

### Return Value

Corresponding [entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.html) in the underlying part or subassembly; null or Nothing if none found (see **Remarks**)

## VBA Syntax

See [ModelDocExtension::GetCorrespondingEntity2](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetCorrespondingEntity2.html).

## Examples

[Get Corresponding Entities Between Parts and Drawing Views (VBA)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VB.htm)
[Get Corresponding Entities Between Parts and Drawing Views (VB.NET)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_VBNET.htm)
[Get Corresponding Entities Between Parts and Drawing Views (C#)](Get_Corresponding_Entities_Between_Parts_and_Views_Example_CSharp.htm)

## Remarks

To get the assembly entity corresponding to a given component entity, use [IComponent2::GetCorrespondingEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetCorrespondingEntity.html).

To get the drawing view entity corresponding to a given part or assembly entity, use [IView::GetCorrespondingEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCorrespondingEntity.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetCorresponding2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCorresponding2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
