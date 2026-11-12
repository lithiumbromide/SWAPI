---
title: "AssemblyDoc::IComponentReload3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__IComponentReload3.htm"
---

# AssemblyDoc::IComponentReload3

This method is obsolete and has been superseded by [AssemblyDoc::ReplaceComponents](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__ReplaceComponents.htm).

Description

This method reloads the selected or supplied component.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = AssemblyDoc->IComponentReload3 ( component, readOnly, options, &result )

| Input: | (LPCOMPONENT) component | Pointer to component to reload |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) readOnly | TRUE if the component is to be loaded read-only |
| Input: | (long)options | Control options as defined in swComponentReloadOption_e |
| Output: | (long)result | Return code as defined in swComponentReloadError_e |
| Return: | (HRESULT)status | S_OK if Successful |

Remarks

If the component argument is set to NULL, then SolidWorks uses the last component in the current selections.
