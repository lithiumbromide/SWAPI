---
title: "ModelDoc::InsertNewNote3"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__InsertNewNote3.htm"
---

# ModelDoc::InsertNewNote3

This method is obsolete and has been superseded by [ModelDoc2::InsertNewNote3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__InsertNewNote3.htm).

Description

This method creates a new note.

Syntax (OLE Automation)

void ModelDoc.InsertNewNote3 ( upperText, noLeader, bentLeader, arrowStyle, leaderSide, angle, balloonStyle, balloonFit, smartArrow )

| Input: | (BSTR) upperText | Upper-text string to be put in the note |
| --- | --- | --- |
| Input: | (BOOL) noLeader | TRUE for no leader line, FALSE otherwise |
| Input: | (BOOL) bentLeader | TRUE for a bent leader line, FALSE otherwise |
| Input: | (short) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (short) leaderSide | Leader-line side as defined in swLeaderSide_e |
| Input: | (double) angle | Text angle |
| Input: | (short) balloonStyle | Balloon style type as defied in swBalloonStyle_e |
| Input: | (short) balloonFit | Balloon fit type as defined in swBalloonFit_e |
| Input: | (BOOL) smartArrow | If TRUE, then the arrow style specified in Options, Detailing is used for the arrows, if FALSE then the arrowStyle argument is used |

Syntax (COM)

status = ModelDoc->InsertNewNote3 ( upperText, noLeader, bentLeader, arrowStyle, leaderSide, angle, balloonStyle, balloonFit, smartArrow )

| Input: | (BSTR) upperText | Uppe- text string to be put in the note |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) noLeader | TRUE for no leade rline, FALSE otherwise |
| Input: | (VARIANT_BOOL) bentLeader | TRUE for a bent leader line, FALSE otherwise |
| Input: | (short) arrowStyle | Arrowhead type as defined in swArrowStyle_e |
| Input: | (short) leaderSide | Leade-line side as defined in swLeaderSide_e |
| Input: | (double) angle | Text angle |
| Input: | (short) balloonStyle | Balloon style type as defined in swBalloonStyle_e |
| Input: | (short) balloonFit | Balloon fit type as defined in swBalloonFit_e |
| Input: | (VARIANT_BOOL) smartArrow | If TRUE, then the arrow style specified in Options, Detailing is used for the arrows, if FALSE then the arrowStyle argument is used |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
