---
title: "Clear Display States Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Clear_Display_States_Example_CSharp.htm"
---

# Clear Display States Example (C#)

This example shows how to clear the display states from a part. This example also shows how to remove appearances and show any hidden features.

```
//----------------------------------------------------------------------------
// Preconditions: Open a part document that has any of the following:
// * appearances
// * linked display states
// * hidden features
//
// Postconditions:
// 1. Removes appearances from all configurations of the part.
// 2. Clears display states from all configurations.
// 3. Shows hidden features.
// ---------------------------------------------------------------------------

	using Microsoft.VisualBasic;

	using System;

	using System.Collections;

	using System.Collections.Generic;

	using System.Data;

	using System.Diagnostics;

	using SolidWorks.Interop.sldworks;

	using SolidWorks.Interop.swconst;

	using System.Runtime.InteropServices;

	namespace RemoveAllDisplayStates_CSharp.csproj

	{

	    partial class SolidWorksMacro

	    {

	        ModelDoc2 modelDoc;

	        PartDoc partDoc;

	        bool boolstatus;

	        public void Main()

	        {

	            modelDoc = (ModelDoc2)swApp.ActiveDoc;

	            partDoc = (PartDoc)modelDoc;

	            boolstatus = partDoc.RemoveAllDisplayStates();

	        }

	        public SldWorks swApp;

	    }

	}
```
