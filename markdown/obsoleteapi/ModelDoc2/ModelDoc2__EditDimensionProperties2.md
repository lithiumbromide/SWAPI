---
title: "ModelDoc2::EditDimensionProperties2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc2/ModelDoc2__EditDimensionProperties2.htm"
---

# ModelDoc2::EditDimensionProperties2

This method is obsolete and has been superseded by [ModelDoc2::EditDimensionProperties3](sldworksAPI.chm::/ModelDoc2/ModelDoc2__EditDimensionProperties3.htm).

Description

This method will allow you to edit the currently selected dimension's properties.

Syntax (OLE Automation)

retval = ModelDoc2.EditDimensionProperties2 ( tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec, precision, arrowsIn, useDocArrows, arrow1, arrow2, prefixText, suffixText, showValue, calloutText1, calloutText2, centerText )

| Input: | (long) tolType | Type of tolerance as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance |
| Input: | (BSTR) tolMaxFit | Text for the maximum FIT value when using a fit tolerance type |
| Input: | (BSTR) tolMinFit | Text for the maximum FIT value when using a fit tolerance type |
| Input: | (BOOL) useDocPrec | TRUE to use the documents precision value, FALSE otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction as defined in swDimensionArrowsSide_e. |
| Input: | (BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this dimension as defined as swArrowStyle_e |
| Input: | (BSTR) prefixText | Text for the prefix of this dimension |
| Input: | (BSTR) suffixText | Text for the suffix of this dimension |
| Input: | (BOOL) showValue | TRUE if you want to display the value of this dimension in the user interface, FALSE otherwise. |
| Input: | (BSTR) calloutText1 | Callout text above the dimension |
| Input: | (BSTR) calloutText2 | Callout text below the dimension |
| Input: | (BOOL) centerText | TRUE if you want to center the text in this dimension, FALSE otherwise |
| Return: | (BOOL) retval | TRUE if the dimension is modified, FALSE otherwise |

Syntax (COM)

status = ModelDoc2->EditDimensionProperties2 ( tolType, tolMax, tolMin, tolMaxFit, tolMinFit, useDocPrec, precision, arrowsIn, useDocArrows, arrow1, arrow2, prefixText, suffixText, showValue, calloutText1, calloutText2, centerText, &retval )

| Input: | (long) tolType | Type of tolerance as defined in swTolType_e |
| --- | --- | --- |
| Input: | (double) tolMax | Maximum value for the tolerance |
| Input: | (double) tolMin | Minimum value for the tolerance |
| Input: | (BSTR) tolMaxFit | Text for the maximum FIT value when using a fit tolerance type |
| Input: | (BSTR) tolMinFit | Text for the maximum FIT value when using a fit tolerance type |
| Input: | (VARIANT_BOOL) useDocPrec | TRUE to use the documents precision value, FALSE otherwise |
| Input: | (long) precision | Precision value to use for this dimension |
| Input: | (long) arrowsIn | Value for the arrow direction as defined in swDimensionArrowsSide_e |
| Input: | (VARIANT_BOOL) useDocArrows | TRUE to use the documents arrow types, FALSE otherwise |
| Input: | (long) arrow1 | Type of arrow to use on the first arrow of this dimension as defined in swArrowStyle_e |
| Input: | (long) arrow2 | Type of arrow to use on the second arrow of this dimension as defined in swArrowStyle_e |
| Input: | (BSTR) prefixText | Text for the prefix of this dimension |
| Input: | (BSTR) suffixText | Text for the suffix of this dimension |
| Input: | (VARIANT_BOOL) showValue | TRUE if you want to display the value of this dimension in the user interface, FALSE otherwise |
| Input: | (BSTR) calloutText1 | Callout text above the dimension |
| Input: | (BSTR) calloutText2 | Callout text below the dimension |
| Input: | (VARIANT_BOOL) centerText | TRUE if you want to center the text in this dimension, FALSE otherwise |
| Output: | (VARIANT_BOOL) retval | TRUE if the dimension is modified, FALSE otherwise |
| Return: | (HRESULT) status | S_OK if successful |

Remarks
