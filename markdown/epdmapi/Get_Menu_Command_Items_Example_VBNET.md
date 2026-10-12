---
title: "Get Menu Command Items Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "epdmapi/Get_Menu_Command_Items_Example_VBNET.htm"
---

# Get Menu Command Items Example (VB.NET)

This example shows how to get add-in menu command items.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
'--------------------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Start Microsoft Visual Studio.
 ' 2. Click File > New > Project > Visual Basic, Windows, Console > Console App.
 ' 3. Type MenuVBNET in Project name.
  ' 4. For Location, click ... and navigate to the folder where to create the project.
 ' 5. Click Next.
 ' 6. Select Framework.
 ' 7. Click Create.
 ' 8. Replace the code in Module1.vb with this code.
 ' 9. Add dependencies and safely pass arrays of structures.
 '10. Add System.Windows.Forms as a reference.
 '11. Replace ACME_LAB with the name of a valid vault view.
 '12. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 ' 1. Displays the command window.
 ' 2. Displays a message box for each add-in menu command item.
 ' 3. Click OK to close each message box.
 ' 4. Displays the menu in the upper-left corner of the desktop.
 ' 5. Click First Command in the menu.
 ' 6. Click OK to close the message box.
 ' 7. Click the command window and press any key.
 ' 8. Closes the command window and exits the application.
 '--------------------------------------------------------------------------------------
'Module1.vb

 Imports EPDM.Interop.epdm
 Imports System.Windows.Forms

 Module Module1

     Dim vault As EdmVault5
     Dim frmParent As Form

     Sub Main()
         Try
             'Create a vault interface
             vault = New EdmVault5()

             'Log into vault
             vault.LoginAuto("ACME_LAB", 0)

             'Show menu
             ShowMenu(vault)

         Catch ex As System.Runtime.InteropServices.COMException
             MsgBox("HRESULT = 0x" + ex.ErrorCode.ToString("X") + " " + ex.Message)
         Catch ex As Exception
             MsgBox(ex.Message)
         End Try

         Console.WriteLine()
         Console.WriteLine("Press any key to exit.")
         Console.ReadKey()

     End Sub

     Private Sub ShowMenu(ByVal vault As IEdmVault12)
         'Create a context-sensitive menu
         'using Windows InsertMenu function
         Dim mnu As System.Windows.Forms.ContextMenu
         mnu = New System.Windows.Forms.ContextMenu

         InsertMenu(mnu.Handle, 0, 0, 100, "First Command")
         InsertMenu(mnu.Handle, 0, 0, 101, "Second Command")
         InsertMenu(mnu.Handle, 0, 0, 102, "Third Command")

         'Create a selection list with all files in the root folder
         Dim selList As IEdmSelectionList6
         selList = New EdmSelectionList5

         Dim folder As IEdmFolder6
         folder = vault.RootFolder
         Dim pos As IEdmPos5
         pos = folder.GetFirstFilePosition()
         While Not pos.IsNull
             Dim file As IEdmFile8
             file = folder.GetNextFile(pos)
             Dim obj As EdmSelectionObject
             obj.mbsPath = file.GetLocalPath(folder.ID)
             obj.meType = file.ObjectType
             obj.mlID = file.ID
             obj.mlProjectID = folder.ID
             selList.AddTail2(obj)
         End While

         'Add menu items for registered add-ins
         Dim count As Integer
         count = 0
         Dim startID As Integer
         startID = 200
         Dim menuCallback As IEdmMenu6
         Dim ppoRetItems() As EdmCmdInfo = Nothing
         menuCallback = vault.CreatePluginMenu2(mnu.Handle.ToInt32(), 3, startID, selList, CreateMenuFlags.Cmf_ContextMenu, count)
         menuCallback.GetItems(EdmMenuFlags.EdmMenu_Nothing, ppoRetItems)

         Dim str As String
         For Each item As EdmCmdInfo In ppoRetItems
             str = "Add-in menu command item: " & vbLf
             str = str & "Command ID: " & item.mlCmdID & vbLf
             str = str & "Command string: " & item.mbsCmdStr & vbLf
             str = str & "Tooltip: " & item.mbsTooltip & vbLf
             str = str & "Status bar help: " & item.mbsStatusBarHelp & vbLf
             str = str & "EdmMenuFlags: " & item.mlEdmMenuFlags
             MsgBox(str)
         Next

         'Display the menu using Windows TrackPopupMenu function
         Dim TPM_RETURNCMD As Integer
         TPM_RETURNCMD = 256
         Dim cmdID As Integer
         frmParent = New Form
         cmdID = TrackPopupMenu(mnu.Handle, TPM_RETURNCMD, frmParent.Left, frmParent.Top, 0, frmParent.Handle, 0)

         'Run the selected command
         Select Case cmdID
             Case 100
                 MsgBox("First command")
             Case 101
                 MsgBox("Second command")
             Case 102
                 MsgBox("Third command")
             Case Else
                 MsgBox(cmdID)
         End Select
     End Sub

     Private Declare Function InsertMenu Lib "user32" Alias "InsertMenuA" _
     (ByVal hMenu As System.IntPtr, _
     ByVal uPosition As Integer, _
     ByVal uFlags As Integer, _
     ByVal uIDNewItem As System.IntPtr, _
     ByVal lpNewItem As String) As Boolean

     Private Declare Function TrackPopupMenu Lib "user32" Alias "TrackPopupMenu" _
     (ByVal hMenu As IntPtr, _
     ByVal uFlags As Integer, _
     ByVal x As Integer, _
     ByVal y As Integer, _
     ByVal nReserved As Integer, _
     ByVal hWnd As IntPtr, _
     ByVal prcRect As IntPtr) As Integer

 End Module
```

[Back to top](#Top)
