---
title: "AssemblyDoc::ComponentReload2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__ComponentReload2.htm"
---

# AssemblyDoc::ComponentReload2

This method is obsolete and has been superseded by [AssemblyDoc::ReplaceComponents](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__ReplaceComponents.htm).

Description

This method reloads the selected or supplied component.

Syntax (OLE Automation)

result = AssemblyDoc.ComponentReload2 ( component, readOnly, options )

| Input: | (LPDISPATCH) component | Dispatch pointer of component to reload |
| --- | --- | --- |
| Input: | (BOOL) readOnly | TRUE if the component is to be loaded read only |
| Input: | (long) options | Control options as defined in swComponentReloadOption_e |
| Return: | (long) result | Return code as defined in swComponentReloadError_e |

Syntax (COM)

status = AssemblyDoc->IComponentReload2 ( component, readOnly, options, &result )

| Input: | (LPCOMPONENT) component | Pointer to component to reload |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) readOnly | TRUE if the component is to be loaded read only |
| Input: | (long) options | Control options as defined in swComponentReloadOption_e |
| Output: | (long) result | Return code as defined in swComponentReloadError_e |
| Return: | (HRESULT) status | S_OK if Successful |

Remarks

If the component argument is set to NULL, then SolidWorks uses the last component in the current selections.
