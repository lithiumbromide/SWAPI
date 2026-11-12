---
title: "PartDoc::Body"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/PartDoc/PartDoc__Body.htm"
---

# PartDoc::Body

The OLE version of this method is obsolete and has been superseded by [PartDoc::GetBodies2](sldworksAPI.chm::/PartDoc/PartDoc__GetBodies2.htm) and [PartDoc::EnumBodies3](sldworksAPI.chm::/PartDoc/PartDoc__EnumBodies3.htm).

The COM version of this method is also obsolete and has been superseded by [PartDoc::IBodyObject2](PartDoc__IBodyObject2.htm).

Description

This method returns a pointer or Dispatch pointer to the Body object for this part. You can object surfaces and edges by referencing this object.

Syntax (OLE Automation)

retval = PartDoc.Body ()

| Return: | (LPDISPATCH) retval | Dispatch pointer to Dispatch object, the geometry of the part |
| --- | --- | --- |

Syntax (COM)

status = PartDoc->IBodyObject ( &retval )

| Output: | (LPBODY) retval | Pointer to the geometry of the part |
| --- | --- | --- |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

When working with assemblies, you may want to obtain the Body object using Component::GetBody. Obtaining the Body object from the actual Component object recognizes any assembly-level changes made to this body.

For example, if an assembly-level hole is drilled through an assembly component, then the Body object returned from Component::GetBody contains that hole; whereas, the Body object returned from PartDoc::Body does not contain the hole. This is because this type of assembly-level change is kept with the assembly component and is not propagated to the underlying part document.

If the PartDoc contains more than one body, this method returns NULL or Nothing in Visual Basic. See Partdoc::EnumBodies3 and PartDoc::GetBodies2.
