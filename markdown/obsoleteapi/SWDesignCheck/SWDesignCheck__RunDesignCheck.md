---
title: "SWDesignCheck::RunDesignCheck"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SWDesignCheck/SWDesignCheck__RunDesignCheck.htm"
---

# SWDesignCheck::RunDesignCheck

This method is obsolete and has been superseded by [SWDesignCheck::RunDesignCheck2](sldworksAPI.chm::/SWDesignCheck/SWDesignCheck__RunDesignCheck2.htm).

Description

This method runs the SolidWorks Design Checker using the specified requirements document. This method can also add a new, or overwrite, an existing the report to the Design Binder.

Syntax (OLE Automation)

retval = SWDesignCheck->RunDesignCheck ( StandardFileName, ReportFolderName, AddtoDesignBinder, bOverWriteReport)

| Input: | (BSTR) StandardFileName | Path and filename of SolidWorks Design Checker requirements document |
| --- | --- | --- |
| Input: | (BSTR) ReportFolderName | Name of report NOTE: A filename extension of .dxp is automatically appended the specified filename. The report is an XML file. |
| Input: | (VARIANT_BOOLEAN) AddtoDesignBinder | TRUE to add the report to the Design Binder, FALSE to not |
| Input: | (VARIANT_BOOLEAN) bOverWriteReport | TRUE to overwrite any existing report of the same name in the Design Binder, FALSE to not |
| Return: | (long) retval | Error code as defined in dsgnchkError_e |

Syntax (COM)

status = SWDesignCheck->RunDesignCheck ( StandardFileName, ReportFolderName, AddtoDesignBinder, bOverWriteReport, &retval)

| Input: | (BSTR) StandardFileName | Path and filename of SolidWorks Design Checker requirements document |
| --- | --- | --- |
| Input: | (BSTR) ReportFolderName | Name of report NOTE: A filename extension of .dxp is automatically appended the specified filename. The output report is an XML file. |
| Input: | (VARIANT_BOOLEAN) AddtoDesignBinder | TRUE to add the report to the Design Binder, FALSE to not |
| Input: | (VARIANT_BOOLEAN) bOverWriteReport | TRUE to overwrite any existing report of the same name in the Design Binder, FALSE to not |
| Output: | (long) retval | Error code as defined in dsgnchkError_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
