---
title: "Callout::UpdatePosition"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Callout/Callout__UpdatePosition.htm"
---

# Callout::UpdatePosition

This method is obsolete and has been superseded by [Callout::Position](sldworksAPI.chm::/Callout/Callout__Position.htm).

Description

This method updates the position of this callout.

Syntax (OLE Automation)

void = Callout.UpdatePosition ( xPos, yPos, zPos)

| Input: | (double) xPos | x coordinate for callout |
| --- | --- | --- |
| Input: | (double) yPos | y coordinate for callout |
| Input: | (double) zPos | z coordinate for callout |

Syntax (COM)

status = Callout->UpdatePosition ( xPos, yPos, zPos)

| Input: | (double) xPos | x coordinate for callout |
| --- | --- | --- |
| Input: | (double) yPos | y coordinate for callout |
| Input: | (double) zPos | z coordinate for callout |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
