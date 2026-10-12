---
title: "Component::ReferencedConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__ReferencedConfiguration.htm"
---

# Component::ReferencedConfiguration

This property is obsolete and has been superseded by [Component2::ReferencedConfiguration](sldworksAPI.chm::/Component2/Component2__ReferencedConfiguration.htm).

Description

This property gets or sets the active configuration used by this component.

Syntax (OLE Automation)

ConfigName = Component.ReferencedConfiguration (VB Get property)

Component.ReferencedConfiguration = ConfigName (VB Set property)

ConfigName = Component.GetReferencedConfiguration ( ) (C++ Get property)

Component.SetReferencedConfiguration ( ConfigName ) (C++ Set property)

| Property: | (BSTR) ConfigName | Name of the configuration for this component |
| --- | --- | --- |

Syntax (COM)

status = Component->get_ReferencedConfiguration( &ConfigName)

status = Component->put_ReferencedConfiguration ( ConfigName )

| Property: | (BSTR) ConfigName | Name of the configuration for this component |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

After changing the referenced configuration, call [AssemblyDoc::EditRebuild](../AssemblyDoc/AssemblyDoc__EditRebuild.htm) to display the changes.

When the configuration is changed, components might become suppressed or unsuppressed. This invalidates the array previously returned by Component::GetChildren. If an application calls this method while it is traversing an assembly, the applications must stop the traversal and start it again using the ModelDoc and active configuration of the assembly. The application should also free the array previously returned by Component::GetChildren before calling this method. To hold onto the component with the changed configuration, you can make an extra call to AddRef() for that component before freeing the array.
