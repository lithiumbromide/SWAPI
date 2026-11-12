---
title: "Add and Remove Items to File Save As and Open Menus Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_CSharp.htm"
---

# Add and Remove Items to File Save As and Open Menus Example (C#)

This example shows how to add items to the **File > Save As** and **File > Open** file type menus.

```vb
 //---------------------------------------------------------------------------
 // Preconditions:
 // 1. In Microsoft Visual Studio 2010, or later, create an SOLIDWORKS add-in
 //    project using Visual C# > SwCSharpAddin.
 // 2. Name the project SwCSharpAddin1.
 // 3. Copy and paste this code into SwAddin.cs of your C# project.
 // 4. Click Project > SwCSharpAddin1 Properties > Debug.
 // 5. Select Start external program and type the path to  sldworks.exe. Include
 //    sldworks.exe in the path.
 // 6. Press F5 to start debugging SOLIDWORKS Design with this add-in.
 //
 // Postconditions:
 // 1. Open a part.
 // 2. Click File > Save As.
 // 3. Select XXX file (*.xxx) in Save as type.
 // 4. Click Save.
 // 5. Displays the path and file name to which to save the part.
 // 6. Click OK to close the message box.
 //-----------------------------------------------------------------------------
// SwAddin.cs:
```

```vb
using System;
 using System.Runtime.InteropServices;
 using System.Collections;
 using System.Reflection;

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swpublished;
 using SolidWorks.Interop.swconst;
 using SolidWorksTools;
 using SolidWorksTools.File;
using System.Windows.Forms;

 namespace SwCSharpAddin1
 {
     /// <summary>
     /// Create third-party pop-up menus.
     /// </summary>
     [Guid("144d6667-43ec-4733-ae26-867c9aa63fe6"), ComVisible(true)]
     [SwAddin(
         Description = "SwCSharpAddin1 description",
         Title = "SwCSharpAddin1",
         LoadAtStartup = true
         )]
     public class SwAddin : ISwAddin
     {
         #region Local Variables
         ISldWorks iSwApp;
         ICommandManager iCmdMgr;
         int addinID;
         int registerID;
         bool resultCode;
         IModelDoc2 model;
         IFrame frame;

         #region Event Handler Variables
         Hashtable openDocs;
         SolidWorks.Interop.sldworks.SldWorks SwEventPtr;
         #endregion

         #region Property Manager Variables
         UserPMPage ppage;
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

             Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
             Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

             string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
             Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);
             addinkey.SetValue(null, 0);

             addinkey.SetValue("Description", SWattr.Description);
             addinkey.SetValue("Title", SWattr.Title);

             keyname =  "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
             addinkey = hkcu.CreateSubKey(keyname);
             addinkey.SetValue(null, Convert.ToInt32(SWattr.LoadAtStartup), Microsoft.Win32.RegistryValueKind.DWord);
         }

         [ComUnregisterFunctionAttribute]
         public static void UnregisterFunction(Type t)
         {
             Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;
             Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

             string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";
             hklm.DeleteSubKey(keyname);

             keyname =  "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";
             hkcu.DeleteSubKey(keyname);
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
             iSwApp.SetAddinCallbackInfo(0, this, addinID);

             //Set up File > Save As > Save as type item and File > Open > File name type item
             bRet = iSwApp.AddFileSaveAsItem2(addinID, "XXX_FileSave", "XXX file (*.xxx)", "xxx", (int)swDocumentTypes_e.swDocPART);
             bRet = iSwApp.AddFileOpenItem3(addinID, "XXX_FileOpen", "XXX file (*.xxx)", "xxx", "", "");

             #region Setup the Command Manager
             iCmdMgr = iSwApp.GetCommandManager(cookie);
             AddCommandMgr();
             #endregion

             #region Setup the Event Handlers
             SwEventPtr = (SolidWorks.Interop.sldworks.SldWorks)iSwApp;
             openDocs = new Hashtable();
             AttachEventHandlers();
             #endregion

             #region Setup Sample Property Manager
             AddPMP();
             #endregion

             return true;
         }

         public bool DisconnectFromSW()
         {
            bRet = iSwApp.RemoveFileSaveAsItem2(addinID, "XXX_FileSave", "XXX file (*.xxx)", "xxx", (int)swDocumentTypes_e.swDocPART);
             bRet = iSwApp.RemoveFileOpenItem2(addinID, "XXX_FileOpen", "XXX file (*.xxx)", "xxx");

             RemoveCommandMgr();
             RemovePMP();
             DetachEventHandlers();

             iSwApp = null;
             //The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
             GC.Collect();
             return true;
         }
```

```vb
public void XXX_FileSave(string sFileName)
 {
     // S_OK          =   Saved successfully
     // S_FALSE       =   Unsuccessful
     // !(SUCCEEDED)  =   Insuccessful

     int fileOp = 1;
     ParseFilename(sFileName, ref fileOp);

 }

 public void XXX_FileOpen(string sFileName)
 {
     // S_OK          =   Loaded successfully
     // S_FALSE       =   Unsuccessful
     // !(SUCCEEDED)  =   Unsuccessful
     int fileOp = 0;
     ParseFilename(sFileName, ref fileOp);

 }

 public void ParseFilename(string sFileName, ref int fileOp)
 {
     string strExtension = null;
     int lPos = 0;
     int lNumExtensionOccurrences = 0;
     int lStart = 0;
     string strSearchString = null;
     int lNumNonRealExtensions = 0;
     string strExtensionWithPeriod = null;

     // Set the extension for which to look
     strExtension = "xxx";
     strExtensionWithPeriod = "." + strExtension;

     // Strip the trailing 'w' or 'r' and any leading and trailing white space
     sFileName = (sFileName.Substring(0, sFileName.Length - 1)).Trim(' ');

     // Strip extension from the back
     sFileName = (sFileName.Substring(0, sFileName.Length - strExtension.Length)).Trim(' ');

     // Change to lowercase to make search case-insensitive
     strSearchString = sFileName.ToLower();

     lNumExtensionOccurrences = 0;

     lStart = 1;

     do
     {
         lPos = strSearchString.IndexOf(strExtensionWithPeriod.ToLower(), lStart - 1) + 1;
         if (lPos > 0)
         {
             lNumExtensionOccurrences = lNumExtensionOccurrences + 1;

             // Move start point of search
             lStart = (int)(lPos + strExtensionWithPeriod.Length);

         }

     } while (lPos > 0);

     // There is 1 real extension and n*2 non-real extension
     lNumNonRealExtensions = (lNumExtensionOccurrences / 2);

     // Start searching from the end to locate the real extension
     // Skip the number of non-real extensions, before reaching the real extension

     // Change to lowercase to make search case-insensitive
     strSearchString = sFileName.ToLower();

     lPos = strSearchString.LastIndexOf(strExtensionWithPeriod.ToLower(), lStart);

     sFileName = sFileName.Substring(0, lPos) + strExtensionWithPeriod;

     if (fileOp == 1)
     {
         MessageBox.Show("XXX_FileSave = " + sFileName);
     }
     else
     {
         MessageBox.Show("XXX_FileOpen = " + sFileName);
     }

 }
```

```vb
         #endregion

         #region UI Methods
         public void AddCommandMgr()
         {
             ICommandGroup cmdGroup;
             BitmapHandler iBmp = new BitmapHandler();
             Assembly thisAssembly;
             int cmdIndex0, cmdIndex1;
             string Title = "C# Add-in", ToolTip = "C# Add-in";

             int[] docTypes = new int[]{(int)swDocumentTypes_e.swDocASSEMBLY,
                                        (int)swDocumentTypes_e.swDocDRAWING,
                                        (int)swDocumentTypes_e.swDocPART};

             thisAssembly = System.Reflection.Assembly.GetAssembly(this.GetType());

             cmdGroup = iCmdMgr.CreateCommandGroup(1, Title, ToolTip, "", -1);
             cmdGroup.LargeIconList = iBmp.CreateFileFromResourceBitmap("SwCSharpAddin1.ToolbarLarge.bmp", thisAssembly);
             cmdGroup.SmallIconList = iBmp.CreateFileFromResourceBitmap("SwCSharpAddin1.ToolbarSmall.bmp", thisAssembly);
             cmdGroup.LargeMainIcon = iBmp.CreateFileFromResourceBitmap("SwCSharpAddin1.MainIconLarge.bmp", thisAssembly);
             cmdGroup.SmallMainIcon = iBmp.CreateFileFromResourceBitmap("SwCSharpAddin1.MainIconSmall.bmp", thisAssembly);

             cmdIndex0 = cmdGroup.AddCommandItem("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", 0);
             cmdIndex1 = cmdGroup.AddCommandItem("Show PMP", -1,  "Display sample property manager", "Show PMP", 2, "ShowPMP", "EnablePMP", 2);

             cmdGroup.HasToolbar =  true;
             cmdGroup.HasMenu = true;
             cmdGroup.Activate();

             bool bResult;

             foreach (int type in docTypes)
             {
                 ICommandTab cmdTab;

                 cmdTab = iCmdMgr.GetCommandTab(type, Title);

                 if (cmdTab == null)
                 {
                     cmdTab = (ICommandTab)iCmdMgr.AddCommandTab(type, Title);

                     CommandTabBox cmdBox = cmdTab.AddCommandTabBox();

                     int[] cmdIDs = new int[3];
                     int[] TextType = new int[3];

                     cmdIDs[0] = cmdGroup.get_CommandID(cmdIndex0);
                     System.Diagnostics.Debug.Print(cmdGroup.get_CommandID(cmdIndex0).ToString());
                     TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                     cmdIDs[1] = cmdGroup.get_CommandID(cmdIndex1);
                     System.Diagnostics.Debug.Print(cmdGroup.get_CommandID(cmdIndex1).ToString());
                     TextType[1] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal;

                     cmdIDs[2] = cmdGroup.ToolbarId;
                     System.Diagnostics.Debug.Print(cmdIDs[2].ToString());
                     TextType[2] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal | (int)swCommandTabButtonFlyoutStyle_e.swCommandTabButton_ActionFlyout;

                     bResult = cmdBox.AddCommands(cmdIDs, TextType);

                     CommandTabBox cmdBox1 = cmdTab.AddCommandTabBox();
                     cmdIDs = new int[1];
                     TextType = new int[1];

                     cmdIDs[0] = cmdGroup.ToolbarId;
                     TextType[0] = (int)swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow | (int)swCommandTabButtonFlyoutStyle_e.swCommandTabButton_ActionFlyout;

                     bResult = cmdBox1.AddCommands(cmdIDs, TextType);

                     cmdTab.AddSeparator(cmdBox1, cmdGroup.ToolbarId);

                 }

             }
             // create a third-party icon in the context-sensitive menus of faces in parts
             frame = (IFrame)SwApp.Frame();
             resultCode = frame.AddMenuPopupIcon2((int)swDocumentTypes_e.swDocPART, (int)swSelectType_e.swSelFACES, "contextsensitive", addinID, "CSCallbackFunction", "CSEnable", "", cmdGroup.SmallMainIcon);

             // create and register the third party menu
             registerID = SwApp.RegisterThirdPartyPopupMenu();

             // add a menu break at the top of the menu
             resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, (int)swDocumentTypes_e.swDocPART, "Menu Break", addinID, "", "", "", "", "", (int)swMenuItemType_e.swMenuItemType_Break
            );
             // add a couple of items to to the menu
             resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, (int)swDocumentTypes_e.swDocPART, "Test1", addinID, "TestCallback", "EnableTest", "", "Test1", cmdGroup.SmallMainIcon, (int)swMenuItemType_e.swMenuItemType_Default
            );
             resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, (int)swDocumentTypes_e.swDocPART, "Test4", addinID, "TestCallback", "EnableTest", "", "Test4", cmdGroup.SmallMainIcon, (int)swMenuItemType_e.swMenuItemType_Default
            );
             // add a separator bar to the menu
             resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, (int)swDocumentTypes_e.swDocPART, "", addinID, "", "", "", "", "", (int)swMenuItemType_e.swMenuItemType_Separator);
             resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, (int)swDocumentTypes_e.swDocPART, "Test5", addinID, "TestCallback", "EnableTest", "", "Test5", cmdGroup.SmallMainIcon, (int)swMenuItemType_e.swMenuItemType_Default
            );

             // add an icon to the menu bar
             resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, (int)swDocumentTypes_e.swDocPART, "", addinID, "TestCallback", "EnableTest", "", "NoOp", cmdGroup.SmallMainIcon, (int)swMenuItemType_e.swMenuItemType_Default
            );

             thisAssembly = null;
             iBmp.Dispose();
         }

         public void  RemoveCommandMgr()
         {
             iCmdMgr.RemoveCommandGroup(1);
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
             //make sure we have a part open
             string partTemplate = iSwApp.GetUserPreferenceStringValue((int)swUserPreferenceStringValue_e.swDefaultTemplatePart);
             IModelDoc2 modDoc = (IModelDoc2)iSwApp.NewDocument(partTemplate, (int)swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0);

             modDoc.InsertSketch2(true);
             modDoc.SketchRectangle(0, 0, 0, .1, .1, .1,  false);
             //Extrude the sketch
             IFeatureManager featMan = modDoc.FeatureManager;
             featMan.FeatureExtrusion(true,
                 false, false,
                 (int)swEndConditions_e.swEndCondBlind, (int)swEndConditions_e.swEndCondBlind,
                 0.1, 0.0,
                 false, false,
                 false, false,
                 0.0, 0.0,
                 false, false,
                 false, false,
                 true,
                 false, false);
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
         public void CSCallbackFunction()
         {
             resultCode = SwApp.ShowThirdPartyPopupMenu(registerID, 500, 500);
         }

         public int CSEnable()
         {
             if (iSwApp.ActiveDoc == null)
             {
                 return 0;
             }
             else
             {
                 return 1;
             }
         }

         public void TestCallback()
         {
             System.Diagnostics.Debug.Print("Test callback");
         }

         public int EnableTest()
         {
             if (iSwApp.ActiveDoc == null)
             {
                 return 0;
             }
             else
             {
                 return 1;
             }
         }

         #endregion

         #region Event Methods
         public bool AttachEventHandlers()
         {
             AttachSwEvents();
             //Listen for events on all currently open docs
             AttachEventsToAllDocuments();
             return true;
         }

         private bool AttachSwEvents()
         {
             try
             {
                 SwEventPtr.ActiveDocChangeNotify +=  new   DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);
                 SwEventPtr.DocumentLoadNotify2 +=  new  DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);
                 SwEventPtr.FileNewNotify2 +=  new  DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);
                 SwEventPtr.ActiveModelDocChangeNotify +=  new   DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);
                 SwEventPtr.FileOpenPostNotify +=  new  DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
                 SwEventPtr.InterfaceBrightnessThemeChangeNotify += new  DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler(InterfaceBrightnessThemeChangeNotify);

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
                 SwEventPtr.ActiveDocChangeNotify -=  new   DSldWorksEvents_ActiveDocChangeNotifyEventHandler(OnDocChange);
                 SwEventPtr.DocumentLoadNotify2 -=  new  DSldWorksEvents_DocumentLoadNotify2EventHandler(OnDocLoad);
                 SwEventPtr.FileNewNotify2 -=  new  DSldWorksEvents_FileNewNotify2EventHandler(OnFileNew);
                 SwEventPtr.ActiveModelDocChangeNotify -=  new   DSldWorksEvents_ActiveModelDocChangeNotifyEventHandler(OnModelChange);
                 SwEventPtr.FileOpenPostNotify -=  new  DSldWorksEvents_FileOpenPostNotifyEventHandler(FileOpenPostNotify);
                 SwEventPtr.InterfaceBrightnessThemeChangeNotify -= new  DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler(InterfaceBrightnessThemeChangeNotify);

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
                             docHandler =  new  PartEventHandler(modDoc,  this);
                             break;
                         }
                     case (int)swDocumentTypes_e.swDocASSEMBLY:
                         {
                             docHandler =  new  AssemblyEventHandler(modDoc,  this);
                             break;
                         }
                     case (int)swDocumentTypes_e.swDocDRAWING:
                         {
                             docHandler =  new  DrawingEventHandler(modDoc,  this);
                             break;
                         }
                     default:
                         {
                             return false; //Unsupported document type
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

             //Close events on all currently open docs
             DocumentEventHandler docHandler;
             int numKeys = openDocs.Count;
             object[] keys = new Object[numKeys];

             //Remove all document event handlers
             openDocs.Keys.CopyTo(keys, 0);
             foreach (ModelDoc2 key in keys)
             {
                 docHandler = (DocumentEventHandler)openDocs[key];
                 docHandler.DetachEventHandlers();  //This also removes the pair from the hash
                 docHandler =  null;
             }
             return true;
         }
         #endregion

         #region Event Handlers
         //Events
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

        public int InterfaceBrightnessThemeChangeNotify(int theme, ref object colors)
         {
             MessageBox.Show("Interface brightness theme changed to (0 = light, 1 = medium, 2 = dark): " + theme);
             int[] colorsArray = null;
             colorsArray = (int[])colors;
             MessageBox.Show("FeatureManager design tree color: " + colorsArray[0]);

             return 0;
         }

         #endregion
     }

 }
```
