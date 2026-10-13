---
title: "IGetEntity2 Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "IGetEntity2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetEntity2.html"
---

# IGetEntity2 Method (IAttribute)

Gets the entity to which this attribute was originally associated.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetEntity2() As Entity
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim value As Entity

value = instance.IGetEntity2()
```

### C#

```csharp
Entity IGetEntity2()
```

### C++/CLI

```cpp
Entity^ IGetEntity2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IEntity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) or NULL (see **Remarks**)

## VBA Syntax

See [Attribute::IGetEntity2](ms-its:sldworksapivb6.chm::/sldworks~Attribute~IGetEntity2.html).

## Remarks

This method returns NULL when the attribute is associated with:

- the document
- an invalid entity
- a suppressed entity

When this method returns NULL, use [IAttribute::GetEntityState](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute~GetEntityState.html) to determine which of these situations you have encountered.

When the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) object is suppressed, this method returns NULL.

## See Also

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html)
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[IAttribute::GetEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity.html)
[IAttribute::GetEntityState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntityState.html)
[IBody2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute.html)
[IComponent2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~FindAttribute.html)
[IEntity::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute.html)
[IEntity::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute.html)
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html)
[ISldWorks::DefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.html)
