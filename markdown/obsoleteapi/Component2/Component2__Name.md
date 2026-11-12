---
title: "Component2::Name"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component2/Component2__Name.htm"
---

# Component2::Name

This property is obsolete and has been superseded by [Component2::Name2](sldworksAPI.chm::/Component2/Component2__Name2.htm).

Description

This property gets the component name that appears in the FeatureManager design tree, and is not necessarily the same as the name of the underlying part or assembly file.

Syntax (OLE Automation)

Name = Component2.Name (VB Get property)

Name = Component2.GetName ( ) (C++ Get property)

| Property: | (BSTR) Name | Name of this component instance |
| --- | --- | --- |

Syntax (COM)

status = Component2->get_Name( &Name )

| Property: | (BSTR) Name | Name of this component instance |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This property returns a name that includes an instance number. For example:

Part1-1

indicates that this is the first instance of the Part1 Component2. If you are examining a component that is within a subassembly, then this property returns a name that includes the full hierarchical path of component names. For example:

subAssem1-2/Part1-1

indicates that this component (Part1) is the first instance within the subAssem1 Component2. It also shows that the second instance of subAssem1 is referenced.

Additionally, the User Option, External Reference setting allows or prohibits changes to this name. This setting affects only interactive user operations.

If you are setting the name of a component, remember that some special characters are reserved by SolidWorks.
