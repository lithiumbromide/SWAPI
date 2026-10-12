---
title: "Dimension::SetUserValueIn"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Dimension/Dimension__SetUserValueIn.htm"
---

# Dimension::SetUserValueIn

This method is obsolete and has been superseded by [Dimension.SetUserValueIn2](sldworksAPI.chm::/Dimension/Dimension_SetUserValueIn2.htm).

Description

This method sets the value of this dimension in the units of the specified document.

Syntax (OLE Automation)

void Dimension.SetUserValueIn ( doc, newValue)

| Input: | (LPDISPATCH) doc | Dispatch pointer to the document whose units you want to use |
| --- | --- | --- |
| Input: | (double) newValue | Dimension value in the units of the specified document, doc |

Syntax (COM)

status = Dimension->ISetUserValueIn ( doc, newValue )

| Input: | (LPMODELDOC) doc | Pointer to the document whose units you want to use |
| --- | --- | --- |
| Input: | (double) newValue | Dimension value in the units of the specified document, doc |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method allows you to change the value of a read-only dimension. Use Dimension::ReadOnly to determine if a dimension is read-only.
