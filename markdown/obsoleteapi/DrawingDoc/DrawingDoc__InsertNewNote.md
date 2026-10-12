---
title: "DrawingDoc::InsertNewNote"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertNewNote.htm"
---

# DrawingDoc::InsertNewNote

This method is obsolete and has been superseded by [DrawingDoc::InsertNewNote2](sldworksAPI.chm::/DrawingDoc/DrawingDoc__InsertNewNote2.htm).

Description

This method creates a new note in this drawing.

Syntax (OLE Automation)

void DrawingDoc.InsertNewNote ( text, noLeader, balloonNote, bentLeader, arrowStyle, leaderSide)

| Input: | (BSTR) text | Text string to be put in the note |
| --- | --- | --- |
| Input: | (BOOL) noLeader | TRUE does not add a leader line, FALSE does |
| Input: | (BOOL) balloonNote | TRUE adds balloon, FALSE does not |
| Input: | (BOOL) bentLeader | TRUE adds a bent leader line, FALSE does not |
| Input: | (short) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (short) leaderSide | Leader line side as defined in swLeaderSide_e |

Syntax (COM)

status = DrawingDoc->InsertNewNote ( text, noLeader, balloonNote, bentLeader, arrowStyle, leaderSide )

| Input: | (BSTR) text | Text string to be put in the note |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) noLeader | TRUE does not add a leader line, FALSE does |
| Input: | (VARIANT_BOOL) balloonNote | TRUE adds a balloon, FALSE does not |
| Input: | (VARIANT_BOOL) bentLeader | TRUE adds a bent leader line, FALSE does not |
| Input: | (short) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (short) leaderSide | Leader line side as defined in swLeaderSide_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
