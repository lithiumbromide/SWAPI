---
title: "Add and Remove Items to File Save As and Open Menus Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Add_and_Remove_Items_to_File_Save_As_and_Open_Menus_VBNET.htm"
---

# Add and Remove Items to File Save As and Open Menus Example (VB.NET)

This example shows how to add items to the **File > Save As** and **File > Open** file type menus.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. In Microsoft Visual Studio 2010, or later, create a SOLIDWORKS add-in
 '    project using Visual Basic > SwVBAddin.
 ' 2. Name the project SwVBAddin1.
 ' 3. Copy and paste this code into SwAddin.vb of your VB.NET project.
 ' 4. Select Project > SwVBAddin1 Properties > Debug.
 ' 5. Select Start external program and type the path to sldworks.exe. Include
 '    sldworks.exe in the path.
 ' 6. Press F5 to start debugging SOLIDWORKS Design with this add-in.
 '
 ' Postconditions:
 ' 1. Open a part.
 ' 2. Click File > Save As.
 ' 3. Select XXX file (*.xxx) in Save as type.
 ' 4. Click Save.
 ' 5. Displays the path and file name to which to save the part.
 ' 6. Click OK to close the message box.
 '----------------------------------------------------------------------------
' SwAddin.vb:
```

```vb
Imports System
 Imports System.Collections
 Imports System.Reflection
 Imports System.Runtime.InteropServices

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports SolidWorks.Interop.swpublished
 Imports SOLIDWORKSTools
 Imports SOLIDWORKSTools.File

 <Guid("a3ddcdce-c8a8-47c2-8561-919a24285286")> _
     <ComVisible(True)> _
     <SwAddin( _
         Description:="SwVBAddin1 third-party pop-up menus", _
         Title:="SwVBAddin1", _
         LoadAtStartup:=True _
         )> _
         Public Class SwAddin
     Implements SolidWorks.Interop.swpublished.SwAddin

 #Region "Local Variables"
     Dim WithEvents iSwApp As SldWorks
     Dim iCmdMgr As ICommandManager
     Dim addinID As Integer
     Dim openDocs As Hashtable
     Dim SwEventPtr As SldWorks
     Dim ppage As UserPMPage
     Dim registerID As Integer
     Dim resultCode As Boolean
     Dim model As ModelDoc2
     Dim frame As IFrame
     Dim cmdGroup As ICommandGroup

     ' Public Properties
     ReadOnly Property SwApp() As SldWorks
         Get
             Return iSwApp
         End Get
     End Property

     ReadOnly Property CmdMgr() As ICommandManager
         Get
             Return iCmdMgr
         End Get
     End Property

     ReadOnly Property OpenDocumentsTable() As Hashtable
         Get
             Return openDocs
         End Get
     End Property
 #End  Region

 #Region  "SOLIDWORKS Registration"

     <ComRegisterFunction()>  Public  Shared  Sub RegisterFunction(ByVal t As Type)

         ' Get Custom Attribute: SwAddinAttribute
         Dim attributes() As Object
         Dim SWattr As SwAddinAttribute = Nothing

         attributes = System.Attribute.GetCustomAttributes(GetType(SwAddin), GetType(SwAddinAttribute))

         If attributes.Length > 0 Then
             SWattr =  DirectCast(attributes(0), SwAddinAttribute)
         End If

         Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
         Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

         Dim keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString() + "}"
         Dim addinkey As Microsoft.Win32.RegistryKey = hklm.CreateSubKey(keyname)
         addinkey.SetValue(Nothing, 0)
         addinkey.SetValue("Description", SWattr.Description)
         addinkey.SetValue("Title", SWattr.Title)

         keyname = "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString() + "}"
         addinkey = hkcu.CreateSubKey(keyname)
         addinkey.SetValue(Nothing, SWattr.LoadAtStartup, Microsoft.Win32.RegistryValueKind.DWord)
     End Sub

     <ComUnregisterFunction()>  Public  Shared  Sub UnregisterFunction(ByVal t As Type)
         Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
         Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

         Dim keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString() + "}"
         hklm.DeleteSubKey(keyname)

         keyname = "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString() + "}"
         hkcu.DeleteSubKey(keyname)
     End Sub

 #End  Region

 #Region  "ISwAddin Implementation"

     Function ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Integer) As  Boolean  Implements SolidWorks.Interop.swpublished.SwAddin.ConnectToSW
         iSwApp = ThisSW
         addinID = Cookie

         ' Set up callbacks
         iSwApp.SetAddinCallbackInfo(0, Me, addinID
        'Set up File > Save As > Save as type item and File > Open > File name type item
         bRet = iSwApp.AddFileSaveAsItem2(addinID, "XXX_FileSave", "XXX file (*.xxx)", "xxx", swDocumentTypes_e.swDocPART)
         bRet = iSwApp.AddFileOpenItem3(addinID, "XXX_FileOpen", "XXX file (*.xxx)", "xxx", "", "")

         ' Set up the Command Manager
         iCmdMgr = iSwApp.GetCommandManager(Cookie)
         AddCommandMgr()

         'Set up the Event Handlers
         SwEventPtr = iSwApp
         openDocs = New Hashtable
         AttachEventHandlers()

         'Set up Sample Property Manager
         AddPMP()

         ConnectToSW = True
     End Function

     Function DisconnectFromSW() As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.DisconnectFromSW
        bRet = iSwApp.RemoveFileSaveAsItem2(addinID, "XXX_FileSave", "XXX file (*.xxx)", "xxx", swDocumentTypes_e.swDocPART)
         bRet = iSwApp.RemoveFileOpenItem2(addinID, "XXX_FileOpen", "XXX file (*.xxx)", "xxx")

         RemoveCommandMgr()
         RemovePMP()
         DetachEventHandlers()

         iSwApp = Nothing
         'The addin _must_ call GC.Collect() here in order to retrieve all managed code pointers
         GC.Collect()
         DisconnectFromSW = True
     End Function
```

```
    Public Sub XXX_FileSave(sFileName As String)
        ' S_OK          =   Saved successfully
        ' S_FALSE       =   Unsuccessful
        ' !(SUCCEEDED)  =   Insuccessful

        Dim fileOp As Integer = 1
        ParseFilename(sFileName, fileOp)

    End Sub

    Public Sub XXX_FileOpen(sFileName As String)
        ' S_OK          =   Loaded successfully
        ' S_FALSE       =   Unsuccessful
        ' !(SUCCEEDED)  =   Unsuccessful
        Dim fileOp As Integer = 0
        ParseFilename(sFileName, fileOp)

    End Sub

    Public Function ParseFilename(ByVal sFileName As String, ByRef fileOp As Integer) As String
        Dim tempParseFileName as String
        Dim strExtension As String
        Dim lPos As Integer
        Dim lNumExtensionOccurrences As Integer
        Dim lStart As Integer
        Dim strSearchString As String
        Dim lNumNonRealExtensions As Integer
        Dim strExtensionWithPeriod As String

        ' Set return value
        tempParseFilename = ""

        ' Set the extension for which to look
        strExtension = "xxx"
        strExtensionWithPeriod = "." & strExtension

        ' Strip the trailing 'w' or 'r' and any leading and trailing white space
        sFileName = Trim$(Left$(sFileName, Len(sFileName) - 1))

        ' Strip extension from the back
        sFileName = Trim$(Left$(sFileName, Len(sFileName) - Len(strExtension)))

        ' Change to lowercase to make search case-insensitive
        strSearchString = LCase$(sFileName)

        lNumExtensionOccurrences = 0

        lStart = 1

        Do

            lPos = InStr(lStart, strSearchString, LCase$(strExtensionWithPeriod))

            If (lPos > 0) Then

                lNumExtensionOccurrences = lNumExtensionOccurrences + 1

                ' Move start point of search
                lStart = lPos + Len(strExtensionWithPeriod)

            End If

        Loop While (lPos > 0)

        ' There is 1 real extension and n*2 non-real extension
        lNumNonRealExtensions = (lNumExtensionOccurrences \ 2)

        ' Start searching from the end to locate the real extension
        ' Skip the number of non-real extensions, before reaching the real extension

        ' Change to lowercase to make search case-insensitive
        strSearchString = LCase$(sFileName)

        lStart = -1

        Do

            lPos = InStrRev(strSearchString, LCase$(strExtensionWithPeriod), lStart)

            If (lPos > 0) Then

                lNumNonRealExtensions = lNumNonRealExtensions - 1

                ' Move start point of search
                lStart = lPos - 1

            End If

        Loop While ((lPos > 0) And (lNumNonRealExtensions >= 0))

        'lStart points to the start of real extension
        sFileName = Left$(sFileName, lStart) & strExtensionWithPeriod

        If fileOp = 1 Then
            MsgBox("XXX_FileSave = " & sFileName)
        Else
            MsgBox("XXX_FileOpen = " & sFileName)
        End If

    End Function
```

```vb
 #End  Region

 #Region  "UI Methods"

     Public Sub AddCommandMgr()

         Dim iBmp As New BitmapHandler
         Dim thisAssembly As Assembly

         Dim cmdIndex0 As Integer, cmdIndex1 As Integer
         Dim Title As String = "VB.NET Add-in"
         Dim ToolTip As String = "VB.NET Add-in"

         Dim docTypes() As Integer = {swDocumentTypes_e.swDocASSEMBLY, _
                                        swDocumentTypes_e.swDocDRAWING, _
                                        swDocumentTypes_e.swDocPART}

         thisAssembly = System.Reflection.Assembly.GetAssembly(Me.GetType())

         cmdGroup = iCmdMgr.CreateCommandGroup(1, Title, ToolTip, "", -1)
         cmdGroup.LargeIconList = iBmp.CreateFileFromResourceBitmap("SwVBAddin1.ToolbarLarge.bmp", thisAssembly)
         cmdGroup.SmallIconList = iBmp.CreateFileFromResourceBitmap("SwVBAddin1.ToolbarSmall.bmp", thisAssembly)
         cmdGroup.LargeMainIcon = iBmp.CreateFileFromResourceBitmap("SwVBAddin1.MainIconLarge.bmp", thisAssembly)
         cmdGroup.SmallMainIcon = iBmp.CreateFileFromResourceBitmap("SwVBAddin1.MainIconSmall.bmp", thisAssembly)

         cmdIndex0 = cmdGroup.AddCommandItem("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", 0)
         cmdIndex1 = cmdGroup.AddCommandItem("Show PMP", -1,  "Show PMP", "Show PMP", 2, "ShowPMP", "PMPEnable", 2)

         cmdGroup.HasToolbar = True
         cmdGroup.HasMenu =  True
         cmdGroup.Activate()

         For Each docType As Integer In docTypes
             Dim cmdTab As ICommandTab = iCmdMgr.GetCommandTab(docType, Title)
             Dim bResult As Boolean

             If cmdTab Is Nothing Then
                 cmdTab = iCmdMgr.AddCommandTab(docType, Title)

                 Dim cmdBox As CommandTabBox = cmdTab.AddCommandTabBox

                 Dim cmdIDs(3) As Integer
                 Dim TextType(3) As Integer

                 cmdIDs(0) = cmdGroup.CommandID(cmdIndex0)
                 TextType(0) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

                 cmdIDs(1) = cmdGroup.CommandID(cmdIndex1)
                 TextType(1) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

                 cmdIDs(2) = cmdGroup.ToolbarId
                 TextType(2) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal

                 bResult = cmdBox.AddCommands(cmdIDs, TextType)

                 Dim cmdBox1 As CommandTabBox = cmdTab.AddCommandTabBox()
                 ReDim cmdIDs(1)
                 ReDim TextType(1)

                 cmdIDs(0) = cmdGroup.ToolbarId
                 TextType(0) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow

                 bResult = cmdBox1.AddCommands(cmdIDs, TextType)

                 cmdTab.AddSeparator(cmdBox1, cmdGroup.ToolbarId)

             End If
         Next

         ' create a third-party icon in the context-sensitive menus of faces in parts
         frame = SwApp.Frame()
         resultCode = frame.AddMenuPopupIcon2(swDocumentTypes_e.swDocPART, swSelectType_e.swSelFACES, "third-party context-sensitive", addinID,  "CSCallbackFunction", "CSEnable", "", cmdGroup.SmallMainIcon)

         ' create and register the shortcut menu
         registerID = SwApp.RegisterThirdPartyPopupMenu()
         ' add a menu break at the top of the shortcut menu
         resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, CInt(swDocumentTypes_e.swDocPART), "Menu Break", addinID, "", "", "", "", "", CInt(swMenuItemType_e.swMenuItemType_Break))
         ' add a couple of items to the shortcut menu
         resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, CInt(swDocumentTypes_e.swDocPART), "Test1", addinID, "TestCallback", "EnableTest", "", "Test1", cmdGroup.SmallMainIcon, CInt(swMenuItemType_e.swMenuItemType_Default))
         resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, CInt(swDocumentTypes_e.swDocPART), "Test4", addinID, "TestCallback", "EnableTest", "", "Test4", cmdGroup.SmallMainIcon, CInt(swMenuItemType_e.swMenuItemType_Default))
         ' add a separator bar to the shortcut menu
         resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, CInt(swDocumentTypes_e.swDocPART), "separator", addinID, "", "", "", "", "", CInt(swMenuItemType_e.swMenuItemType_Separator))
         ' add another item to the shortcut menu
         resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, CInt(swDocumentTypes_e.swDocPART), "Test5", addinID, "TestCallback", "EnableTest", "", "Test5", cmdGroup.SmallMainIcon, CInt(swMenuItemType_e.swMenuItemType_Default))

         ' add an icon to a menu bar of the shortcut menu
         resultCode = SwApp.AddItemToThirdPartyPopupMenu2(registerID, CInt(swDocumentTypes_e.swDocPART), "", addinID, "TestCallback", "EnableTest", "", "NoOp", cmdGroup.SmallMainIcon, CInt(swMenuItemType_e.swMenuItemType_Default))

         ' remove an icon from the menu bar of the shortcut menu
         'resultCode = SwApp.RemoveItemFromThirdPartyPopupMenu(registerID, CInt(swDocumentTypes_e.swDocPART), "", 1)
         thisAssembly =  Nothing
         iBmp.Dispose()
     End Sub

     Public Sub RemoveCommandMgr()
         iCmdMgr.RemoveCommandGroup(1)
     End Sub

     Function AddPMP() As Boolean
         ppage =  New UserPMPage
         ppage.Init(iSwApp, Me)
     End Function

     Function RemovePMP() As Boolean
         ppage =  Nothing
     End Function
 #End  Region

 #Region  "Event Methods"
     Sub AttachEventHandlers()
         AttachSWEvents()

         'Listen for events on all currently open docs
         AttachEventsToAllDocuments()
     End Sub

     Sub DetachEventHandlers()
         DetachSWEvents()

         'Close events on all currently open docs
         Dim docHandler As DocumentEventHandler
         Dim key As ModelDoc2
         Dim numKeys As Integer
         numKeys = openDocs.Count
         If numKeys > 0 Then
             Dim keys() As Object = New Object(numKeys - 1) {}

             'Remove all document event handlers
             openDocs.Keys.CopyTo(keys, 0)
             For Each key In keys
                 docHandler = openDocs.Item(key)
                 docHandler.DetachEventHandlers()  'This also removes the pair from the hash
                 docHandler =  Nothing
                 key =  Nothing
             Next
         End If
     End Sub

     Sub AttachSWEvents()
         AddHandler iSwApp.ActiveDocChangeNotify,  AddressOf  Me.SldWorks_ActiveDocChangeNotify
         AddHandler iSwApp.DocumentLoadNotify2,  AddressOf  Me.SldWorks_DocumentLoadNotify2
         AddHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
         AddHandler iSwApp.ActiveModelDocChangeNotify,  AddressOf  Me.SldWorks_ActiveModelDocChangeNotify
         AddHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
         AddHandler iSwApp.InterfaceBrightnessThemeChangeNotify, AddressOf Me.SldWorks_InterfaceBrightnessChangeThemeNotify

     End Sub

     Sub DetachSWEvents()
         RemoveHandler iSwApp.ActiveDocChangeNotify,  AddressOf  Me.SldWorks_ActiveDocChangeNotify
         RemoveHandler iSwApp.DocumentLoadNotify2,  AddressOf  Me.SldWorks_DocumentLoadNotify2
         RemoveHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
         RemoveHandler iSwApp.ActiveModelDocChangeNotify,  AddressOf  Me.SldWorks_ActiveModelDocChangeNotify
         RemoveHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
         RemoveHandler iSwApp.InterfaceBrightnessThemeChangeNotify,  AddressOf Me.SldWorks_InterfaceBrightnessChangeThemeNotify

     End Sub

     Sub AttachEventsToAllDocuments()
         Dim modDoc As ModelDoc2
         modDoc = iSwApp.GetFirstDocument()
         While Not modDoc Is Nothing
             If Not openDocs.Contains(modDoc) Then
                 AttachModelDocEventHandler(modDoc)
             End If
             modDoc = modDoc.GetNext()
         End While
     End Sub

     Function AttachModelDocEventHandler(ByVal modDoc As ModelDoc2) As Boolean
         If modDoc Is Nothing Then
             Return False
         End If
         Dim docHandler As DocumentEventHandler = Nothing

         If Not openDocs.Contains(modDoc) Then
             Select Case modDoc.GetType
                 Case swDocumentTypes_e.swDocPART
                     docHandler = New PartEventHandler()
                 Case swDocumentTypes_e.swDocASSEMBLY
                     docHandler = New AssemblyEventHandler()
                 Case swDocumentTypes_e.swDocDRAWING
                     docHandler = New DrawingEventHandler()
             End Select

             docHandler.Init(iSwApp,  Me, modDoc)
             docHandler.AttachEventHandlers()
             openDocs.Add(modDoc, docHandler)
         End If
     End Function

     Sub DetachModelEventHandler(ByVal modDoc As ModelDoc2)
         Dim docHandler As DocumentEventHandler
         docHandler = openDocs.Item(modDoc)
         openDocs.Remove(modDoc)
         modDoc = Nothing
         docHandler =  Nothing
     End Sub
 #End  Region

 #Region  "Event Handlers"
     Function SldWorks_ActiveDocChangeNotify() As Integer
         'TODO: Add your implementation here
     End Function

     Function SldWorks_DocumentLoadNotify2(ByVal docTitle As String, ByVal docPath As String) As  Integer

     End Function

     Function SldWorks_FileNewNotify2(ByVal newDoc As Object, ByVal doctype As Integer, ByVal templateName As String) As  Integer
         AttachEventsToAllDocuments()
     End Function

     Function SldWorks_ActiveModelDocChangeNotify() As Integer
         'TODO: Add your implementation here
     End Function

     Function SldWorks_FileOpenPostNotify(ByVal FileName As String) As  Integer
         AttachEventsToAllDocuments()
     End Function
    Function SldWorks_InterfaceBrightnessChangeThemeNotify(ByVal Theme As Integer, ByRef Colors as Object) As  Integer
         MsgBox("Interface brightness theme changed to (0 = light, 1 = medium, 2 = dark): " & Theme)
         Dim colorsArray() As Integer
         colorsArray = Colors
         MsgBox("FeatureManager design tree color: " & colorsArray(0))
     End Function
 #End  Region

 #Region  "UI Callbacks"
     Sub CreateCube()

         'make sure we have a part open
         Dim partTemplate As String

         Dim featMan As FeatureManager

         partTemplate = iSwApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)
         model = iSwApp.NewDocument(partTemplate, swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0)

         model.InsertSketch2(True)
         model.SketchRectangle(0, 0, 0, 0.1, 0.1, 0.1,  False)

         'Extrude the sketch
         featMan = model.FeatureManager
         featMan.FeatureExtrusion(True, _
                                   False, False, _
                                   swEndConditions_e.swEndCondBlind, swEndConditions_e.swEndCondBlind, _
                                   0.1, 0.0, _
                                   False, False, _
                                   False, False, _
                                   0.0, 0.0, _
                                   False, False, _
                                   False, False, _
                                   True, _
                                   False, False)

     End Sub
     Sub CSCallbackFunction()
         resultCode = SwApp.ShowThirdPartyPopupMenu(registerID, 500, 500)
     End Sub
     Function CSEnable() As Integer
         If iSwApp.ActiveDoc Is Nothing Then
             CSEnable = 0
         Else
             CSEnable = 1
         End If
     End Function
     Sub ShowPMP()
         ppage.Show()

     End Sub

     Function PMPEnable() As Integer
         If iSwApp.ActiveDoc Is Nothing Then
             PMPEnable = 0
         Else
             PMPEnable = 1
         End If
     End Function
     Sub TestCallback()
         System.Diagnostics.Debug.Print("Test callback")
     End Sub
     Function EnableTest() As Integer
         If iSwApp.ActiveDoc Is Nothing Then
             EnableTest = 0
         Else
             EnableTest = 1
         End If
     End Function
 #End  Region

 End Class
```
