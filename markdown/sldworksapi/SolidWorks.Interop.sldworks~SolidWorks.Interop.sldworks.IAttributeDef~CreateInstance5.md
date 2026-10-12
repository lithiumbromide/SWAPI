---
title: "CreateInstance5 Method (IAttributeDef)"
project: "SOLIDWORKS API Help"
interface: "IAttributeDef"
member: "CreateInstance5"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~CreateInstance5.html"
---

# CreateInstance5 Method (IAttributeDef)

Creates an instance of this attribute on the specified object with the specified options.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateInstance5( _
   ByVal OwnerDoc As ModelDoc2, _
   ByVal OwnerObj As System.Object, _
   ByVal NameIn As System.String, _
   ByVal Options As System.Integer, _
   ByVal ConfigurationOption As System.Integer _
) As Attribute
```

### Visual Basic (Usage)

```vb
Dim instance As IAttributeDef
Dim OwnerDoc As ModelDoc2
Dim OwnerObj As System.Object
Dim NameIn As System.String
Dim Options As System.Integer
Dim ConfigurationOption As System.Integer
Dim value As Attribute

value = instance.CreateInstance5(OwnerDoc, OwnerObj, NameIn, Options, ConfigurationOption)
```

### C#

```csharp
Attribute CreateInstance5(
   ModelDoc2 OwnerDoc,
   System.object OwnerObj,
   System.string NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

### C++/CLI

```cpp
Attribute^ CreateInstance5(
   ModelDoc2^ OwnerDoc,
   System.Object^ OwnerObj,
   System.String^ NameIn,
   System.int Options,
   System.int ConfigurationOption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OwnerDoc`: Document whose FeatureManager design tree to which to add this attribute
- `OwnerObj`: Component or entity to which to add this attribute:

  - [IBODY2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)
  - [ICOMPONENT2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)
  - [IENTITY](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEntity.html), which can be a face, loop, edge, vertex, or feature
  - [MODELDOC2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) if NULL
- `NameIn`: Name to assign to this attribute instance (see **Remarks**)
- `Options`: Creation control options (see **Remarks**)
- `ConfigurationOption`: Configuration options as defined in [swInConfigurationOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

### Return Value

Newly created [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) object

## VBA Syntax

See [AttributeDef::CreateInstance5](ms-its:sldworksapivb6.chm::/sldworks~AttributeDef~CreateInstance5.html).

## Examples

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)
[Delete Faces (VBA)](Delete_Faces_Example_VB.htm)
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)
[Delete Blended Faces (C#)](Delete_Blended_Faces_Example_CSharp.htm)
[Delete Blended Faces (VB.NET)](Delete_Blended_Faces_Example_VBNET.htm)
[Delete Blended Faces (VBA)](Delete_Blended_Faces_Example_VB.htm)

## Remarks

When you add an attribute to a feature, the FeatureManager design tree might not reflect the new state of the model. This discrepancy exists for performance reasons (rebuilding the FeatureManager design tree is very time-consuming). You can request a rebuild after you have added a number of attributes to save time.

The attribute is created as a feature and displayed in the FeatureManager design tree, which means that the name specified in nameIn must be unique in the FeatureManager design tree for the document.

You can create attributes on entity objects such as faces and edges, on features, or on the document itself. Do not use this method to set an attribute to or get an attribute from an assembly body. Instead, use [IFace2::SetFaceId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~SetFaceId.html) or [IFace2::GetFaceId](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetFaceId.html) to set or get the attribute.

Setting or clearing bits in the options argument controls the creation of the attribute:

| Bit | Value | Meaning |
| --- | --- | --- |
| 1 | 1 | Attribute is created hidden in the FeatureManager design tree (see IFeature::SetUIState ) |
| 1 | 0 | Attribute is created visible in the FeatureManager design tree |

For example, options = 1 creates an attribute that is hidden in the FeatureManager design tree.

NOTE: By default, SOLIDWORKS adds attributes only to the active configuration. SOLIDWORKS adds the attribute to all other configurations as a suppressed feature. You can unsuppress the attribute by selecting it with [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) and calling [IModelDoc2::EditUnsuppressDependent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~EditUnsuppressDependent2.html). If you want to add your attributes to a non-active configuration, then the user must edit the properties of that particular configuration and make sure that the Suppress New Features option is disabled.

If you add an attribute to an entity, SOLIDWORKS strips the attribute feature from the entity if the entity is included in your export to a library feature or library feature part. See the SOLIDWORKS Help for more information about library features.

NOTE: An attribute is a feature; thus, this method respects the [IConfiguration::SuppressNewFeatures](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~SuppressNewFeatures.html) setting.

## See Also

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.html)
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
