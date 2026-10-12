---
title: "Body2::Check2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Body2/Body2__Check2.htm"
---

# Body2::Check2

This method is obsolete and has been superseded by [Body2::Check3](sldworksAPI.chm::/Body2/Body2__Check3.htm).

Description

This method checks whether or not the body is a valid solid.

Syntax (OLE Automation)

retval = Body2.Check2 ()

| Output: | (long) retval | 1 if the body is a valid solid, 0 if not (see Remarks ) |
| --- | --- | --- |

Syntax (COM)

status = Body2->Check2 ( &retval)

| Output: | (long) retval | 1 if the body is a valid solid, 0 if not (see Remarks ) |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The return value indicates the number of faults found in the body.
