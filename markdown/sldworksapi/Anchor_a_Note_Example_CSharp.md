---
title: "Anchor a Note Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Anchor_a_Note_Example_CSharp.htm"
---

# Anchor a Note Example (C#)

This example shows how to:

- insert a note.
- set a note's text to all uppercase and its vertical justification to bottom.
- anchor and position a note.

```
//----------------------------------------------------------------------------------
// Preconditions: Open public_documents\samples\tutorial\advdrawings\foodprocessor.slddrw.
//
// Postconditions:
// 1. Inserts a note.
// 2. Sets the note's text to all uppercase and its vertical justification
//    to bottom.
// 3. Locks the note at the specified position.
// 4. Examine the graphics area.
//
// NOTE: Because the model is used elsewhere, do not save changes.
// --------------------------------------------------------------------------------
using System;
using System.Diagnostics;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;

namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        ModelDoc2 Part;
        Note myNote;
        Annotation myAnnotation;
        bool boolstatus;

        public void Main()
        {
            Part = (ModelDoc2)swApp.ActiveDoc;

            myNote = (Note)Part.InsertNote("Drawing View1 Note");
            if ((myNote != null))
            {
                myNote.AllUpperCase = true;
                myNote.SetTextVerticalJustification((int)swTextAlignmentVertical_e.swTextAlignmentBottom);
                myNote.LockPosition = true;
                myAnnotation = (Annotation)myNote.GetAnnotation();
                if ((myAnnotation != null))
                {
                    boolstatus = myAnnotation.SetPosition(0.2, 0.269, 0);
                }
            }

            Part.ClearSelection2(true);
            Part.WindowRedraw();
        }
        public SldWorks swApp;
    }
}
```
