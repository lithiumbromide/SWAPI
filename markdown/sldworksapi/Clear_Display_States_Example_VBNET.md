---
title: "Clear Display States Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Clear_Display_States_Example_VBNET.htm"
---

# Clear Display States Example (VB.NET)

This example shows how to clear the display states from a part. This example also shows how to remove appearances and show any hidden features.

```
'----------------------------------------------------------------------------
' Preconditions: Open a part document that has any of the following:
' * appearances
' * linked display states
' * hidden features
'
' Postconditions:
' 1. Removes appearances from all configurations of the part.
' 2. Clears display states from all configurations.
' 3. Shows hidden features.
' ---------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Partial Class SolidWorksMacro

	    Dim modelDoc As ModelDoc2

	    Dim partDoc As PartDoc

	    Dim boolstatus As Boolean

	    Sub main()

	        modelDoc = swApp.ActiveDoc

	        partDoc = modelDoc

	        boolstatus = partDoc.RemoveAllDisplayStates

	    End Sub

	    Public swApp As SldWorks

	End Class
```
