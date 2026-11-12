---
title: "Get Preselected Object Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Preselected_Object_Example_CSharp.htm"
---

# Get Preselected Object Example (C#)

This example shows how to get a preselected object when a preselection event is fired.

```
//-----------------------------------------------------------
// Preconditions:
// 1. Open a part, assembly, or drawing document.
// 2. Click Tools > Options > System Options > Stop VSTA debugger
//    on macro exit if the check box is selected.
// 3. If a part or assembly document is active, then
//    preselect (mouse over) a face.
//    - or -
//    If a drawing document is active, then pre-elect
//    an edge.
// 4. Open the Immediate window.
//
// Postconditions:
// 1. When a face is preselected in a part or assembly
//    document, or an edge is pre-selected in a drawing document,
//    then that interface's UserSelectionPreNotify event is fired.
// 2. To stop running the macro, click Debug > Stop Debugging
//    in the SolidWorks Visual Studio Tools for Applications IDE.
// 3. Examine the Immediate window.
// 4. Click Tools > Options > System Options > Stop VSTA debugger
//    on macro exit to select the check box.
//------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Collections;
using System.Diagnostics;
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

            swModel = (ModelDoc2)swApp.ActiveDoc;

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
        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }
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
        private int pDoc_UserSelectionPreNotify(int SelectionType)
        {
            int functionReturnValue = 0;
            ModelDoc2 swModel;
            SelectionMgr swSelMgr;
            object SelectedObject;
            Face2 swFace;
            Feature swFeature;
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            SelectedObject = (object)swSelMgr.GetPreSelectedObject();
            if (SelectionType == (int)swSelectType_e.swSelFACES)
            {
                swFace = (Face2)SelectedObject;
                swFeature = (Feature)swFace.GetFeature();
                Debug.Print("Name of feature whose face you preselected: " + swFeature.Name);
                Debug.Print("   Mouse over a different face, or click Debug > Stop Debugging to stop running macro");
                Debug.Print(" ");
                functionReturnValue = 1;
            }
            return functionReturnValue;
        }
        public int aDoc_UserSelectionPreNotify(int SelectionType)
        {
            int functionReturnValue = 0;
            ModelDoc2 swModel;
            SelectionMgr swSelMgr;
            object SelectedObject;
            Face2 swFace;
            Feature swFeature;
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            SelectedObject = (object)swSelMgr.GetPreSelectedObject();
            if (SelectionType == (int)swSelectType_e.swSelFACES)
            {
                swFace = (Face2)SelectedObject;
                swFeature = (Feature)swFace.GetFeature();
                Debug.Print("Name of feature whose face you preselected: " + swFeature.Name);
                Debug.Print("   Mouse over a different face, or click Debug > Stop Debugging to stop running macro");
                Debug.Print(" ");
                functionReturnValue = 1;
            }
            return functionReturnValue;
        }
        private int dDoc_UserSelectionPreNotify(int SelectionType)
        {
            int functionReturnValue = 0;
            ModelDoc2 swModel;
            SelectionMgr swSelMgr;
            object SelectedObject;
            Edge swEdge;
            Body2 swBody;
            swModel = (ModelDoc2)swApp.ActiveDoc;
            swSelMgr = (SelectionMgr)swModel.SelectionManager;
            SelectedObject = (object)swSelMgr.GetPreSelectedObject();
            if (SelectionType == (int)swSelectType_e.swSelEDGES)
            {
                swEdge = (Edge)SelectedObject;
                swBody = (Body2)swEdge.GetBody();
                Debug.Print("Name of body whose edge you preselected: " + swBody.Name);
                Debug.Print("   Mouse over a different edge, or click Debug > Stop Debugging to stop running macro");
                Debug.Print(" ");
                functionReturnValue = 1;
            }
            return functionReturnValue;
        }
        /// <summary>
        /// The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
