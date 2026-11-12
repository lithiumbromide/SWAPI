---
title: "Create CommandManager Tab and Tab Boxes Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_CommandManager_Tab_and_Tab_Boxes_Example_CSharp.htm"
---

# Create CommandManager Tab and Tab Boxes Example (C#)

This example shows how to create an add-in that creates a CommandManager tab and tab boxes.

NOTES:

- This sample code is part of a project that was built using the C# Add-In Wizard.
- To run this sample code, you need to create a complete C# project.
- Your add-in must check to see if the tab already exists. If the tab already exists, then you should use that tab instead of creating a new tab. If your add-in does not check for an existing tab, then SOLIDWORKS Design will create a new tab each time it starts up.
- Users can add buttons to and remove buttons from your CommandManager tab. However, if your add-in removes the CommandManager tab upon exiting SOLIDWORKS Design, then any user customizations will be lost.

\\------------------------------------------------------------------------------------------------------------------------------

#### \\ SwAddin.cs

```vb
using System;
using System.Diagnostics;
using System.Collections;
using System.Reflection;
using System.Runtime.InteropServices;
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using SolidWorks.Interop.swpublished;
using SolidWorksTools;
using SolidWorksTools.File;
namespace SwCSharpAddin1
{
    [Guid("c5ede50f-7484-416b-9425-ca49f565e48e")]
    [ComVisible(true)]
    [SwAddin(Description = "test description", Title = "test", LoadAtStartup = true)]
    public class SwAddin : SolidWorks.Interop.swpublished.SwAddin
    {
        #region "Local Variables"
        SldWorks iSwApp;
        ICommandManager iCmdMgr;
        int addinID;
        Hashtable openDocs;
        SldWorks SwEventPtr;
        UserPMPage ppage;
        // Public Properties
        public SldWorks SwApp
        {
            get { return iSwApp; }
        }
        public ICommandManager CmdMgr
        {
            get { return iCmdMgr; }
        }
        public Hashtable OpenDocumentsTable
        {
            get { return openDocs; }
        }
        #endregion
        #region "SOLIDWORKS Registration"
        [ComRegisterFunction()]
        public static void RegisterFunction(Type t)
        {
            // Get Custom Attribute: SwAddinAttribute
            object[] attributes = null;
            SwAddinAttribute SWattr = null;
            attributes = System.Attribute.GetCustomAttributes(typeof(SwAddin), typeof(SwAddinAttribute));
            if (attributes.Length > 0)
            {
                SWattr = (SwAddinAttribute)attributes[0];
            }
            Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
            Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;
            string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
            Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);
            addinkey.SetValue(null, 0);
            addinkey.SetValue("Description", SWattr.Description);
            addinkey.SetValue("Title", SWattr.Title);
            keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
            addinkey = hkcu.CreateSubKey(keyname);
            addinkey.SetValue(null, SWattr.LoadAtStartup, Microsoft.Win32.RegistryValueKind.DWord);
        }
        [ComUnregisterFunction()]
        public static void UnregisterFunction(Type t)
        {
            Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
            Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;
            string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
            hklm.DeleteSubKey(keyname);
            keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
            hkcu.DeleteSubKey(keyname);
        }
        #endregion
        #region "ISwAddin Implementation"
        public bool ConnectToSW(object ThisSW, int Cookie)
        {
            iSwApp = (SldWorks)ThisSW;
            addinID = Cookie;
            // Setup callbacks
            iSwApp.SetAddinCallbackInfo(0, this, addinID);
            // Setup the Command Manager
            iCmdMgr = iSwApp.GetCommandManager(Cookie);
            AddCommandMgr();
            //Setup the Event Handlers
            SwEventPtr = iSwApp;
            openDocs = new Hashtable();
            AttachEventHandlers();
            //Setup Sample Property Manager
            AddPMP();
            return true;
        }
        public bool DisconnectFromSW()
        {
            RemoveCommandMgr();
            RemovePMP();
            DetachEventHandlers();
            iSwApp = null;
            //The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
            GC.Collect();
            return true;
        }
        #endregion
        #region "UI Methods"
        public void AddCommandMgr()
        {
            ICommandGroup cmdGroup = default(ICommandGroup);
            BitmapHandler iBmp = new BitmapHandler();
            Assembly thisAssembly = default(Assembly);
            int cmdIndex0 = 0;
            int cmdIndex1 = 0;
            string Title = "C# Addin";
            string ToolTip = "C# Addin";
            int[] docTypes = { (int)swDocumentTypes_e.swDocASSEMBLY, (int)swDocumentTypes_e.swDocDRAWING, (int)swDocumentTypes_e.swDocPART };
            thisAssembly = System.Reflection.Assembly.GetAssembly(this.GetType());
            cmdGroup = iCmdMgr.CreateCommandGroup(1, Title, ToolTip, "", -1);
            cmdGroup.LargeIconList = iBmp.CreateFileFromResourceBitmap("test.ToolbarLarge.bmp", thisAssembly);
            cmdGroup.SmallIconList = iBmp.CreateFileFromResourceBitmap("test.ToolbarSmall.bmp", thisAssembly);
            cmdGroup.LargeMainIcon = iBmp.CreateFileFromResourceBitmap("test.MainIconLarge.bmp", thisAssembly);
            cmdGroup.SmallMainIcon = iBmp.CreateFileFromResourceBitmap("test.MainIconSmall.bmp", thisAssembly);
            cmdIndex0 = cmdGroup.AddCommandItem2("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", 0, 1);
            cmdIndex1 = cmdGroup.AddCommandItem2("Show PMP", -1, "Display sample property manager", "Show PMP", 2, "ShowPMP", "PMPEnable", 2, 1);
            cmdGroup.HasToolbar = true;
            cmdGroup.HasMenu = true;
            cmdGroup.Activate();
            foreach (int docType in docTypes)
            {
                ICommandTab cmdTab = iCmdMgr.GetCommandTab(docType, Title);
                bool bResult = false;
                if (cmdTab == null)
                {
                    cmdTab = iCmdMgr.AddCommandTab(docType, Title);
                    CommandTabBox cmdBox = cmdTab.AddCommandTabBox();
                    int[] cmdIDs = new int[4];
                    int[] TextType = new int[4];
                    cmdIDs[0] = cmdGroup.get_CommandID(cmdIndex0);
                    TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;
                    cmdIDs[1] = cmdGroup.get_CommandID(cmdIndex1);
                    TextType[1] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;
                    cmdIDs[2] = cmdGroup.ToolbarId;
                    TextType[2] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;
                    bResult = cmdBox.AddCommands(cmdIDs, TextType);
                    // Call GetCommands to confirm number of commands added
                    int buttonNumber = 0;
                    object idObject = null;
                    object textTypeObject = null;
                    buttonNumber = cmdBox.GetCommands(out idObject, out textTypeObject);
                    Debug.Print("Added " + buttonNumber + " commands.");
                    CommandTabBox cmdBox1 = cmdTab.AddCommandTabBox();
                    cmdIDs = new int[1];
                    TextType = new int[1];
                    cmdIDs[0] = cmdGroup.ToolbarId;
                    TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow;
                    bResult = cmdBox1.AddCommands(cmdIDs, TextType);
                    cmdTab.AddSeparator(cmdBox1, cmdGroup.ToolbarId);

                }
            }

            thisAssembly = null;
            iBmp.Dispose();
        }
        public void RemoveCommandMgr()
        {
            iCmdMgr.RemoveCommandGroup(1);
        }
        public bool AddPMP()
        {
            ppage = new UserPMPage(this);
            return true;
        }
        public bool RemovePMP()
        {
            ppage = null;
            return true;
        }
        #endregion
        #region "Event Methods"
        public void AttachEventHandlers()
        {
            AttachSWEvents();
            //Listen for events on all currently open docs
            AttachEventsToAllDocuments();
        }
        public void DetachEventHandlers()
        {
            DetachSWEvents();
            //Close events on all currently open docs
            DocumentEventHandler docHandler = default(DocumentEventHandler);
            IDictionaryEnumerator _enumerator = openDocs.GetEnumerator();
            while (_enumerator.MoveNext())
            {
                docHandler = (DocumentEventHandler)_enumerator.Value;
                docHandler.DetachEventHandlers();
                //This also removes the pair from the hash
                docHandler = null;
                //key = null;
            }
        }
        public void AttachSWEvents()
        {
            iSwApp.ActiveDocChangeNotify += this.SldWorks_ActiveDocChangeNotify;
            iSwApp.DocumentLoadNotify2 += this.SldWorks_DocumentLoadNotify2;
            iSwApp.FileNewNotify2 += this.SldWorks_FileNewNotify2;
            iSwApp.ActiveModelDocChangeNotify += this.SldWorks_ActiveModelDocChangeNotify;
            iSwApp.FileOpenPostNotify += this.SldWorks_FileOpenPostNotify;
        }
        public void DetachSWEvents()
        {
            iSwApp.ActiveDocChangeNotify -= this.SldWorks_ActiveDocChangeNotify;
            iSwApp.DocumentLoadNotify2 -= this.SldWorks_DocumentLoadNotify2;
            iSwApp.FileNewNotify2 -= this.SldWorks_FileNewNotify2;
            iSwApp.ActiveModelDocChangeNotify -= this.SldWorks_ActiveModelDocChangeNotify;
            iSwApp.FileOpenPostNotify -= this.SldWorks_FileOpenPostNotify;
        }
        public void AttachEventsToAllDocuments()
        {
            ModelDoc2 modDoc = default(ModelDoc2);
            modDoc = (ModelDoc2)iSwApp.GetFirstDocument();
            while ((modDoc != null))
            {
                if (!openDocs.Contains(modDoc))
                {
                    AttachModelDocEventHandler(modDoc);
                }
                modDoc = (ModelDoc2)modDoc.GetNext();
            }
        }
        public bool AttachModelDocEventHandler(ModelDoc2 modDoc)
        {
            if (modDoc == null)
            {
                return false;
            }
            DocumentEventHandler docHandler = null;
            if (!openDocs.Contains(modDoc))
            {
                switch (modDoc.GetType())
                {
                    case (int)swDocumentTypes_e.swDocPART:
                        docHandler = new PartEventHandler(modDoc, this);
                        break;
                    case (int)swDocumentTypes_e.swDocASSEMBLY:
                        docHandler = new AssemblyEventHandler(modDoc, this);
                        break;
                    case (int)swDocumentTypes_e.swDocDRAWING:
                        docHandler = new DrawingEventHandler(modDoc, this);
                        break;
                }

                docHandler.AttachEventHandlers();
                openDocs.Add(modDoc, docHandler);
            }
            return true;
        }
        public void DetachModelEventHandler(ModelDoc2 modDoc)
        {

            openDocs.Remove(modDoc);
            modDoc = null;

        }
        #endregion
        #region "Event Handlers"
        public int SldWorks_ActiveDocChangeNotify()
        {
            //TODO: Add your implementation here
            return 0;
        }
        public int SldWorks_DocumentLoadNotify2(string docTitle, string docPath)
        {
            ModelDoc2 modDoc = default(ModelDoc2);
            modDoc = (ModelDoc2)iSwApp.GetFirstDocument();
            while ((modDoc != null))
            {
                if (modDoc.GetTitle() == docTitle)
                {
                    if (!openDocs.Contains(modDoc))
                    {
                        AttachModelDocEventHandler(modDoc);
                    }
                }
                modDoc = (ModelDoc2)modDoc.GetNext();
            }
            return 0;
        }
        public int SldWorks_FileNewNotify2(object newDoc, int doctype, string templateName)
        {
            AttachEventsToAllDocuments();
            return 0;
        }
        public int SldWorks_ActiveModelDocChangeNotify()
        {
            //TODO: Add your implementation here
            return 0;
        }
        public int SldWorks_FileOpenPostNotify(string FileName)
        {
            AttachEventsToAllDocuments();
            return 0;
        }
        #endregion
        #region "UI Callbacks"
        public void CreateCube()
        {
            //make sure we have a part open
            string partTemplate = null;
            ModelDoc2 model = default(ModelDoc2);
            FeatureManager featMan = default(FeatureManager);
            partTemplate = iSwApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);
            model = (ModelDoc2)iSwApp.NewDocument(partTemplate, (int)swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0);
            model.InsertSketch2(true);
            model.SketchRectangle(0, 0, 0, 0.1, 0.1, 0.1, false);
            //Extrude the sketch
            featMan = model.FeatureManager;
            featMan.FeatureExtrusion(true, false, false, (int)swEndConditions_e.swEndCondBlind, (int)swEndConditions_e.swEndCondBlind, 0.1, 0.0, false, false, false,
            false, 0.0, 0.0, false, false, false, false, true, false, false
            );
        }
        public void ShowPMP()
        {
            ppage.Show();
        }
        public int PMPEnable()
        {
            int functionReturnValue = 0;
            if (iSwApp.ActiveDoc == null)
            {
                functionReturnValue = 0;
            }
            else
            {
                functionReturnValue = 1;
            }
            return functionReturnValue;
        }
        #endregion
    }
}
```
