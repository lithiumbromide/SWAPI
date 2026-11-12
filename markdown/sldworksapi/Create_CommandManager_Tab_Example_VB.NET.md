---
title: "Create CommandManager Tab Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_CommandManager_Tab_Example_VB.NET.htm"
---

# Create CommandManager Tab Example (VB.NET)

This example shows how to create a CommandManager command tab.

NOTES:

- This example is only a code snippet. The complete project is available in the SOLIDWORKS API SDK.
- Your add-in must check to see if the tab already exists. If the tab already exists, then you must use that tab instead of creating a new tab. If your add-in does not check for an existing tab, then SOLIDWORKS Design will create a new tab each time it starts up.

```vb
...
        Dim cmdGroup As ICommandGroup
        Dim iBmp As New BitmapHandler
        Dim thisAssembly As Assembly

        Dim cmdIndex0 As Integer, cmdIndex1 As Integer
        Dim Title As String = "VB Addin"
        Dim ToolTip As String = "VB Addin"

        Dim docTypes() As Integer = {swDocumentTypes_e.swDocASSEMBLY, _
                                       swDocumentTypes_e.swDocDRAWING, _
                                       swDocumentTypes_e.swDocPART}

        thisAssembly = System.Reflection.Assembly.GetAssembly(Me.GetType())

        cmdGroup = iCmdMgr.CreateCommandGroup(1, Title, ToolTip, "", -1)
        cmdGroup.LargeIconList = iBmp.CreateFileFromResourceBitmap("SwVBAddin3.ToolbarLarge.bmp", thisAssembly)
        cmdGroup.SmallIconList = iBmp.CreateFileFromResourceBitmap("SwVBAddin3.ToolbarSmall.bmp", thisAssembly)
        cmdGroup.LargeMainIcon = iBmp.CreateFileFromResourceBitmap("SwVBAddin3.MainIconLarge.bmp", thisAssembly)
        cmdGroup.SmallMainIcon = iBmp.CreateFileFromResourceBitmap("SwVBAddin3.MainIconSmall.bmp", thisAssembly)

        cmdIndex0 = cmdGroup.AddCommandItem("CreateCube", -1, "Create a cube", "Create cube", 0, "CreateCube", "", 0)
        cmdIndex1 = cmdGroup.AddCommandItem("Show PMP", -1, "Display sample property manager", "Show PMP", 2, "ShowPMP", "PMPEnable", 2)

        cmdGroup.HasToolbar = True
        cmdGroup.HasMenu = True
        cmdGroup.Activate()

        For Each docType As Integer In docTypes
            Dim cmdTabs() As Object = iCmdMgr.CommandTabs(docType)
            Dim cmdTab As ICommandTab

            Dim tabExists As Boolean = False

            For i As Integer = 0 To iCmdMgr.GetCommandTabCount(docType) - 1
                cmdTab = cmdTabs(i)
                If cmdTab.TabName = Title Then
                    tabExists = True
                    Exit For
                End If
            Next

            If Not tabExists Then
                cmdTab = iCmdMgr.CreateCommandTab(-1, Title, docType)

                cmdTab.AddCommand(cmdGroup.CommandID(cmdIndex0))
                cmdTab.SetTextDisplay(cmdGroup.CommandID(cmdIndex0), swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal)

                cmdTab.AddCommand(cmdGroup.CommandID(cmdIndex1))
                cmdTab.SetTextDisplay(cmdGroup.CommandID(cmdIndex1), swCommandTabButtonTextDisplay_e.swCommandTabButton_TextHorizontal)

                cmdTab.AddCommand(cmdGroup.ToolbarId)
                cmdTab.SetTextDisplay(cmdGroup.ToolbarId, swCommandTabButtonTextDisplay_e.swCommandTabButton_TextBelow)

                cmdTab.AddSeparator(cmdGroup.ToolbarId)
            End If
        Next

        thisAssembly = Nothing
        iBmp.Dispose()
    End Sub
...
```
