---
title: "Fire Selection After Selection Made Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Event_After_Selection_Made_Example_CSharp.htm"
---

# Fire Selection After Selection Made Example (C#)

This example shows how to fire an event after a selection is made in a part, assembly, or drawing document.

```
//------------------------------------------------------
// Preconditions: Open a part, assembly, or drawing.
//
// Postconditions:
// 1. Select an entity.
// 2. Displays a message box confirming your
//    selection.
//    NOTE: If necessary, click the message box icon
//    on the Windows taskbar to display the message box.
// 3. Click OK to close the message box.
//
// NOTE: Tools > Options > System>  Stop VSTA debugger
// on macro exit must be cleared for this macro to run to
// completion.
//-------------------------------------------------------

using SolidWorks.Interop.sldworks;

using SolidWorks.Interop.swconst;

using System;

using System.Windows.Forms;

namespace UserSelectionPostNotifyEventCSharp.csproj

{

    partial class SolidWorksMacro

    {

        public PartDoc pDoc;

        public AssemblyDoc aDoc;

        public DrawingDoc dDoc;

        public void Main()

        {

            ModelDoc2 swModel;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            // Determine the document type

            // and set up
event handlers

            if (swModel.GetType() == (int)swDocumentTypes_e.swDocPART)

            {

                pDoc = (PartDoc)swModel;

            }

            else if (swModel.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)

            {

                aDoc = (AssemblyDoc)swModel;

            }

            else if (swModel.GetType() == (int)swDocumentTypes_e.swDocDRAWING)

            {

                dDoc = (DrawingDoc)swModel;

            }

            AttachEventHandlers();

        }

        public void AttachEventHandlers()

        {

            AttachSWEvents();

        }

        public void AttachSWEvents()

        {

            if ((pDoc != null))

            {

                pDoc.UserSelectionPostNotify += this.pDoc_UserSelectionPostNotify;

            }

            if ((aDoc != null))

            {

                aDoc.UserSelectionPostNotify += this.aDoc_UserSelectionPostNotify;

            }

            if ((dDoc != null))

            {

                dDoc.UserSelectionPostNotify += this.dDoc_UserSelectionPostNotify;

            }

        }

        private int pDoc_UserSelectionPostNotify()

        {

            int functionReturnValue = 0;

            MessageBox.Show("An entity was selected
in a part document.");

            return functionReturnValue;

        }

        public int aDoc_UserSelectionPostNotify()

        {

            int functionReturnValue = 0;

            MessageBox.Show("An entity was selected
in a assembly document.");

            return functionReturnValue;

        }

        private int dDoc_UserSelectionPostNotify()

        {

            int functionReturnValue = 0;

            MessageBox.Show("An entity was selected
in a drawing document.");

            return functionReturnValue;

        }

        /// <summary>

        /// The SldWorks swApp variable is pre-assigned for you.

        /// </summary>

        public SldWorks swApp;

    }

}
```
