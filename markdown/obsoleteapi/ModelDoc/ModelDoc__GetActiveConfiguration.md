---
title: "ModelDoc::GetActiveConfiguration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetActiveConfiguration.htm"
---

# ModelDoc::GetActiveConfiguration

This method is obsolete and has been superseded by [ModelDoc2::GetActiveConfiguration](../ModelDoc2/ModelDoc2__GetActiveConfiguration.htm).

Description

This method returns the currently active Configuration object for this document. If this document is an assembly, then you can use this method to begin your traversal of the assembly components by making a subsequent call to Configuration::GetRootComponent.

Syntax (OLE Automation)

retval = ModelDoc.GetActiveConfiguration ()

| Return: | (LPDISPATCH) retval | Pointer to Dispatch object for the active Configuration object |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetActiveConfiguration ( &retval )

| Output: | (LPCONFIGURATION) retval | Pointer to the active Configuration object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

A component object is based on the currently active configuration; one assembly configuration may suppress the component, while another may display it. Therefore, your traversal of component objects may vary if you switch to a different configuration.

You should use this method of assembly traversal to replace previous calls to the Member class.

The order of calls needed in a typical assembly traversal are:

1. ModelDoc::GetActiveConfiguration (called only once)

2. Configuration::GetRootComponent (called only once)

3. Component::GetChildren (called recursively)

Your assembly traversal routine must begin from the root component and work its way down through the assembly structure. This is done by recursively calling Component::GetChildren. Calls to ModelDoc::GetActiveConfiguration and Configuration::GetRootComponent should only be done once for the entire assembly. In addition, your assembly traversal must begin with a ModelDoc object that has been activated and is visible, otherwise, the assembly structure may not be intact.

From the SolidWorks API, the Configuration and Component objects access to all the children components, the component transforms, and the component Body objects as seen in a specific assembly configuration. The Body objects and component transforms may vary based on the configuration; therefore, component traversal should be done for each of the configurations that exist. For example, one assembly configuration may have an assembly-level feature that cuts a hole through each of the components in the assembly. Using Component::GetBody on each of the assembly components will return the body of each component with the hole feature that was applied in this particular configuration. If you switch to the configuration without the assembly-level hole and re-traverse the component objects, then calling Component::GetBody for each component will return the Body object without the hole feature because it was applied in the other configuration.
