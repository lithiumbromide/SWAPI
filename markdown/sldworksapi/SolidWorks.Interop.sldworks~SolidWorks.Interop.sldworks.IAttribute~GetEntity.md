---
title: "GetEntity Method (IAttribute)"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: "GetEntity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetEntity.html"
---

# GetEntity Method (IAttribute)

Gets the entity to which this attribute was originally associated.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEntity() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
Dim value As System.Object

value = instance.GetEntity()
```

### C#

```csharp
System.object GetEntity()
```

### C++/CLI

```cpp
System.Object^ GetEntity();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Object for the entity or NULL (see **Remarks**)

## VBA Syntax

See [Attribute::GetEntity](ms-its:sldworksapivb6.chm::/sldworks~Attribute~GetEntity.html).

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
[IAttribute::IGetEntity2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetEntity2.html)
[IAttribute::GetName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetName.html)
[IAttribute::GetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter.html)
[IAttributeDef::CreateInstance5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.html)
[IBody2::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~FindAttribute.html)
[IEntity::FindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~FindAttribute.html)
[IEntity::IFindAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~IFindAttribute.html)
[IFeature::GetSpecificFeature2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.html)
[ISldWorks::DefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.html)
