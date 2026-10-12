---
title: "Component::GetModelDoc"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetModelDoc.htm"
---

# Component::GetModelDoc

This method is obsolete and has been superseded by [Component2::GetModelDoc](sldworksAPI.chm::/Component2/Component2__IGetModelDoc.htm).

Description

This method gets the ModelDoc object for this component.

Syntax (OLE Automation)

retval = Component.GetModelDoc ()

| Return: | (LPDISPATCH) retval | Pointer to Dispatch object, the model for this component |
| --- | --- | --- |

Syntax (COM)

status = Component->IGetModelDoc ( &retval )

| Output: | (LPMODELDOC) retval | Pointer to the model for this component |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If a component is suppressed or lightweight, this method might return NULL because the component has not been loaded into memory by SolidWorks. For more information on lightweight components, see Working With Lightweight Components.

When you use the ModelDoc object of a component, you do not have access to whatever uniqueness might exist for this instance of the assembly component. This happens because the ModelDoc object goes back to the local version of the part file. By comparison, the Component object gathers its information at the assembly level. This allows Component objects to recognize any assembly-level changes made to a component instance (for example, assembly-level features and material changes).

In addition, the ModelDoc returned from this method is representative of the last saved state. If the component part is open, then the ModelDoc represents the state of the opened document. For example, if the component part is not open and it was last saved in the default configuration, then Component::GetModelDoc returns a ModelDoc pointer representing that state. To get access to other configuration information, such as features and configuration properties, use [ShowConfiguration](../ModelDoc/ModelDoc__ShowConfiguration2.htm) to activate the part and display that configuration.

If this component is the root component, then this method returns a NULL pointer. For more information, see Configuration::GetRootComponent.
