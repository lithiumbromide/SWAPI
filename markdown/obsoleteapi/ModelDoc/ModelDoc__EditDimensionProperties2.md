---
title: "ModelDoc::EditDimensionProperties2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__EditDimensionProperties2.htm"
---

# ModelDoc::EditDimensionProperties2

This method is obsolete and has been superseded by [ModelDoc2::EditDimensionProperties2](../ModelDoc2/ModelDoc2__EditDimensionProperties2.htm).

Description

This method edits the currently selected dimension's properties.

Syntax (OLE Automation)

retval = ModelDoc.EditDimensionProperties2 ( tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec, precision, arrowsIn, useDocArrows, arrow1, arrow2, prefixText, suffixText, showValue, calloutText1, calloutText2, centerText )

| Input: | (long) tolType | Type of tolerance you want to use as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance. |
| Input: | (BSTR) tolMaxFit | Text string for the maximum FIT value when using a fit tolerance type |
| Input: | (BSTR) tolMinFit | Text string for the maximum FIT value when using a fit tolerance type |
| Input: | (BOOL) useDocPrec | TRUE to use the documents precision value, FALSE otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction as defined in swDimensionArrowsSide_e |
| Input: | (BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this dimension as defined in swArrowStyle_e |
| Input: | (BSTR) prefixText | String you want to display as the prefix of this dimension |
| Input: | (BSTR) suffixText | String that you want to display as the suffix of this dimension |
| Input: | (BOOL) showValue | TRUE if you want to display the value of this dimension in the user interface, FALSE otherwise |
| Input: | (BSTR) calloutText1 | Callout text above the dimension |
| Input: | (BSTR) calloutText2 | Callout text below the dimension |
| Input: | (BOOL) centerText | TRUE if you want to center the text in this dimension, FALSE otherwise |
| Return: | (BOOL) retval | TRUE if the dimension was successfully edited, FALSE otherwise |

Syntax (COM)

status = ModelDoc->EditDimensionProperties2 ( tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec, precision, arrowsIn, useDocArrows, arrow1, arrow2, prefixText, suffixText, showValue, calloutText1, calloutText2, centerText, &retval )

| Input: | (long) tolType | Type of tolerance you'd like to use. See swTolType_e. |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance. |
| Input: | (double) tolMin | Minimum value for the tolerance. |
| Input: | (BSTR) tolMaxFit | Text string for the maximum FIT value when using a fit tolerance type |
| Input: | (BSTR) tolMinFit | Text string for the maximum FIT value when using a fit tolerance type |
| Input: | (VARIANT_BOOL) useDocPrec | TRUE to use the documents precision value, FALSE otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction. See swDimensionArrowsSide_e |
| Input: | (VARIANT_BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this dimension as defined in swArrowStyle_e |
| Input: | (BSTR) prefixText | String you want to display as the prefix of this dimension |
| Input: | (BSTR) suffixText | String that you want to display as the suffix of this dimension |
| Input: | (VARIANT_BOOL) showValue | TRUE if you want to display the value of this dimension in the user interface, FALSE otherwise |
| Input: | (BSTR) calloutText1 | Callout text above the dimension |
| Input: | (BSTR) calloutText2 | Callout text below the dimension |
| Input: | (VARIANT_BOOL) centerText | TRUE if you want to center the text in this dimension, FALSE otherwise |
| Output: | (VARIANT_BOOL) retval | TRUE if the dimension was successfully edited, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
