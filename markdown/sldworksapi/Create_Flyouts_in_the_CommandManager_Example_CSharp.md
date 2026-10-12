---
title: "Create Flyouts in the CommandManager Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Flyouts_in_the_CommandManager_Example_CSharp.htm"
---

# Create Flyouts in the CommandManager Example (C#)

This example shows how to use an add-in to create flyouts in:

- CommandManager
- context-sensitive menus of selected faces

```
//--------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the SOLIDWORKS API SDK add-in templates for your version
//    of Microsoft Visual Studio are installed.
// 2. In Microsoft Visual Studio, create a C# project using the
//    SwCSharpAddin template.
// 3. Name the project FlyoutAddin.
// 4. Copy and paste SwAddin into SwAddin.cs of your project.
// 5. Click Project > FlyoutAddin Properties > Debug.
// 6. Select Start external program and type the pathname of your
//    SOLIDWORKS executable.
// 7. Replace the text shown for the icons and mainIcons array elements
//    with the pathnames of your image files.
// 8. Press F5 to start debugging this add-in.
//
// Postconditions:
// 1. In SOLIDWORKS, click Tools > C# Add-in > CreateCube.
// 2. Click Dynamic Flyout in the CommandManager and click FlyoutCommand 2.
// 3. Inspect the Immediate window.
// 4. Click a face of the cube.
// 5. Click the flyout button in the face's context-sensitive menu and
//    click FlyoutCommand 1.
// 6. Inspect the Immediate window.
//---------------------------------------------------------------------------

//SwAddin

using System;
using System.Runtime.InteropServices;
using System.Collections;
using System.Reflection;

using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swpublished;
using SolidWorks.Interop.swconst;
using SolidWorksTools;
using SolidWorksTools.File;
using System.Collections.Generic;
using System.Diagnostics;

namespace FlyoutAddin
{
    /// <summary>
    /// This C# add-in shows how to create a flyout menu in both the CommandManager
    /// and the context-sensitive menus of selected faces.
    /// </summary>
    [Guid("cc6bb106-bf87-49e0-b0fb-dcb49eab0bbe"), ComVisible(true)]
    [SwAddin(
        Description = "A flyout menu appears on the toolbar and on the context-sensitive menus of selected faces.",
        Title = "C# Add-in",
        LoadAtStartup = true
        )]
    public class SwAddin : ISwAddin
    {
        #region Local Variables
        ISldWorks iSwApp = null;
        ICommandManager iCmdMgr = null;
        ICommandGroup cmdGroup;
        IFlyoutGroup flyoutGroup;
        int addinID = 0;
        BitmapHandler iBmp;

        public const int mainCmdGroupID = 5;
        public const int mainItemID1 = 0;
        public const int mainItemID2 = 1;
        public const int mainItemID3 = 2;
        public const int flyoutGroupID = 91;

        string[] mainIcons = new string[3];
        string[] icons = new string[3];

        #region Event Handler Variables
        Hashtable openDocs = new Hashtable();
        SolidWorks.Interop.sldworks.SldWorks SwEventPtr = null;
        #endregion

        #region Property Manager Variables
        UserPMPage ppage = null;
        #endregion

        // Public Properties
        public ISldWorks SwApp
        {
            get { return iSwApp; }
        }
        public ICommandManager CmdMgr
        {
            get { return iCmdMgr; }
        }

        public Hashtable OpenDocs
        {
            get { return openDocs; }
        }

        #endregion

        #region SOLIDWORKS Registration
        [ComRegisterFunctionAttribute]
        public static void RegisterFunction(Type t)
        {
            #region Get Custom Attribute: SwAddinAttribute
            SwAddinAttribute SWattr = null;
            Type type = typeof(SwAddin);

            foreach (System.Attribute attr in type.GetCustomAttributes(false))
            {
                if (attr is SwAddinAttribute)
                {
                    SWattr = attr as SwAddinAttribute;
                    break;
                }
            }

            #endregion

            try
            {
                Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
                Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

                string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
                Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);
                addinkey.SetValue(null, 0);

                addinkey.SetValue("Description", SWattr.Description);
                addinkey.SetValue("Title", SWattr.Title);

                keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
                addinkey = hkcu.CreateSubKey(keyname);
                addinkey.SetValue(null, Convert.ToInt32(SWattr.LoadAtStartup), Microsoft.Win32.RegistryValueKind.DWord);
            }
            catch (System.NullReferenceException nl)
            {
                Console.WriteLine("There was a problem registering this dll: SWattr is null. \n\"" + nl.Message + "\"");
                System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: SWattr is null.\n\"" + nl.Message + "\"");
            }

            catch (System.Exception e)
            {
                Console.WriteLine(e.Message);

                System.Windows.Forms.MessageBox.Show("There was a problem registering the function: \n\"" + e.Message + "\"");
            }
        }

        [ComUnregisterFunctionAttribute]
        public static void UnregisterFunction(Type t)
        {
            try
            {
                Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
                Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

                string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
                hklm.DeleteSubKey(keyname);

                keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
                hkcu.DeleteSubKey(keyname);
            }
            catch (System.NullReferenceException nl)
            {
                Console.WriteLine("There was a problem unregistering this dll: " + nl.Message);
                System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: \n\"" + nl.Message + "\"");
            }
            catch (System.Exception e)
            {
                Console.WriteLine("There was a problem unregistering this dll: " + e.Message);
                System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: \n\"" + e.Message + "\"");
            }
        }

        #endregion

        #region ISwAddin Implementation
        public SwAddin()
        {
        }

        public bool ConnectToSW(object ThisSW, int cookie)
        {
            iSwApp = (ISldWorks)ThisSW;
            addinID = cookie;

            //Set up callbacks
            iSwApp.SetAddinCallbackInfo2(0, this, addinID);

            #region Set up the CommandManager
            iCmdMgr = iSwApp.GetCommandManager(cookie);
            AddCommandMgr();
            #endregion

            #region Set up the Event Handlers
            SwEventPtr = (SolidWorks.Interop.sldworks.SldWorks)iSwApp;
            openDocs = new Hashtable();
            AttachEventHandlers();
            #endregion

            #region Set up PropertyManager page
            AddPMP();
            #endregion

            return true;
        }

        public bool DisconnectFromSW()
        {
            RemoveCommandMgr();
            RemovePMP();
            DetachEventHandlers();

            System.Runtime.InteropServices.Marshal.ReleaseComObject(iCmdMgr);
            iCmdMgr = null;
            System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp);
            iSwApp = null;
            // The add-in must call GC.Collect() here in order to retrieve all managed code pointers
            GC.Collect();
            GC.WaitForPendingFinalizers();

            GC.Collect();
            GC.WaitForPendingFinalizers();

            return true;
        }
        #endregion

        #region UI Methods
        public void updateBtns()
        {

            flyoutGroup = iCmdMgr.GetFlyoutGroup(91);

            flyoutGroup.RemoveAllCommandItems();

            flyoutGroup.AddCommandItem("FlyoutCommand 1", "FlyoutCommand 1", 0, "FlyoutCommandItem1", "FlyoutEnableCommandItem1");
            flyoutGroup.AddCommandItem("FlyoutCommand 2", "FlyoutCommand 2", 0, "FlyoutCommandItem2", "FlyoutEnableCommandItem2");

            flyoutGroup.FlyoutType = (int)swCommandFlyoutStyle_e.swCommandFlyoutStyle_Simple;

            IFlyoutGroup fogrp;
            fogrp = iCmdMgr.GetFlyoutGroup(91);
            Debug.Print("  CmdID: " + fogrp.CmdID);
            Debug.Print("  Button count: " + fogrp.ButtonCount);
            Debug.Print("  Flyout type: " + fogrp.FlyoutType);
            mainIcons = (string[])fogrp.MainIconList;
            Debug.Print("  Small button: " + mainIcons[0]);
            Debug.Print("  Medium button: " + mainIcons[1]);
            Debug.Print("  Large button: " + mainIcons[1]);
            icons = (string[])fogrp.IconList;
            Debug.Print("  Small toolbar button: " + icons[0]);
            Debug.Print("  Medium toolbar button: " + icons[2]);
            Debug.Print("  Large toolbar button: " + icons[2]);

        }
        public void AddCommandMgr()
        {

            if (iBmp == null)
                iBmp = new BitmapHandler();
            Assembly thisAssembly;
            int cmdIndex0, cmdIndex1;
            string Title = "C# Add-in", ToolTip = "Flyout demo";

            int[] docTypes = new int[]{(int)swDocumentTypes_e.swDocASSEMBLY,
                                       (int)swDocumentTypes_e.swDocDRAWING,
                                       (int)swDocumentTypes_e.swDocPART};

            thisAssembly = System.Reflection.Assembly.GetAssembly(this.GetType());

            int cmdGroupErr = 0;
            bool ignorePrevious = false;

            object registryIDs;
            // Get the ID information stored in the registry
            bool getDataResult = iCmdMgr.GetGroupDataFromRegistry(mainCmdGroupID, out registryIDs);

            int[] knownIDs = new int[2] { mainItemID1, mainItemID2 };

            if (getDataResult)
            {
                if (!CompareIDs((int[])registryIDs, knownIDs)) // If the IDs don't match, reset the CommandGroup
                {
                    ignorePrevious = true;
                }
            }
```

```
  int smallImage = 0;
  int mediumImage = 0;
  int largeImage = 0;
  int imageSizeToUse = 0;

  imageSizeToUse = SwApp.GetImageSize(out smallImage, out mediumImage, out largeImage);

  Debug.Print("Image sizes:");
  Debug.Print("  Default PropertyManager page and menu image size based on DPI setting: " + imageSizeToUse);
  Debug.Print("    Small image size based on DPI setting: " + smallImage);
  Debug.Print("    Medium image size based on DPI setting: " + mediumImage);
  Debug.Print("    Large image size based on DPI setting: " + largeImage);
```

```
            cmdGroup = iCmdMgr.CreateCommandGroup2(mainCmdGroupID, Title, ToolTip, "", -1, ignorePrevious, ref cmdGroupErr);

            icons[0] = "Pathname_to_toolbar_nxn_image";
            icons[1] = "Pathname_to_toolbar_nnxnn_image";
            icons[2] = "Pathname_to_toolbar_nnnxnnn_image";
            mainIcons[0] = "Pathname_to_nxn_image";
            mainIcons[1] = "Pathname_to_nnxnn_image";
            mainIcons[2] = "Pathname_to_nnnxnnn_image";

            cmdGroup.IconList = icons;
            cmdGroup.MainIconList = mainIcons;

            int menuToolbarOption = (int)(swCommandItemType_e.swMenuItem | swCommandItemType_e.swToolbarItem);
            cmdIndex0 = cmdGroup.AddCommandItem2("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", mainItemID1, menuToolbarOption);
            cmdIndex1 = cmdGroup.AddCommandItem2("Show PMP", -1, "Display sample property manager", "Show PMP", 2, "ShowPMP", "EnablePMP", mainItemID2, menuToolbarOption);

            cmdGroup.HasToolbar = true;
            cmdGroup.HasMenu = true;
            cmdGroup.Activate();

            bool bResult;

            flyoutGroup = iCmdMgr.CreateFlyoutGroup2(flyoutGroupID, "Dynamic Flyout", "Dynamic Flyout", "Flyout Hint",
              mainIcons, icons, "FlyoutCallback", "FlyoutEnable");

            // Add the FlyoutGroup to the context-sensitive menus of faces in parts
            bResult = flyoutGroup.AddContextMenuFlyout((int)swDocumentTypes_e.swDocPART, (int)swSelectType_e.swSelFACES);
            Debug.Print("Context-sensitive menu flyout created for faces in parts: " + bResult.ToString());

            // Get the total number of FlyoutGroups in CommandManager
            Debug.Print("Number of FlyoutGroups is " + iCmdMgr.NumberOfFlyoutGroups);

            // Get the FlyoutGroups
            object[] objGroups;
            objGroups = (object[])iCmdMgr.GetFlyoutGroups();
            Debug.Print("Find all FlyoutGroups in CommandManager:");
            int i;
            for (i = 0; i <= objGroups.GetUpperBound(0); i++)
            {
                Debug.Print("FlyoutGroup found");

            }

            // Get a FlyoutGroup by its user-defined ID
            IFlyoutGroup fogrp;
            fogrp = iCmdMgr.GetFlyoutGroup(91);
            Debug.Print("  CmdID: " + fogrp.CmdID);
            Debug.Print("  Button count: " + fogrp.ButtonCount);
            Debug.Print("  Flyout Type: " + fogrp.FlyoutType);
            mainIcons = (string[])fogrp.MainIconList;
            Debug.Print("  Small button: " + mainIcons[0]);
            Debug.Print("  Medium button: " + mainIcons[1]);
            Debug.Print("  Large button: " + mainIcons[2]);
            icons = (string[])fogrp.IconList;
            Debug.Print("  Small toolbar button: " + icons[0]);
            Debug.Print("  Medium toolbar button: " + icons[1]);
            Debug.Print("  Large toolbar button: " + icons[2]);

            foreach (int type in docTypes)
            {
                CommandTab cmdTab;

                cmdTab = iCmdMgr.GetCommandTab(type, Title);

                if (cmdTab != null && !getDataResult || ignorePrevious)// If tab exists, but we have ignored the registry info (or changed CommandGroup ID), re-create the tab; otherwise the ids won't match and the tab will be blank
                {
                    bool res = iCmdMgr.RemoveCommandTab(cmdTab);
                    cmdTab = null;
                }

                // If cmdTab is null, must be first load (possibly after reset), add the commands to the tabs
                if (cmdTab == null)
                {
                    cmdTab = iCmdMgr.AddCommandTab(type, Title);

                    CommandTabBox cmdBox = cmdTab.AddCommandTabBox();

                    int[] cmdIDs = new int[3];
                    int[] TextType = new int[3];

                    cmdIDs[0] = cmdGroup.get_CommandID(cmdIndex0);

                    TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                    cmdIDs[1] = cmdGroup.get_CommandID(cmdIndex1);

                    TextType[1] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                    cmdIDs[2] = cmdGroup.ToolbarId;

                    TextType[2] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal | (int)swCommandTabButtonFlyoutStyle_e.swCommandTabButton_ActionFlyout;

                    bResult = cmdBox.AddCommands(cmdIDs, TextType);

                    CommandTabBox cmdBox1 = cmdTab.AddCommandTabBox();
                    cmdIDs = new int[1];
                    TextType = new int[1];

                    cmdIDs[0] = flyoutGroup.CmdID;
                    TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow | (int)swCommandTabButtonFlyoutStyle_e.swCommandTabButton_ActionFlyout;

                    bResult = cmdBox1.AddCommands(cmdIDs, TextType);

                    cmdTab.AddSeparator(cmdBox1, cmdIDs[0]);

                }

            }
            thisAssembly = null;

        }

        public void RemoveCommandMgr()
        {
            iBmp.Dispose();

            iCmdMgr.RemoveCommandGroup(mainCmdGroupID);
            iCmdMgr.RemoveFlyoutGroup(flyoutGroupID);
        }

        public bool CompareIDs(int[] storedIDs, int[] addinIDs)
        {
            List<int> storedList = new List<int>(storedIDs);
            List<int> addinList = new List<int>(addinIDs);

            addinList.Sort();
            storedList.Sort();

            if (addinList.Count != storedList.Count)
            {
                return false;
            }
            else
            {

                for (int i = 0; i < addinList.Count; i++)
                {
                    if (addinList[i] != storedList[i])
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        public Boolean AddPMP()
        {
            ppage = new UserPMPage(this);
            return true;
        }

        public Boolean RemovePMP()
        {
            ppage = null;
            return true;
        }

        #endregion

        #region UI Callbacks
        public void CreateCube()
        {
            // Make sure a part open is open
            string partTemplate = iSwApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);
            if ((partTemplate != null) && (partTemplate != ""))
            {
                IModelDoc2 modDoc = (IModelDoc2)iSwApp.NewDocument(partTemplate, (int)swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0);
                ISketchManager sketchMgr = modDoc.SketchManager;
                sketchMgr.InsertSketch(true);
                sketchMgr.CreateCornerRectangle(0, 0, 0, .1, .1, .1);
                // Extrude the sketch
                IFeatureManager featMan = modDoc.FeatureManager;
                featMan.FeatureExtrusion3(true,
                    false, false,
                    (int)swEndConditions_e.swEndCondBlind, (int)swEndConditions_e.swEndCondBlind,
                    0.1, 0.0,
                    false, false,
                    false, false,
                    0.0, 0.0,
                    false, false,
                    false, false,
                    false,
                    false, true, (int)swStartConditions_e.swStartSketchPlane, 0.0, false);
            }
            else
            {
                System.Windows.Forms.MessageBox.Show("There is no part template available. Please check your options and make sure there is a part template selected, or select a new part template.");
            }
        }

        public void ShowPMP()
        {
            if (ppage != null)
                ppage.Show();
        }

        public int EnablePMP()
        {
            if (iSwApp.ActiveDoc != null)
                return 1;
            else
                return 0;
        }

        public void FlyoutCallback()
        {
            updateBtns();
        }
        public int FlyoutEnable()
        {
            // Enable the flyout only if CommandGroup buttons are enabled
            if (cmdGroup.HasEnabledButton)
                return 1;
            else
                return 0;
        }

        public void FlyoutCommandItem1() { Debug.Print("Flyout command 1 called"); }

        public int FlyoutEnableCommandItem1() { return 1; }

        public void FlyoutCommandItem2() { Debug.Print("Flyout command 2 called"); }

        public int FlyoutEnableCommandItem2() { return 1; }

        #endregion

        #region Event Methods
        public bool AttachEventHandlers()
        {
            AttachSwEvents();
            // Listen for events on all currently open docs
            AttachEventsToAllDocuments();
            return true;
        }

        private bool AttachSwEvents()
        {
            try
            {
                SwEventPtr.ActiveDocChangeNotify += new DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);
                SwEventPtr.DocumentLoadNotify2 += new DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);
                SwEventPtr.FileNewNotify2 += new DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);
                SwEventPtr.ActiveModelDocChangeNotify += new DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);
                SwEventPtr.FileOpenPostNotify += new DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
                return true;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }
        }

        private bool DetachSwEvents()
        {
            try
            {
                SwEventPtr.ActiveDocChangeNotify -= new DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);
                SwEventPtr.DocumentLoadNotify2 -= new DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);
                SwEventPtr.FileNewNotify2 -= new DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);
                SwEventPtr.ActiveModelDocChangeNotify -= new DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);
                SwEventPtr.FileOpenPostNotify -= new DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
                return true;
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return false;
            }

        }

        public void AttachEventsToAllDocuments()
        {
            ModelDoc2 modDoc = (ModelDoc2)iSwApp.GetFirstDocument();
            while (modDoc != null)
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
                return false;

            DocumentEventHandler docHandler = null;

            if (!openDocs.Contains(modDoc))
            {
                switch (modDoc.GetType())
                {
                    case (int)swDocumentTypes_e.swDocPART:
                        {
                            docHandler = new PartEventHandler(modDoc, this);
                            break;
                        }
                    case (int)swDocumentTypes_e.swDocASSEMBLY:
                        {
                            docHandler = new AssemblyEventHandler(modDoc, this);
                            break;
                        }
                    case (int)swDocumentTypes_e.swDocDRAWING:
                        {
                            docHandler = new DrawingEventHandler(modDoc, this);
                            break;
                        }
                    default:
                        {
                            return false; // Unsupported document type
                        }
                }
                docHandler.AttachEventHandlers();
                openDocs.Add(modDoc, docHandler);
            }
            return true;
        }

        public bool DetachModelEventHandler(ModelDoc2 modDoc)
        {
            DocumentEventHandler docHandler;
            docHandler = (DocumentEventHandler)openDocs[modDoc];
            openDocs.Remove(modDoc);
            modDoc = null;
            docHandler = null;
            return true;
        }

        public bool DetachEventHandlers()
        {
            DetachSwEvents();

            // Close events on all currently open docs
            DocumentEventHandler docHandler;
            int numKeys = openDocs.Count;
            object[] keys = new Object[numKeys];

            // Remove all document event handlers
            openDocs.Keys.CopyTo(keys, 0);
            foreach (ModelDoc2 key in keys)
            {
                docHandler = (DocumentEventHandler)openDocs[key];
                docHandler.DetachEventHandlers(); // This also removes the pair from the hash
                docHandler = null;
            }
            return true;
        }
        #endregion

        #region Event Handlers
        // Events
        public int OnDocChange()
        {
            return 0;
        }

        public int OnDocLoad(string docTitle, string docPath)
        {
            return 0;
        }

        int FileOpenPostNotify(string FileName)
        {
            AttachEventsToAllDocuments();
            return 0;
        }

        public int OnFileNew(object newDoc, int docType, string templateName)
        {
            AttachEventsToAllDocuments();
            return 0;
        }

        public int OnModelChange()
        {
            return 0;
        }

        #endregion
    }

}
```
