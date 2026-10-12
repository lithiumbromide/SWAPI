---
title: "IAttribute Interface"
project: "SOLIDWORKS API Help"
interface: "IAttribute"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.html"
---

# IAttribute Interface

Allows access to an attribute's values.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IAttribute
```

### Visual Basic (Usage)

```vb
Dim instance As IAttribute
```

### C#

```csharp
public interface IAttribute
```

### C++/CLI

```cpp
public interface class IAttribute
```

## VBA Syntax

See [Attribute](ms-its:sldworksapivb6.chm::/sldworks~Attribute.html).

## Examples

[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)
[Delete Attribute (C#)](Delete_Attribute_Example_CSharp.htm)
[Delete Attribute (VB.NET)](Delete_Attribute_Example_VBNET.htm)
[Delete Attribute (VBA)](Delete_Attribute_Example_VB.htm)

## Remarks

An attribute is a piece of information that can be stored on a [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html), [entity](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html) ( [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html), [edge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html), [vertex](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IVertex.html), [loop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2.html), or [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)), and [model](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) if null.

After you place an attribute on an object, you can get the IAttribute object and get or set its parameter values. For example, you can place an attribute containing NC machining information on a face. You can then use that attribute in automation on the shop floor to know what feed or speed to use during the machining process.

You can also add attributes to a [document object](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html).

From the attribute instance you can get the:

- Attribute definition
- Associated entity
- Parameter values
- Instance name

## Accessors

[IAttributeDef::CreateInstance5 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttributeDef~CreateInstance5.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c2498' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c2498'

[IBody2::FindAttribute Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~FindAttribute.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c3681' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c3681'

[IComponent2::FindAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~FindAttribute.html) and [IComponent2::IFindAttribute Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~IFindAttribute.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c3685'

[IEntity::FindAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~FindAttribute.html) and [IEntity::IFindAttribute Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity~IFindAttribute.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c3683' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c3683'

[IFeature::GetSpecificFeature2 Method](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)designcommand:name=edit,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c303' designcommand:name=delete,id='SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute|c3685'

## Access Diagram

[Attribute](SWObjectModel.pdf#Attribute)

## See Also

[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
