---
title: "ModelDoc::VersionHistory"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__VersionHistory.htm"
---

# ModelDoc::VersionHistory

This method is obsolete and has been superseded by [ModelDoc2::VersionHistory](sldworksAPI.chm::/ModelDoc2/ModelDoc2__VersionHistory.htm).

Description

This method returns a list of strings indicating the versions in which this document was saved.

Syntax (OLE Automation)

retval = ModelDoc.VersionHistory ( )

| Return: | (VARIANT) retval | VARIANT of type SafeArray containing an array of strings of the version history |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IVersionHistory ( retval )

| Output: | (BSTR*) retval | An array of strings containing the version history |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

There is one array entry for each major release of SolidWorks in which the document has been saved. The format for each entry is a major release code followed by one or more minor release codes separated by commas:

"<major release code>[<minor release code>]" or

"<major release code>[<minor release code>,<minor release code>...]"

where:

<major release code> = a number that remains constant through a major release of SolidWorks. For example, the following values would be returned based on the corresponding major SolidWorks version:

SolidWorks 95 = 44

SolidWorks 96 = 243

SolidWorks 97 = 483

SolidWorks 97Plus = 629

SolidWorks 98 = 822

SolidWorks 98Plus = 1008

SolidWorks 99 = 1137

SolidWorks 2000 = 1500

<minor release code> = the year and day of manufacture of a saving version (for example, 1997/320)

To get the size of array needed by IVersionHistory call ModelDoc::IGetVersionHistoryCount.

NOTE: If the document has not yet been saved, there is no version history information. In that case, this method (OLE Automation) returns VT_EMPTY, and the ModelDoc::IGetVersionHistoryCount API (COM) returns 0.

Last value returned in this array is the active SolidWorks version.
