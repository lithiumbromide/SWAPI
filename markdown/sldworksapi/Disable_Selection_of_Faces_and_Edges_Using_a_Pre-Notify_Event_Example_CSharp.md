---
title: "Disable Selection of Faces and Edges Using a Pre-Notify Event Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Disable_Selection_of_Faces_and_Edges_Using_a_Pre-Notify_Event_Example_CSharp.htm"
---

# Disable Selection of Faces and Edges Using a Pre-Notify Event Example (C#)

This example shows how to disable the interactive selection of these entities using a pre-notify event:

- faces in part and assembly documents
- edges in drawing documents

```
//---------------------------------------------------
// Preconditions: Open a part, assembly, or drawing.
//
// NOTE: Tools > Options > System > Stop VSTA debugger
// on macro exit must be cleared for this macro
// to run to completion.
//
// Postconditions:
// 1. Disables interactively selecting faces in
//    a part or assembly.
//    - or -
//    Disables interactively selecting edges in a
//    drawing.
// 2. Click the Stop Debugging button in the
//    SOLIDWORKS Visual Studio Tools for
//    Applications IDE to re-enable the
//    interactive selection of faces in
//    a part or assembly document or edges in
//    a drawing document.
//----------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
namespace Macro1CSharp.csproj
{
    partial class SolidWorksMacro
    {
        public PartDoc pDoc;
        public AssemblyDoc aDoc;
        public DrawingDoc dDoc;
        public void Main()
        {
            ModelDoc2 swModel;
            Hashtable openPart;
            Hashtable openAssembly;
            Hashtable openDrawing;
```

```
            swModel = (ModelDoc2)swApp.ActiveDoc;
```

```
            // Determine the document type
            // and set up event handlers
            if (swModel.GetType() == (int)swDocumentTypes_e.swDocPART)
            {
                pDoc = (PartDoc)swModel;
                openPart = new Hashtable();
            }
            else if (swModel.GetType() == (int)swDocumentTypes_e.swDocASSEMBLY)
            {
                aDoc = (AssemblyDoc)swModel;
                openAssembly = new Hashtable();
            }
            else if (swModel.GetType() == (int)swDocumentTypes_e.swDocDRAWING)
            {
                dDoc = (DrawingDoc)swModel;
                openDrawing = new Hashtable();
            }
            AttachEventHandlers();
        }
```

```
        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }
```

```
        public void AttachSWEvents()
        {
            if ((pDoc != null))
            {
                pDoc.UserSelectionPreNotify += this.pDoc_UserSelectionPreNotify;
            }
            if ((aDoc != null))
            {
                aDoc.UserSelectionPreNotify += this.aDoc_UserSelectionPreNotify;
            }
            if ((dDoc != null))
            {
                dDoc.UserSelectionPreNotify += this.dDoc_UserSelectionPreNotify;
            }
        }
```

```
        private int pDoc_UserSelectionPreNotify(int SelectionType)
        {
            int functionReturnValue = 0;
            // Disable the selection of faces in this part
            if (SelectionType == (int)swSelectType_e.swSelFACES)
            {
                functionReturnValue = 1;
            }
            return functionReturnValue;
        }
```

```
        public int aDoc_UserSelectionPreNotify(int SelectionType)
        {
            int functionReturnValue = 0;
            // Disable the selection of faces in this assembly
            if (SelectionType == (int)swSelectType_e.swSelFACES)
            {
                functionReturnValue = 1;
            }
            return functionReturnValue;
        }
```

```
        private int dDoc_UserSelectionPreNotify(int SelectionType)
        {
            int functionReturnValue = 0;
            // Disable the selection of edges in this drawing
            if (SelectionType == (int)swSelectType_e.swSelEDGES)
            {
                functionReturnValue = 1;
            }
            return functionReturnValue;
        }
```

```
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
