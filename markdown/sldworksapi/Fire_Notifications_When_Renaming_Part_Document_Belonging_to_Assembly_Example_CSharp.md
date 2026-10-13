---
title: "Fire Notifications When Renaming Part Document Belonging to Assembly Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Fire_Notifications_When_Renaming_Part_Document_Belonging_to_Assembly_Example_CSharp.htm"
---

# Fire Notifications When Renaming Part Document Belonging to Assembly Example (C#)

This example shows how to fire notifications when you:

- are about to rename a part document belonging to an assembly.
- rename the part document.

```
//----------------------------------------------------------------------
// Preconditions:
// 1. Open public_documents\samples\tutorial\EDraw\claw\center.sldprt.
// 2. Open the Immediate window.
//
// Postconditions:
// 1. Renames center to centerXXX.
// 2. Fires the PreRenameItemNotify and RenameItemNotify events.
// 3. Examine the FeatureManager design tree and Immediate window.
//
// NOTE: Because the part is used elsewhere, do not save changes.
//---------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System.Runtime.InteropServices;
using System;
using System.Diagnostics;
using System.Collections;

namespace Macro1CSharp.csproj
{
    public partial class SolidWorksMacro
    {
        public PartDoc swPart;

        public void Main()
        {
            ModelDoc2 swModel = default(ModelDoc2);
            ModelDocExtension swModelDocExt = default(ModelDocExtension);
            Hashtable openPart = default(Hashtable);
            int errors = 0;
            bool status = false;

            swModel = (ModelDoc2)swApp.ActiveDoc;

            //Set up event
            swPart = (PartDoc)swModel;
            openPart = new Hashtable();
            AttachEventHandlers();

            swModelDocExt = (ModelDocExtension)swModel.Extension;
            status = swModelDocExt.SelectByID2("center.sldprt", "COMPONENT", 0, 0, 0, false, 0, null, 0);
            errors = swModelDocExt.RenameDocument("centerXXX");

        }

        public void AttachEventHandlers()
        {
            AttachSWEvents();
        }

        public void AttachSWEvents()
        {
            if ((swPart != null))
            {
                swPart.PreRenameItemNotify += this.swPart_PreRenameItemNotify;
                swPart.RenameItemNotify += this.swPart_RenameItemNotify;
            }
        }

        //Fire notification when item is about to be renamed
        public int swPart_PreRenameItemNotify(int entType, string oldName, string newName)
        {
            Debug.Print("PreRenameItemNotify fired");
            return 0;
        }
        //Fire notification when item is renamed
        public int swPart_RenameItemNotify(int entType, string oldName, string newName)
        {
            Debug.Print("RenameItemNotify fired");
            return 0;
        }

        /// <summary>
        ///  The SldWorks swApp variable is pre-assigned for you.
        /// </summary>
        public SldWorks swApp;
    }
}
```
