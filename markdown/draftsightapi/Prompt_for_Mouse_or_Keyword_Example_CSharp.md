---
title: "Prompt for Mouse or Keyword Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Prompt_for_Mouse_or_Keyword_Example_CSharp.htm"
---

# Prompt for Mouse or Keyword Example (C#)

This example shows how to create a prompting cursor (tracker) that displays a simple note as you prompt the user for where to insert the simple note in the graphics area.

//--------------------------------------------------------------
// Preconditions:
// 1. Create a C# Windows console project.
// 2. Copy and paste this example into the C# IDE.
// 3. Add a reference to:
// `install_dir`\**APISDK\tlb\DraftSight.Interop.dsAutomation.dll**
// 4. Add references to **System** and **System.Windows.Forms**.
// 5. Start DraftSight.
// 6. Press F5 to debug the project.
//
// Postconditions:
// 1. Prompts the user for some text and its properties.
// 2. Creates a prompting tracker with the text.
// 3. Prompts the user for the insertion point of the text.
// 4. Inserts the text at the user-specified location.
//----------------------------------------------------------------

```vb
 using System;
 using System.Collections.Generic;
 using System.Linq;
 using System.Text;
 using System.Threading.Tasks;
 using System.Runtime.InteropServices;
 using DraftSight.Interop.dsAutomation;
 using System.Windows.Forms;

 namespace PromptForMouseOrKeywordConsoleApp1
 {
       class  Program
      {
            public  static SimpleNote m_note =   null;
            static  void Main(string[] args)
           {
               //Connect to DraftSight application
              DraftSight.Interop.dsAutomation.Application application = ConnectToDraftSight();
               if (null == application)
              {
                   return;
              }

              application.AbortRunningCommand();   // abort any command currently running in DraftSight to avoid nested commands
              CommandMessage dsCommandMessage = application.GetCommandMessage();
               if (null == dsCommandMessage)
              {
                   return;
              }

              Document dsDoc = application.GetActiveDocument();
               if (null == dsDoc)
              {
                   return;
              }

              MathUtility dsMathUtility = application.GetMathUtility();
               if (null == dsMathUtility)
              {
                   return;
              }

              Model dsModel = dsDoc.GetModel();
               if (null == dsModel)
              {
                  return;
              }

              SketchManager dsSketchManager = dsModel.GetSketchManager();
               if (null == dsSketchManager)
              {
                   return;
              }

               bool result;
               string text =  "Hello, World!";
               double height = 1.2;
               double angle = 0;
               double x = 0, y = 0, z = 0;

              result = dsCommandMessage.PromptForString(true,  "Specify text", text,   out text);
               if (!result)
                   return;

              result = dsCommandMessage.PromptForDouble("Specify text height", height,   out height);
               if (!result)
                   return;

              result = dsCommandMessage.PromptForDouble("Specify text angle [deg]", angle,   out angle);
               if (!result)
                   return;

               //Angle in radians
              angle = angle * 3.1415926535897932384626433832795 / 180;

              result = dsCommandMessage.PromptForPoint("Specify insertion point",   out x,   out y,   out z);
               if (!result)
                   return;

              application.TemporaryEntityMode =   true;
              m_note = dsSketchManager.InsertSimpleNote(x, y, z, height, angle, text);
              application.TemporaryEntityMode =   false;

              Tracker tracker = application.CreateTracker();
               //Add the simple note to the tracker
              tracker.AddTemporaryEntity(m_note);
              dsCommandMessage.AddTracker(tracker);

              tracker.UpdateNotify +=   new _ITrackerEvents_UpdateNotifyEventHandler(UpdateNotify);

               //Keywords
               string keyword =   "";
               object global_keywords =   null;
               object local_keywords =   null;

              MathPoint insertion_point = dsMathUtility.CreatePoint(0, 0, 0);
              MathPlane xy_plane = dsMathUtility.CreateXYPlane();

              dsPromptResultType_e dsPromptResult = dsPromptResultType_e.dsPromptResultType_None;
              dsPromptKeyboardModificators2_e keyboardModificator = dsPromptKeyboardModificators2_e.dsPromptKeyboardModificators_Unknown;
              dsMouseEventType_e mouseEvnt = dsMouseEventType_e.dsMouseEventType_Unknown;

              dsPromptResult = dsCommandMessage.PromptForMouseOrKeyword2(
                   "Specify insertion point",
                   "Invalid input",
                  global_keywords,
                  local_keywords,
                  0,
                   false,
                  insertion_point,
                  insertion_point,
                  xy_plane,
                   out keyword,
                   out insertion_point,
                   out keyboardModificator,
                   out mouseEvnt);

              dsCommandMessage.PrintLine("\n");
              dsCommandMessage.PrintLine("Keyboard modificator: " + keyboardModificator.ToString());
              dsCommandMessage.PrintLine("\n");
              dsCommandMessage.PrintLine("Mouse event: " + mouseEvnt.ToString());
              dsCommandMessage.PrintLine("\n");

              dsCommandMessage.RemoveTracker(tracker);

              tracker.UpdateNotify -=   new _ITrackerEvents_UpdateNotifyEventHandler(UpdateNotify);

               //Add the simple note to the graphics area   at the user-specified insertion point
              insertion_point.GetPosition(out x, out y, out z);
             m_note.SetPosition(x, y, z);
              dsSketchManager.AddTemporaryEntity(m_note);
           }
            public  static  void UpdateNotify(MathPoint CursorPosition)
           {
               if (CursorPosition ==   null || m_note ==   null)
                   return;

               double x = 0.0, y = 0.0, z = 0.0;
              CursorPosition.GetPosition(out x,   out y,   out z);

              m_note.SetPosition(x, y, z);
           }
            public  static DraftSight.Interop.dsAutomation.Application ConnectToDraftSight()
           {

              DraftSight.Interop.dsAutomation.Application dsApp =  null;

               try
              {
                 //Connect to DraftSight
                 dsApp = (DraftSight.Interop.dsAutomation.Application)Marshal.GetActiveObject("DraftSight.Application");
              }
               catch (Exception ex)
              {
                  MessageBox.Show("Failed to connect to DraftSight. Cause: " + ex.Message);
                  dsApp =   null;
              }

               return dsApp;
           }
      }
 }
```
