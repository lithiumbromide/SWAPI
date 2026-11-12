---
title: "Create Flyouts in the CommandManager Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Flyouts_in_the_CommandManager_Example_VBNET.htm"
---

# Create Flyouts in the CommandManager Example (VB.NET)

This example shows how to use an add-in to create flyouts in:

- CommandManager
- context-sensitive menus of selected faces

```
'---------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the SOLIDWORKS API SDK add-in templates for your version
'    of Microsoft Visual Studio are installed.
' 2. In Microsoft Visual Studio, create a Visual Basic project using the
'    SwVBAddin template.
' 3. Name the project SwVBAddin1.
' 4. Copy and paste SwAddin into SwAddin.vb of your project.
' 5. Click Project > SwVBAddin1 Properties > Debug.
' 6. Select Start external program and type the pathname to your
'    SOLIDWORKS executable.
' 7. Replace the text shown for the icons and mainIcons array elements
'    with the pathnames to your image files.
' 8. Press F5 to start debugging this add-in.
'
' Postconditions:
' 1. In SOLIDWORKS, click Tools > VB.NET Add-in > CreateCube.
' 2. Click Dynamic Flyout in the CommandManager and click FlyoutCommand 2.
' 3. Inspect the Immediate window.
' 4. Click a face of the cube.
' 5. Click the flyout button in the face's context-sensitive menu and
'    click FlyoutCommand 1.
' 6. Inspect the Immediate window.
'---------------------------------------------------------------------------

' SwAddin

Imports System
Imports System.Collections
Imports System.Reflection
Imports System.Runtime.InteropServices

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports SolidWorks.Interop.swpublished
Imports SolidWorksTools
Imports SolidWorksTools.File

Imports System.Collections.Generic
Imports System.Diagnostics

' This VB.NET add-in shows how to create a flyout menu in both the CommandManager
' and the context-sensitive menus of selected faces

<Guid("88bf8dab-7623-4846-9a76-c1f64a2ebeba")> _
    <ComVisible(True)> _
    <SwAddin( _
        Description:="A flyout menu appears on the toolbar and on the context-sensitive menus of selected faces.", _
        Title:="VB.NET Add-in", _
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
    Dim iBmp As BitmapHandler
    Dim cmdGroup As ICommandGroup

    Public Const mainCmdGroupID As Integer = 0
    Public Const mainItemID1 As Integer = 0
    Public Const mainItemID2 As Integer = 1
    Public Const flyoutGroupID As Integer = 91

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
#End Region

#Region "SOLIDWORKS Registration"

    <ComRegisterFunction()> Public Shared Sub RegisterFunction(ByVal t As Type)

        ' Get Custom Attribute: SwAddinAttribute
        Dim attributes() As Object
        Dim SWattr As SwAddinAttribute = Nothing

        attributes = System.Attribute.GetCustomAttributes(GetType(SwAddin), GetType(SwAddinAttribute))

        If attributes.Length > 0 Then
            SWattr = DirectCast(attributes(0), SwAddinAttribute)
        End If
        Try
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
        Catch nl As System.NullReferenceException
            Console.WriteLine("There was a problem registering this dll: SWattr is null.\n " & nl.Message)
            System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: SWattr is null.\n" & nl.Message)
        Catch e As System.Exception
            Console.WriteLine("There was a problem registering this dll: " & e.Message)
            System.Windows.Forms.MessageBox.Show("There was a problem registering this dll: " & e.Message)
        End Try
    End Sub

    <ComUnregisterFunction()> Public Shared Sub UnregisterFunction(ByVal t As Type)
        Try
            Dim hklm As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.LocalMachine
            Dim hkcu As Microsoft.Win32.RegistryKey = Microsoft.Win32.Registry.CurrentUser

            Dim keyname As String = "SOFTWARE\SOLIDWORKS\Addins\{" + t.GUID.ToString() + "}"
            hklm.DeleteSubKey(keyname)

            keyname = "Software\SOLIDWORKS\AddInsStartup\{" + t.GUID.ToString() + "}"
            hkcu.DeleteSubKey(keyname)
        Catch nl As System.NullReferenceException
            Console.WriteLine("There was a problem unregistering this dll: SWattr is null.\n " & nl.Message)
            System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: SWattr is null.\n" & nl.Message)
        Catch e As System.Exception
            Console.WriteLine("There was a problem unregistering this dll: " & e.Message)
            System.Windows.Forms.MessageBox.Show("There was a problem unregistering this dll: " & e.Message)
        End Try

    End Sub

#End Region

#Region "ISwAddin Implementation"

    Function ConnectToSW(ByVal ThisSW As Object, ByVal Cookie As Integer) As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.ConnectToSW
        iSwApp = ThisSW
        addinID = Cookie

        ' Set up callbacks
        iSwApp.SetAddinCallbackInfo2(0, Me, addinID)

        ' Set up the CommandManager
        iCmdMgr = iSwApp.GetCommandManager(Cookie)
        AddCommandMgr()

        ' Set up the Event Handlers
        SwEventPtr = iSwApp
        openDocs = New Hashtable
        AttachEventHandlers()

        ' Set up PropertyManager page
        AddPMP()

        ConnectToSW = True
    End Function

    Function DisconnectFromSW() As Boolean Implements SolidWorks.Interop.swpublished.SwAddin.DisconnectFromSW

        RemoveCommandMgr()
        RemovePMP()
        DetachEventHandlers()

        System.Runtime.InteropServices.Marshal.ReleaseComObject(iCmdMgr)
        iCmdMgr = Nothing
        System.Runtime.InteropServices.Marshal.ReleaseComObject(iSwApp)
        iSwApp = Nothing
        ' The add-in must call GC.Collect() here to retrieve all managed code pointers
        GC.Collect()
        GC.WaitForPendingFinalizers()

        GC.Collect()
        GC.WaitForPendingFinalizers()

        DisconnectFromSW = True
    End Function
#End Region

#Region "UI Methods"
    Public Sub AddCommandMgr()

        If iBmp Is Nothing Then
            iBmp = New BitmapHandler()
        End If

        Dim thisAssembly As Assembly

        Dim cmdIndex0 As Integer, cmdIndex1 As Integer
        Dim Title As String = "VB.NET Add-in"
        Dim ToolTip As String = "Flyout demo"

        Dim docTypes() As Integer = {swDocumentTypes_e.swDocASSEMBLY, _
                                       swDocumentTypes_e.swDocDRAWING, _
                                       swDocumentTypes_e.swDocPART}

        thisAssembly = System.Reflection.Assembly.GetAssembly(Me.GetType())

        Dim cmdGroupErr As Integer = 0
        Dim ignorePrevious As Boolean = False

        Dim registryIDs As Object = Nothing
        Dim getDataResult As Boolean = iCmdMgr.GetGroupDataFromRegistry(mainCmdGroupID, registryIDs)

        Dim knownIDs As Integer() = New Integer(1) {mainItemID1, mainItemID2}

        If getDataResult Then
            If Not CompareIDs(registryIDs, knownIDs) Then ' If the IDs don't match, reset the CommandGroup
                ignorePrevious = True
            End If
        End If
```

```
   Dim smallImage As Integer
   Dim mediumImage As Integer
   Dim largeImage As Integer
   Dim imageSizeToUse As Integer

   imageSizeToUse = SwApp.GetImageSize(smallImage, mediumImage, largeImage)

   Debug.Print("Image sizes:")
   Debug.Print("  Default PropertyManager page and menu icon size based on DPI setting: " & imageSizeToUse)
   Debug.Print("    Small image size based on DPI setting: " & smallImage)
   Debug.Print("    Medium image size based on DPI setting: " & mediumImage)
   Debug.Print("    Large image size based on DPI setting: " & largeImage)
```

```
   cmdGroup = iCmdMgr.CreateCommandGroup2(mainCmdGroupID, Title, ToolTip, "", -1, ignorePrevious, cmdGroupErr)
   If cmdGroup Is Nothing Or thisAssembly Is Nothing Then
       Throw New NullReferenceException()
   End If
```

```
        Dim mainIcons(2) As String
        Dim icons(2) As String
        icons(0) = "Pathname_to_toolbar_nxn_image"
        icons(1) = "Pathname_to_toolbar_nnxnn_image"
        icons(2) = "Pathname_to_toolbar_nnnxnnn_image"
        mainIcons(0) = "Pathname_to_nxn_image"
        mainIcons(1) = "Pathname_to_nnxnn_image"
        mainIcons(2) = "Pathname_to_nnnxnnn_image"

        cmdGroup.IconList = icons
        cmdGroup.MainIconList = mainIcons

        Dim menuToolbarOption As Integer = swCommandItemType_e.swMenuItem Or swCommandItemType_e.swToolbarItem

        cmdIndex0 = cmdGroup.AddCommandItem2("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", mainItemID1, menuToolbarOption)
        cmdIndex1 = cmdGroup.AddCommandItem2("Show PMP", -1, "Display sample property manager", "Show PMP", 2, "ShowPMP", "PMPEnable", mainItemID2, menuToolbarOption)

        cmdGroup.HasToolbar = True
        cmdGroup.HasMenu = True
        cmdGroup.Activate()

        ' Get number of command IDs in the CommandGroup
        Debug.Print("Number of command IDs in the CommandGroup is " & iCmdMgr.GetCommandIDsCount(0).ToString())

        ' Get group data from registry
        Dim userIDs As Integer()
        Dim objIDs As Object = Nothing
        iCmdMgr.GetGroupDataFromRegistry(0, objIDs)
        userIDs = DirectCast(objIDs, Integer())
        Debug.Print("Command IDs found in the registry:")
        For Each ID As Integer In userIDs
            Debug.Print(ID.ToString())
        Next

        Dim bResult As Boolean

        Dim flyGroup As FlyoutGroup

        flyGroup = iCmdMgr.CreateFlyoutGroup2(flyoutGroupID, "Dynamic Flyout", "Dynamic Flyout", "Flyout Hint", _
              mainIcons, icons, "FlyoutCallback", "FlyoutEnable")

        ' Add the FlyoutGroup to the context-sensitive menus of faces in parts
        bResult = flyGroup.AddContextMenuFlyout(CInt(swDocumentTypes_e.swDocPART), CInt(swSelectType_e.swSelFACES))
        Debug.Print("Context-sensitive menu flyout created for faces in parts: " & bResult.ToString())

        ' Get the total number of FlyoutGroups in CommandManager
        Debug.Print("Number of FlyoutGroups is " & iCmdMgr.NumberOfFlyoutGroups)

        ' Get the FlyoutGroups
        Dim objGroups As Object()
        objGroups = DirectCast(iCmdMgr.GetFlyoutGroups(), Object())
        Debug.Print("Find all FlyoutGroups in CommandManager:")
        Dim i As Integer
        For i = 0 To objGroups.GetUpperBound(0)
            Debug.Print("FlyoutGroup found")
        Next

        ' Get a FlyoutGroup by its user-defined ID
        Dim fogrp As IFlyoutGroup
        fogrp = iCmdMgr.GetFlyoutGroup(91)
        Debug.Print(" CmdID: " & fogrp.CmdID)
        Debug.Print(" Button count: " & fogrp.ButtonCount)
        Debug.Print(" Flyout type: " & fogrp.FlyoutType)
        mainIcons = fogrp.MainIconList
        Debug.Print(" Small button: " & mainIcons(0))
        Debug.Print(" Medium button: " & mainIcons(1))
        Debug.Print(" Large button: " & mainIcons(2))
        icons = fogrp.IconList
        Debug.Print(" Small toolbar button: " & icons(0))
        Debug.Print(" Medium toolbar button: " & icons(1))
        Debug.Print(" Large toolbar button: " & icons(2))

        For Each docType As Integer In docTypes
            Dim cmdTab As ICommandTab = iCmdMgr.GetCommandTab(docType, Title)

            If Not cmdTab Is Nothing And Not getDataResult Or ignorePrevious Then ' If tab exists, but the registry info is ignored, then re-create the tab; otherwise the IDs won't match and the tab will be blank
                Dim res As Boolean = iCmdMgr.RemoveCommandTab(cmdTab)
                cmdTab = Nothing
            End If

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

                cmdIDs(0) = flyGroup.CmdID
                TextType(0) = swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow

                bResult = cmdBox1.AddCommands(cmdIDs, TextType)

                cmdTab.AddSeparator(cmdBox1, cmdIDs(0))

            End If
        Next

        thisAssembly = Nothing

    End Sub

    Public Sub RemoveCommandMgr()
        Try
            iBmp.Dispose()
            iCmdMgr.RemoveCommandGroup(mainCmdGroupID)
            iCmdMgr.RemoveFlyoutGroup(flyoutGroupID)
        Catch e As Exception
        End Try
    End Sub

    Function AddPMP() As Boolean
        ppage = New UserPMPage
        ppage.Init(iSwApp, Me)
    End Function

    Function RemovePMP() As Boolean
        ppage = Nothing
    End Function

    Function CompareIDs(ByVal storedIDs() As Integer, ByVal addinIDs() As Integer) As Boolean

        Dim storeList As New List(Of Integer)(storedIDs)
        Dim addinList As New List(Of Integer)(addinIDs)

        addinList.Sort()
        storeList.Sort()

        If Not addinList.Count = storeList.Count Then

            Return False
        Else

            For i As Integer = 0 To addinList.Count - 1
                If Not addinList(i) = storeList(i) Then

                    Return False
                End If
            Next
        End If

        Return True
    End Function
#End Region

#Region "Event Methods"
    Sub AttachEventHandlers()
        AttachSWEvents()

        ' Listen for events on all currently open docs
        AttachEventsToAllDocuments()
    End Sub

    Sub DetachEventHandlers()
        DetachSWEvents()

        ' Close events on all currently open docs
        Dim docHandler As DocumentEventHandler
        Dim key As ModelDoc2
        Dim numKeys As Integer
        numKeys = openDocs.Count
        If numKeys > 0 Then
            Dim keys() As Object = New Object(numKeys - 1) {}

            ' Remove all document event handlers
            openDocs.Keys.CopyTo(keys, 0)
            For Each key In keys
                docHandler = openDocs.Item(key)
                docHandler.DetachEventHandlers() ' This also removes the pair from the hash
                docHandler = Nothing
                key = Nothing
            Next
        End If
    End Sub

    Sub AttachSWEvents()
        Try
            AddHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
            AddHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
            AddHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
            AddHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
            AddHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
        Catch e As Exception
            Console.WriteLine(e.Message)
        End Try
    End Sub

    Sub DetachSWEvents()
        Try
            RemoveHandler iSwApp.ActiveDocChangeNotify, AddressOf Me.SldWorks_ActiveDocChangeNotify
            RemoveHandler iSwApp.DocumentLoadNotify2, AddressOf Me.SldWorks_DocumentLoadNotify2
            RemoveHandler iSwApp.FileNewNotify2, AddressOf Me.SldWorks_FileNewNotify2
            RemoveHandler iSwApp.ActiveModelDocChangeNotify, AddressOf Me.SldWorks_ActiveModelDocChangeNotify
            RemoveHandler iSwApp.FileOpenPostNotify, AddressOf Me.SldWorks_FileOpenPostNotify
        Catch e As Exception
            Console.WriteLine(e.Message)
        End Try
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

            docHandler.Init(iSwApp, Me, modDoc)
            docHandler.AttachEventHandlers()
            openDocs.Add(modDoc, docHandler)
        End If
    End Function

    Sub DetachModelEventHandler(ByVal modDoc As ModelDoc2)
        Dim docHandler As DocumentEventHandler
        docHandler = openDocs.Item(modDoc)
        openDocs.Remove(modDoc)
        modDoc = Nothing
        docHandler = Nothing
    End Sub
#End Region

#Region "Event Handlers"
    Function SldWorks_ActiveDocChangeNotify() As Integer
        ' TODO: Add your implementation here
    End Function

    Function SldWorks_DocumentLoadNotify2(ByVal docTitle As String, ByVal docPath As String) As Integer

    End Function

    Function SldWorks_FileNewNotify2(ByVal newDoc As Object, ByVal doctype As Integer, ByVal templateName As String) As Integer
        AttachEventsToAllDocuments()
    End Function

    Function SldWorks_ActiveModelDocChangeNotify() As Integer
        ' TODO: Add your implementation here
    End Function

    Function SldWorks_FileOpenPostNotify(ByVal FileName As String) As Integer
        AttachEventsToAllDocuments()
    End Function
#End Region

#Region "UI Callbacks"
    Sub CreateCube()

        ' Make sure a part open is open
        Dim partTemplate As String
        Dim model As ModelDoc2
        Dim featMan As FeatureManager

        partTemplate = iSwApp.GetUserPreferenceStringValue(swUserPreferenceStringValue_e.swDefaultTemplatePart)
        If Not partTemplate = "" Then
            model = iSwApp.NewDocument(partTemplate, swDwgPaperSizes_e.swDwgPaperA2size, 0.0, 0.0)

            Dim sketchMgr As SketchManager
            sketchMgr = model.SketchManager
            sketchMgr.InsertSketch(True)
            sketchMgr.CreateCornerRectangle(0, 0, 0, 0.1, 0.1, 0.1)

            ' Extrude the sketch
            featMan = model.FeatureManager
            featMan.FeatureExtrusion3(True, _
                                      False, False, _
                                      swEndConditions_e.swEndCondBlind, swEndConditions_e.swEndCondBlind, _
                                      0.1, 0.0, _
                                      False, False, _
                                      False, False, _
                                      0.0, 0.0, _
                                      False, False, _
                                      False, False, _
                                      False, _
                                      False, True, swStartConditions_e.swStartSketchPlane, 0.0, False)
        Else
            System.Windows.Forms.MessageBox.Show("There is no part template available. Please check your options and make sure there is a part template selected, or select a new part template.")
        End If
    End Sub
    Sub ShowPMP()
        If Not ppage Is Nothing Then
            ppage.Show()
        End If
    End Sub

    Function PMPEnable() As Integer
        If iSwApp.ActiveDoc Is Nothing Then
            PMPEnable = 0
        Else
            PMPEnable = 1
        End If
    End Function

    Sub FlyoutCallback()
        Dim flyGroup As FlyoutGroup = iCmdMgr.GetFlyoutGroup(flyoutGroupID)
        flyGroup.RemoveAllCommandItems()

        flyGroup.AddCommandItem("FlyoutCommand 1", "FlyoutCommand 1", 0, "FlyoutCommandItem1", "FlyoutEnableCommandItem1")
        flyGroup.AddCommandItem("FlyoutCommand 2", "FlyoutCommand 2", 0, "FlyoutCommandItem2", "FlyoutEnableCommandItem2")

        flyGroup.FlyoutType = CInt(swCommandFlyoutStyle_e.swCommandFlyoutStyle_LastUsed)

    End Sub

    Public Sub FlyoutCommandItem1()
        Debug.Print("FlyoutCommand 1 called")
    End Sub

    Public Function FlyoutEnableCommandItem1() As Integer
        Return 1
    End Function

    Public Sub FlyoutCommandItem2()
        Debug.Print("FlyoutCommand 2 called")
    End Sub

    Public Function FlyoutEnableCommandItem2() As Integer
        Return 1
    End Function

    Function FlyoutEnable() As Integer
        If cmdGroup.HasEnabledButton Then
            Return 1
        Else
            Return 0
        End If
    End Function

#End Region

End Class
```
