---
title: "EnumDocuments::Next"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/EnumDocuments/EnumDocuments__Next.htm"
---

# EnumDocuments::Next

This method is obsolete and has been superseded by [EnumDocuments2::Next](sldworksAPI.chm::/EnumDocuments2/EnumDocuments2__Next.htm).

Description

This method gets the next ModelDoc object.

Syntax (OLE Automation)

Not available.

Syntax (COM)

status = EnumDocuments->Next ( celt, rgelt, &pceltFetched )

| Input: | (long) celt | Number of documents desired for the enumerated list |
| --- | --- | --- |
| Output: | (LPMODELDOC*) rgelt | Pointer to an array of size celt to hold the documents |
| Output: | (long) pceltFetched | Pointer to the number of documents returned from the list; this value can be less than celt if you ask for more documents than exist, or it can be NULL if no more documents exist |
| Return: | (HRESULT)status | S_OK if successful |

Remarks
