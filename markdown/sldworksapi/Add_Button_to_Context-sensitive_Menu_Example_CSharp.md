---
title: "Add Button to Context-sensitive Menu Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_Button_to_Context-sensitive_Menu_Example_CSharp.htm"
---

# Add Button to Context-sensitive Menu Example (C#)

This example shows how to add:

- button to a face's context-sensitive menu in a part.
- shortcut menu for that button.

```
//---------------------------------------------------------------------------
// Preconditions:
// 1. Verify that the SOLIDWORKS API SDK add-in templates for your version
//    of Microsoft Visual Studio are installed.
// 2. In Microsoft Visual Studio, create a C# project using the
//    SwCSharpAddin template.
// 3. Name the project AddMenuPopupIconCSharp.
// 4. Copy and paste SwAddin into SwAddin.cs of your project.
// 5. Click Project > AddMenuPopupIconCSharp Properties > Debug.
// 6. Select Start external program and type the pathname to your
//    SOLIDWORKS Design executable.
// 7. Replace the text shown for the imageList array elements
//    and smallMainIcon with the pathnames to your image files.
// 8. Press F5 to start debugging this add-in.
//
// Postconditions:
// 1. In SOLIDWORKS Design, open a part.
// 2. Right-click a face of the part.
// 3. Note the size of the button added by this add-in to the
//    context-sensitive menu.
// 4. Click the button added by this add-in to display the shortcut menu.
// 5. Exit SOLIDWORKS Design.
// 6. Change the size of the text and other items on your computer.
//    For example, in Windows 7:
//    a. Click Start > Control Panel > Appearance and
//       Personalization > Display.
//    b. Select a different size.
//    c. Click Apply.
//    d. Click Log off now.
//    e. Log back in.
// 7. Start SOLIDWORKS Design.
// 8. Repeat steps 1 - 3.
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

namespace AddMenuPopupCSharp
{
    /// <summary>
    /// Summary description for AddMenuPopupCSharp.
    /// </summary>
    [Guid("7d3de7ec-7f66-4827-af80-1411b18c7dfa"), ComVisible(true)]
    [SwAddin(
        Description = "AddMenuPopupCSharp description",
        Title = "AddMenuPopupCSharp",
        LoadAtStartup = true
        )]
    public class SwAddin : ISwAddin
    {
        #region Local Variables
        SldWorks iSwApp;
        int addinID;
        BitmapHandler iBmp;
        ModelDoc2 model;
        IFrame frame;
        bool resultCode;
        int registerID;

        #region Event Handler Variables
        Hashtable openDocs = new Hashtable();
        SolidWorks.Interop.sldworks.SldWorks SwEventPtr = null;
        #endregion

        // Public Properties
        public ISldWorks SwApp
        {
            get { return iSwApp; }
        }

        public Hashtable OpenDocs
        {
            get { return openDocs; }
        }

        #endregion

        #region SolidWorks Registration
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

                string keyname = "SOFTWARE\\SolidWorks\\Addins\\{" + t.GUID.ToString() + "}";
                Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);
                addinkey.SetValue(null, 0);

                addinkey.SetValue("Description", SWattr.Description);
                addinkey.SetValue("Title", SWattr.Title);

                keyname = "Software\\SolidWorks\\AddInsStartup\\{" + t.GUID.ToString() + "}";
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

                string keyname = "SOFTWARE\\SolidWorks\\Addins\\{" + t.GUID.ToString() + "}";
                hklm.DeleteSubKey(keyname);

                keyname = "Software\\SolidWorks\\AddInsStartup\\{" + t.GUID.ToString() + "}";
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
            iSwApp = (SldWorks)ThisSW;
            addinID = cookie;

            //Set up callbacks
            iSwApp.SetAddinCallbackInfo2(0, this, addinID);

            #region Set up third-party buttons
            AddThirdPartyIcon();
            #endregion

            #region Set up the Event Handlers
            SwEventPtr = (SldWorks)iSwApp;
            openDocs = new Hashtable();
            AttachEventHandlers();
            #endregion

            return true;
        }

        public bool DisconnectFromSW()
        {
            DetachEventHandlers();

            System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp);
            iSwApp = null;
            //The add-in must call GC.Collect() here to retrieve all managed code pointers
            GC.Collect();
            GC.WaitForPendingFinalizers();

            GC.Collect();
            GC.WaitForPendingFinalizers();

            return true;
        }
        #endregion

        #region UI Methods
 	    public void AddThirdPartyIcon()
	    {

		    BitmapHandler iBmp = new BitmapHandler();
		    Assembly thisAssembly1 = default(Assembly);

            	    thisAssembly1 = System.Reflection.Assembly.GetAssembly(this.GetType());

		    // Create a button in the context-sensitive menus of faces in parts
		    frame = SwApp.Frame();
		    string[] imageList = new string[3];
		    imageList[0] = "Pathname_to_button_nxn_image";
		    imageList[1] = "Pathname_to_button_nnxnn_image";
		    imageList[2] = "Pathname_to_button_nnnxnnn_image";
		    resultCode = frame.AddMenuPopupIcon3((int)swDocumentTypes_e.swDocPART, (int)swSelectType_e.swSelFACES, "Third-party context-sensitive", addinID, "CSCallbackFunction", "CSEnable", "", imageList);

		    // Create and register the shortcut menu
		    registerID = SwApp.RegisterThirdPartyPopupMenu();
		    // Add a menu break at the top of the shortcut menu
		    resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, Convert.ToInt32(swDocumentTypes_e.swDocPART), "Menu Break", addinID, "", "", "", "", "", Convert.ToInt32(swMenuItemType_e.swMenuItemType_Break));
		    // Add a couple of items to the shortcut menu
		    string smallMainIcon = null;
		    smallMainIcon = "Pathname_to_shortcut_button_image";
		    resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, Convert.ToInt32(swDocumentTypes_e.swDocPART), "Test1", addinID, "TestCallback", "EnableTest", "", "Test1", smallMainIcon, Convert.ToInt32(swMenuItemType_e.swMenuItemType_Default));
		    resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, Convert.ToInt32(swDocumentTypes_e.swDocPART), "Test4", addinID, "TestCallback", "EnableTest", "", "Test4", smallMainIcon, Convert.ToInt32(swMenuItemType_e.swMenuItemType_Default));
		    // Add a separator bar to the shortcut menu
		    resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, Convert.ToInt32(swDocumentTypes_e.swDocPART), "separator", addinID, "", "", "", "", "", Convert.ToInt32(swMenuItemType_e.swMenuItemType_Separator));
		    // Add another item to the shortcut menu
		    resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, Convert.ToInt32(swDocumentTypes_e.swDocPART), "Test5", addinID, "TestCallback", "EnableTest", "", "Test5", smallMainIcon, Convert.ToInt32(swMenuItemType_e.swMenuItemType_Default));
		    // Add a button to a menu bar of the shortcut menu
		    resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, Convert.ToInt32(swDocumentTypes_e.swDocPART), "", addinID, "TestCallback", "EnableTest", "", "NoOp", smallMainIcon, Convert.ToInt32(swMenuItemType_e.swMenuItemType_Default));

		    thisAssembly1 = null;
		    iBmp.Dispose();

        }
        #endregion

        #region Event Methods
        public bool AttachEventHandlers()
        {
            AttachSwEvents();
            //Listen for events on all currently open documents
            AttachEventsToAllDocuments();
            return true;
        }

        private bool AttachSwEvents()
        {
            try
            {
                SwEventPtr.ActiveDocChangeNotify += new DSldWorksEvents_ActiveDocChangeNotifyEventHandler(ActiveDocChangeNotify);
                SwEventPtr.DocumentLoadNotify2 += new DSldWorksEvents_DocumentLoadNotify2EventHandler(DocumentLoadNotify2);
                SwEventPtr.FileNewNotify2 += new DSldWorksEvents_FileNewNotify2EventHandler(FileNewNotify2);
                SwEventPtr.ActiveModelDocChangeNotify += new DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(ActiveModelDocChangeNotify);
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
                SwEventPtr.ActiveDocChangeNotify -= new DSldWorksEvents_ActiveDocChangeNotifyEventHandler(ActiveDocChangeNotify);
                SwEventPtr.DocumentLoadNotify2 -= new DSldWorksEvents_DocumentLoadNotify2EventHandler(DocumentLoadNotify2);
                SwEventPtr.FileNewNotify2 -= new DSldWorksEvents_FileNewNotify2EventHandler(FileNewNotify2);
                SwEventPtr.ActiveModelDocChangeNotify -= new DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(ActiveModelDocChangeNotify);
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
                else if (openDocs.Contains(modDoc))
                {
                    bool connected = false;
                    DocumentEventHandler docHandler = (DocumentEventHandler)openDocs[modDoc];
                    if (docHandler != null)
                    {
                        connected = docHandler.ConnectModelViews();
                    }
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
                            //Unsupported document type
                            return false;
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

            // Close events on all currently open documents
            DocumentEventHandler docHandler;
            int numKeys = openDocs.Count;
            object[] keys = new Object[numKeys];

            // Remove all document event handlers
            openDocs.Keys.CopyTo(keys, 0);
            foreach (ModelDoc2 key in keys)
            {
                docHandler = (DocumentEventHandler)openDocs[key];
                //Remove the pair from the hash
                docHandler.DetachEventHandlers();
                docHandler = null;
            }
            return true;
        }
        #endregion

        #region Event Handlers
        // Events
        public int ActiveDocChangeNotify()
        {
            return 0;
        }

        public int DocumentLoadNotify2(string docTitle, string docPath)
        {
            return 0;
        }

        public int FileOpenPostNotify(string FileName)
        {
            AttachEventsToAllDocuments();
            return 0;
        }

        public int FileNewNotify2(object newDoc, int docType, string templateName)
        {
            AttachEventsToAllDocuments();
            return 0;
        }

        public int ActiveModelDocChangeNotify()
        {
            return 0;
        }

        #endregion
        #region " UI Callbacks"
        public void CSCallbackFunction()
        {
            resultCode = SwApp.ShowThirdPartyPopupMenu(registerID, 500, 500);
        }

        public int CSEnable()
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
