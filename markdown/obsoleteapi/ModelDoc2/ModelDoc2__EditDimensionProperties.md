---
title: "ModelDoc2::EditDimensionProperties"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditDimensionProperties.htm"
---

# ModelDoc2::EditDimensionProperties

This method is now obsolete and has been superseded by [ModelDoc2::EditDimensionProperties2](ModelDoc2__EditDimensionProperties2.htm).

Description

This method edits the currently selected dimension's properties.

Syntax (OLE Automation)

retval = ModelDoc2.EditDimensionProperties ( tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec, precision, arrowsIn, useDocArrows, arrow1, arrow2 )

| Input: | (long) tolType | Type of tolerance as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance |
| Input: | (BSTR) tolMaxFit | Text for the maximum FIT value when using a fit tolerance type |
| Input: | (BSTR) tolMinFit | Text for the maximum FIT value when using a fit tolerance type |
| Input: | (BOOL) useDocPrec | TRUE to use the documents precision value FALSE otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction as defined in swDimensionArrowsSide_e |
| Input: | (BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this dimension as defined in swArrowStyle_e |
| Return: | (BOOL) retval | TRUE if the dimension is modified, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->EditDimensionProperties ( tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec, precision, arrowsIn, useDocArrows, arrow1, arrow2, &retval )

| Input: | (long) tolType | Type of tolerance as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance |
| Input: | (BSTR) tolMaxFit | Text for the maximum FIT value when using a fit tolerance type |
| Input: | (BSTR) tolMinFit | Text string for the maximum FIT value when using a fit tolerance type |
| Input: | (VARIANT_BOOL) useDocPrec | TRUE to use the documents precision value, FALSE otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction as defined in swDimensionArrowsSide_e |
| Input: | (VARIANT_BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this dimension as defined in swArrowStyle_e |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
