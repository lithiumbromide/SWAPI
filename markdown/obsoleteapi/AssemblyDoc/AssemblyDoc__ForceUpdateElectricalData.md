---
title: "AssemblyDoc::ForceUpdateElectricalData"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/AssemblyDoc/AssemblyDoc__ForceUpdateElectricalData.htm"
---

# AssemblyDoc::ForceUpdateElectricalData

This method is obsolete and has been superseded by [AssemblyDoc::ForeUpdateElectricalData2](sldworksAPI.chm::/AssemblyDoc/AssemblyDoc__ForceUpdateElectricalData2.htm).

Description

This method forces an update of electrical data.

Syntax (OLE Automation)

void = AssemblyDoc.ForceUpdateElectricalData ( stream)

| Input: | (long) stream | 0 = All streams 2 = From-To list stream 3 = Segment data stream 4 = Wire list stream |
| --- | --- | --- |

Syntax (COM

status = AssemblyDoc->ForceUpdateElectricalData ( stream)

| Input: | (long) stream | 0 = All streams 2 = From-To list stream 3 = Segment data stream 4 = Wire list stream |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Third-party applications call this method to tell the SolidWorks software that they have changed the electrical data. The SolidWorks software then re-reads the data to get the updates.
