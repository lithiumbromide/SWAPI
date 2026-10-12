---
title: "ModelDoc::InsertNote"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertNote.htm"
---

# ModelDoc::InsertNote

This method is obsolete and has been superseded by [ModelDoc2::InsertNote](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertNote.htm).

Description

This method creates a new note in this document.

Syntax (OLE Automation)

retval = ModelDoc.InsertNote ( text )

| Input: | ( BSTR ) text | T ext string or symbol to be put in the note |
| --- | --- | --- |
| Return: | (LPDISPATCH) retval | Dispatch pointer to the new Note object |

Syntax (COM)

status = ModelDoc->IInsertNote ( text, &retval )

| Input: | (BSTR) text | T ext string or symbol to be put in the note |
| --- | --- | --- |
| Output: | (LPNOTE) retval | Pointer to the new Note object |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

The leader attachment points for the note that is created come from the selections made before calling this method. The initial location of the note will also be near the selection location. If there are no selections, the note will not have a leader, be free standing, and initially be at the origin of the model or drawing.

This method creates a default note. To adjust the display characteristics of this note, you should use the pointer that is returned by this method to access the various properties and get and set methods of the Note interface, such as Note::SetBalloon and Note::Angle. Use the Note::GetAnnotation method to retrieve the Annotation object, which has other useful methods, such as Annotation::SetLeader2 and Annotation::SetPosition.
