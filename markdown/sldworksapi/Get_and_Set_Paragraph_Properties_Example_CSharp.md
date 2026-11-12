---
title: "Get and Set Paragraph Properties Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Paragraph_Properties_Example_CSharp.htm"
---

# Get and Set Paragraph Properties Example (C#)

This example shows how to get and set the properties of paragraphs in note annotations.

```vb
  //----------------------------------------------------------------------------
 // Preconditions:
  // 1. Open a drawing with a note annotation that contains one or more
 //    paragraphs.
 // 2. Select the annotation in the graphics area.
 // 3. Open an Immediate window.
 //
 // Postconditions:
 // 1. For each paragraph in the selected note:
 //    * Sets the paragraph and line spacing.
  //    * Gets properties of numbered lists, if present.
 //    * Gets text segment formatting.
 //    * Bolds the text of each text segment.
 // 2. Inspect the Immediate window.
  //----------------------------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetParagraphs_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         public void Main()
         {
             ModelDoc2 swModel = default(ModelDoc2);
             SelectionMgr swSelMgr = default(SelectionMgr);
             Note noteObj = default(Note);
             Annotation swAnn = default(Annotation);
             Paragraphs paragraphs = default(Paragraphs);
             int numSegs = 0;
             int paragraphIndex = 0;
             int iseg = 0;
             TextFormat textFormat = default(TextFormat);
             int paraType = 0;
             int numberingtype = 0;
             int startas = 0;
             int format = 0;
             int numtype = 0;
             int numParagraphs = 0;
             string Text = null;

             swModel = (ModelDoc2)swApp.ActiveDoc;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             if (swSelMgr.GetSelectedObjectCount() > 0)
             {
                 noteObj = (Note)swSelMgr.GetSelectedObject6(1, -1);
                 swAnn = (Annotation)noteObj.GetAnnotation();
                 paragraphs = (Paragraphs)swAnn.GetParagraphs();

                 numParagraphs = paragraphs.Count;
                 Debug.Print("Number of paragraphs = " + numParagraphs);
                 Debug.Print("");

                 for (paragraphIndex = 0; paragraphIndex <= numParagraphs - 1; paragraphIndex++)
                 {
                     paragraphs.CurrentParagraph = paragraphIndex;
                     Debug.Print("paragraph(" + paragraphIndex + "): ");
                     Debug.Print(paragraphs.GetText(true));

                     if (paragraphIndex == 0)
                     {
                         paragraphs.SetFormatting(0.0011, 0.0012);
                     }
                     else
                     {
                         paragraphs.SetFormatting(0.0021, 0.0022);
                     }

                     paragraphs.GetBulletsAndNumbering(out paraType, out numberingtype, out startas, out numtype, out format);
                     Debug.Print("Paragraph list type as defined in swParagraphType_e: " + paraType);
                     if (paraType == 1)
                     {
                         Debug.Print("Numbered list:");
                         Debug.Print("  Start numbering from location as defined in swNumberedListStartType_e: " + numberingtype);
                         Debug.Print("  Start numbering index: " + startas);
                         Debug.Print("  Type as defined in swNumberedListType_e: " + numtype);
                         Debug.Print("  Format as defined in swNumberingFormat_e: " + format);
                     }

                     numSegs = paragraphs.GetTextSegmentCount();
                     Debug.Print("Text segment count: " + numSegs);

                     for (iseg = 0; iseg <= numSegs - 1; iseg++)
                     {
                         Text = paragraphs.GetTextSegmentText(iseg);
                         Debug.Print("segment(" + iseg + "): " + Text);

                         textFormat = (TextFormat)paragraphs.GetTextSegmentFormat(iseg);
                         Debug.Print("  Typeface: " + textFormat.TypeFaceName);
                         Debug.Print("  Backwards? " + textFormat.BackWards);
                         Debug.Print("  Bold? " + textFormat.Bold);
                         Debug.Print("  Italic? " + textFormat.Italic);
                         Debug.Print("  Strikeout? " + textFormat.Strikeout);

                         textFormat.Bold = true;
                         paragraphs.SetTextSegmentFormat(iseg, textFormat);

                     }

                     paragraphs.UpdateParagraph();

                 }

                 swModel.GraphicsRedraw2();

             }

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }

 }
```
