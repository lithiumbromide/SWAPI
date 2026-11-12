---
title: "Paint Features Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swutilitiesapi/Paint_Features_VB6.htm"
---

# Paint Features Example (VBA)

This example shows how to copy the source feature's parameters to the target feature using the SOLIDWORKS Utilities API.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Add the SOLIDWORKS Utilities as an add-in
'    (in SOLIDWORKS, click Tools > Add-Ins > SOLIDWORKS Utilities).
' 2. Add the SOLIDWORKS Utilities type library as a reference
'    (in the SOLIDWORKS Microsoft Visual Basic for Applications IDE, click
'    Tools > References > SolidWorks Utilities <version> Type Library).
' 3. Open public_documents\samples\tutorial\toolbox\braceleft.sldprt and
'    frontplate.sldprt.
'
' Postconditions:
' 1. Runs PowerSelect and paints the Base-Extrude feature of frontplate.sldprt
'    the same color as the Base-Extrude feature of braceleft.sldrpt.
' 2. Examine frontplate.sldprt.
'
' NOTE: Because the parts are used elsewhere, do not save changes.
'------------------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swUtil As SWUtilities.gtcocswUtilities
    Dim swUtilFeatPaint As SWUtilities.gtcocswFeaturePaint
    Dim errorcode As gtError_e
```

```
    ' Connect to SOLIDWORKS
    Set swApp = Application.SldWorks
```

```
    ' Get the SOLIDWORKS Utilities interface
    Set swUtil = swApp.GetAddInObject("Utilities.UtilitiesApp")
    Set swUtilFeatPaint = swUtil.GetToolInterface(gtSwToolFeatPaint, 0)
```

```
    ' Copy the source feature's parameters to the target feature
    errorcode = swUtilFeatPaint.FeaturePaint("Base-Extrude@C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\braceleft.sldprt",
    "Base-Extrude@C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\frontplate.sldprt")
```

```
End Sub
```
