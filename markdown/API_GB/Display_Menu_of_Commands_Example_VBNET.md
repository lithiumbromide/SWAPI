---
title: "Display Menu of Add-ins Commands Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "API_GB/Display_Menu_of_Commands_Example_VBNET.htm"
---

# Display Menu of Add-ins Commands Example (VB.NET)

## Display Menu of Commands Example (VB.NET)

This example shows how to display a menu of commands, including commands registered by any SOLIDWORKS PDM Professional add-ins and the Administrate Add-ins command.

**NOTE**: If using the primary interop assembly provided with SOLIDWORKS PDM Professional, see [Using .NET Framework 4.0 in Stand-alone Applications](Using_NET_Framework_in_Applications.htm).

```vb
'--------------------------------------------------------------------------------------
 ' Preconditions:
 '  1. Start Microsoft Visual Studio 2010.
 '     a. Click File > New > Project > Visual Basic > Console Application.
 '     b. Type MenuVBNET in Name.
 '     c. Click Browse and navigate to the folder where to create the project.
 '     d. Click OK.
 '     e. Replace the code in Module1.vb with this code.
 '  2. Add EPDM.Interop.epdm.dll as a reference (right-click the project
 '     name in the Solution Explorer, click Add Reference, click
 '     Assemblies > Framework in the left-side panel, browse to the top folder of
 '     your SOLIDWORKS PDM Professional installation, locate and click
 '     EPDM.Interop.epdm.dll, click Open, and click Add).
 '  3. Add System.Windows.Forms as a reference (click System.Windows.Forms
 '     in the Name column, click Add, and click Close).
 '  4. Right-click EPDM.Interop.epdm in References, click Properties, and set
 '     Embed Interop Types to False to handle methods that pass arrays of
 '     structures.
 '  5. Replace ACME_LAB with the name of a valid vault view.
 '  6. Click Debug > Start Debugging or press F5.
 '
 ' Postconditions:
 '  1. Displays the command window.
 '     a. Click anywhere on the desktop.
 '     b. Displays the menu in the upper-left corner of the desktop.
 '     c. Click First Command in the menu.
 '     d. Click OK to close the message box.
 '     e. Click the command window and press any key.
 '     f. Closes the command window and exits the application.
 ' 2. Click Debug > Start Debugging or press F5 again.
 '     a. Displays the command window.
 '     b. Click anywhere on the desktop.
 '     c. Displays the menu in the upper-left corner of the desktop.
 '     d. Click the Administrate Add-ins in the menu.
 '        1. Displays the Administrate Add-ins dialog box.
 '        2. Click Cancel to close the dialog box.
 '     e. Click the command window and press any key.
 '     f. Closes the command window and exits the application.
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

         'Add menu items for registered add-ins and add
         'the Administrate Add-ins command
         Dim count As Integer
         count = 0
         Dim startID As Integer
         startID = 200
         Dim menuCallback As IEdmMenu7
         menuCallback = vault.CreatePluginMenu2(mnu.Handle.ToInt32(), 3, startID, selList, CreateMenuFlags.Cmf_ContextMenu + CreateMenuFlags.Cmf_IncludeAdminReactors, count)

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
                 menuCallback.OnMenuItem2(cmdID, mnu.Handle.ToInt32(), vault.RootFolderID, selList)
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
