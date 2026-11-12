---
title: "Component::Solving"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Component/Component__Solving.htm"
---

# Component::Solving

This property is obsolete and has been superseded by [Component2::Solving](sldworksAPI.chm::/Component2/Component2__Solving.htm).

Description

This property provides access to the solving option of this component.

Syntax (OLE Automation)

solving = Component.Solving (VB Get property)

solving = Component.GetSolving ( ) (C++ Get property)

| Property: | (long) solving | Solving option of this component instance as defined in swComponentSolvingOption_e |
| --- | --- | --- |

Syntax (COM)

status = Component->get_Solving( &solving )

| Property: | (long) solving | Solving option of this component instance as defined in swComponentSolvingOption_e |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

You can use AssemblyDoc::CompConfigProperties3 to set the solving state of a component.

This property applies only to subassembly components, not part components. If you try to get the solving option of a part component, SolidWorks returns -1.
