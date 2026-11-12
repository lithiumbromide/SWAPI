---
title: "Get Notes from New or Existing Title Block (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm"
---

# Get Notes from New or Existing Title Block (C#)

This example shows how to create a title block in a drawing, if one does not already exist, and how to get the notes from an existing title block in a drawing.

```vb
//--------------------------------------------------------
// Preconditions: Drawing document is open.
//
// Postconditions: If the drawing contains a title block, then
//                 the notes of that block are printed
//                 to the Immediate window. If not,
//                 a title block is created.
//-------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
namespace ExampleCS.csproj
{
    public partial class SolidWorksMacro
    {
        ModelDoc2 swModel;
        ModelDocExtension swExt;
        SelectionMgr swSelMgr;
        View swView;
        DrawingDoc swDraw;
        public void Main()
        {
            swModel = swApp.ActiveDoc as ModelDoc2;
            swExt = swModel.Extension;
            swSelMgr = swModel.SelectionManager as SelectionMgr;
            swDraw = swModel as DrawingDoc;
            Sheet swSheet;
            swSheet = swDraw.GetCurrentSheet() as Sheet;
            TitleBlock swTitleBlock;
            swTitleBlock = swSheet.TitleBlock;
            object[] vNotes;
            int i;
            // Create title block if one doesn't exist
            if (swTitleBlock == null)
            {
                swView = swDraw.GetFirstView() as View;
                vNotes = (object[])swView.GetNotes();
                // Add first two notes to the title block
                DispatchWrapper[] notesArray = new DispatchWrapper[2];
                notesArray[0] = new DispatchWrapper(vNotes[0]);
                notesArray[1] = new DispatchWrapper(vNotes[1]);
                swTitleBlock = swSheet.InsertTitleBlock(notesArray);
            }
            vNotes = (object[])swTitleBlock.GetNotes();
            for (i = 0; i < vNotes.Length; i++)
            {
                Note swNote;
                swNote = (Note)vNotes[i];
                Debug.Print("Name: " + swNote.GetName());
                Debug.Print("Value: " + swNote.GetText());
            }
        }
        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
