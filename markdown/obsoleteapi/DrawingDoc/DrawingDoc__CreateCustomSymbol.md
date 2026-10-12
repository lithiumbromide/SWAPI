---
title: "DrawingDoc::CreateCustomSymbol"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__CreateCustomSymbol.htm"
---

# DrawingDoc::CreateCustomSymbol

This method is obsolete and has been superseded by [DrawingDoc::CreateBlockDefinition](DrawingDoc__CreateBlockDefinition.htm).

Description

This method makes a custom symbol from the specified entities.

Syntax (OLE Automation)

retval = DrawingDoc.CreateCustomSymbol ( Segments, Points, Notes )

| Input: | (VARIANT) Segments | VARIANT of type SafeArray of Dispatch objects of the sketch segments to be part of this custom symbol |
| --- | --- | --- |
| Input: | (VARIANT) Points | VARIANT of type SafeArray of Dispatch objects of the sketch points to be part of this custom symbol |
| Input: | (VARIANT) Notes | VARIANT of type SafeArray of Dispatch objects of the notes to be part of this custom symbol |
| Output: | (LPDISPATCH) retval | Dispatch pointer to the new custom symbol |

Syntax (COM)

status = DrawingDoc->ICreateCustomSymbol ( SegmentCount, Segments, PointCount, Points, NoteCount, Notes, &retval )

| Input: | (long) SegmentCount | Number of segments in the Segments array |
| --- | --- | --- |
| Input: | (LPSKETCHSEGMENT*) Segments | Array of sketch segments to be part of this custom symbol |
| Input: | (long) PointCount | Number of points in the Point array |
| Input: | (LPSKETCHPOINT*) Points | Array of sketch points to be part of this custom symbol |
| Input: | (long) NoteCount | Number of notes in the Notes array |
| Input: | (LPNOTE*) Notes | Array of notes to be part of this custom symbol |
| Output: | (LPCUSTOMSYMBOL) retval | Interface to the custom symbol |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

This method is similar to [DrawingDoc::MakeCustomSymbol2](DrawingDoc__MakeCustomSymbol2.htm), except that instead of creating a custom symbol from the selected entities, this method creates a custom symbol from the specified entities. If you already have the pointers to the entities that need to be part of the custom symbol, directly running this method is much faster than selecting all of the entities and then running DrawingDoc::MakeCustomSymbol2.
