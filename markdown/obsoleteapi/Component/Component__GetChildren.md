---
title: "Component::GetChildren"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__GetChildren.htm"
---

# Component::GetChildren

This method is obsolete and has been superseded by [Component2::GetChildren](sldworksAPI.chm::/Component2/Component2__GetChildren.htm).

Description

This method gets all the children components of this component object.

Syntax (OLE Automation)

retval = Component.GetChildren ()

| Return: | (VARIANT) retval | VARIANT of type SafeArray of an array of pointers to Dispatch objects |
| --- | --- | --- |

Syntax (COM)

status = Component->IGetChildren ( &retval )

| Output: | (LPCOMPONENT*) retval | Pointer to an array of Component objects |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

If this assembly component is a part document, SolidWorks returns NULL. If this assembly component is the root component or a subassembly, then this method returns the child components that belong to the assembly document.

The typical order of calls needed in assembly traversal is:

1. ModelDoc::GetActiveConfiguration (called only once)

2. Configuration::GetRootComponent (called only once)

3. Component::GetChildren (called recursively)

Your assembly traversal routine must begin from the root component and work its way down through the assembly structure. This is done by recursively calling Component::GetChildren, as demonstrated in the examples above. Call Component::GetActiveConfiguration and Component::GetRootComponent once for the entire assembly. In addition, your assembly traversal must begin with a ModelDoc object that is activated and visible, otherwise the assembly structure might not be in tact.

COM applications should use to Component::IGetChildrenCount to determine the number of component children, which is the size of the array required to Component::IGetChildren.

You must call the GetChildren method recursively because it returns only the immediate (one level) children. It does not get child components of the sub-assemblies. For example, if one of the child components of a component is a sub-assembly that has its own children, those children are not returned by this method. You need to call this method again from that sub-assembly component to get its children.

For a given component, this method returns all of the immediate child components. This includes suppressed, hidden and lightweight components. Use Component::Visible and Component::GetSuppression to detect the component states.

Results of an assembly traversal vary based on the configuration currently displayed in your main assembly and based on the configuration referenced by the subassembly component. The list of child components that this function returns can be different depending on which configuration is referenced by the component (refer to ModelDoc::GetActiveConfiguration and Component::ReferencedConfiguration).

For example, if one configuration of your main assembly contains a suppressed subassembly, GetChildren returns an empty array when you call it from that suppressed subassembly component. As another example, a subassembly document (.sldasm file) can contain several configurations, each of which has varying states of suppression for its child components. When inserted into your main assembly, this subassembly document can reference any of these configurations. As a result, you might find that the child component suppression states vary based on which configuration is referenced by the subassembly component (refer to Component::ReferencedConfiguration).

Be aware that from call to call, this method might not return components in the same order.
