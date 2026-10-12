---
title: "CustomSymbol::GetAnnotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/CustomSymbol/CustomSymbol__GetAnnotation.htm"
---

# CustomSymbol::GetAnnotation

This method is obsolete and has been superseded by [BlockInstance::GetAnnotation](../BlockInstance/BlockInstance__GetAnnotation.htm).

Description

This method gets the general annotation object for this custom symbol.

Syntax (OLE Automation)

retval = CustomSymbol.GetAnnotation ( )

| Return: | (LPDISPATCH) retval | Pointer to a Dispatch object, the general annotation object |
| --- | --- | --- |

Syntax (COM)

status = CustomSymbol->IGetAnnotation ( &retval )

| Output: | (LPANNOTATION) retval | Pointer to the general annotation object |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method gets the owning annotation object for this custom symbol. The annotation object is a higher-level object which contains methods that apply to all types of annotations (for example, Annotation::SetPosition).
