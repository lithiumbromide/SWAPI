---
title: "Component::MaterialPropertyValues"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__MaterialPropertyValues.htm"
---

# Component::MaterialPropertyValues

This property is obsolete and has been superseded by [Component2::MaterialPropertyValues](sldworksAPI.chm::/Component2/Component2__MaterialPropertyValues.htm).

Description

This property gets or sets the material properties for a component.

Syntax (OLE Automation)

MaterialPropertyValues = Component.MaterialPropertyValues (VB Get property)

Component.MaterialPropertyValues = MaterialPropertyValues (VB Set property)

MaterialPropertyValues = Component.GetMaterialPropertyValues ( ) (C++ Get property)

Component.SetMaterialPropertyValues ( MaterialPropertyValues ) (C++ Set property)

| Property: | (VARIANT) MaterialPropertyValues | VARIANT of type SafeArray of doubles that describes the material values on this component (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Component->get_IMaterialPropertyValues( MaterialPropertyValues )

status = Component->put_IMaterialPropertyValues ( MaterialPropertyValues )

| Property: | (double*) MaterialPropertyValues | Array of doubles that describes the material values on this component (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The material values include the component color (R,G,B values), reflectivity (ambient, diffuse, specular, shininess), transparency, and emission. Valid values are from 0 to 1 for all values.

The format of the parameters or return values is an array of doubles as follows:

[ R, G, B, Ambient, Diffuse, Specular, Shininess, Transparency, Emission ]

This method returns a NULL VARIANT for OLE implementations and an S_FALSE HRESULT for COM implementations if this component has not been explicitly modified from the material property values of the underlying part document. For example, if the user performs a right-mouse click on a component in the FeatureManager design tree, then the user can select Component Properties and change the color. If the user does not do this, then the Component object returns NULL color information when calling Component::MaterialPropertyValues.

The default component color can be obtained from the component's ModelDoc object (Component::GetModelDoc) using ModelDoc::MaterialPropertyValues.

You can also use Face::MaterialPropertyValues to check for specific face colors.
