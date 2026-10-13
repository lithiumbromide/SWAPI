---
title: "Calling Add-ins (C#)"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/csharpcardbutton.htm"
---

# Calling Add-ins (C#)

This sample shows how to implement [IEdmAddIn5::GetAddInInfo](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~GetAddInInfo.html) and [IEdmAddIn5::OnCmd](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmAddIn5~OnCmd.html) to create a Visual C# add-in that is called when the user clicks a button in a file data card. The add-in opens a dialog box in which the user browses for the file whose data card is displayed. The add-in copies the path of the selected file to a text field in the file's data card.

**NOTE:** Because SOLIDWORKS PDM Professional cannot force a reload of add-ins if they are written in .NET, all client machines must be restarted to ensure that the latest version of the add-in is used.

1. Follow [Creating Menu Commands (C#)](csharpmenuitem.htm) to create a basic add-in.
2. Register a hook to notify your add-in when a user clicks a button in a file data card. Implement IEdmAddIn5::GetAddInInfo as follows:
3. Implement IEdmAddIn5::OnCmd as follows:

  ```vb
        public void OnCmd(ref EdmCmd poCmd, ref EdmCmdData[] ppoData)
        {
               //Respond only to a specific button command
               //The button command to respond to begins with "MyButton:" and ends with the name of the
               //variable to update in the card
               if (Strings.Left(poCmd.mbsComment, 9) == "MyButton:")
               {
                   //Get the name of the variable to update.
                   string VarName = null;
                   VarName = Strings.Right(poCmd.mbsComment, Strings.Len(poCmd.mbsComment) - 9);

                   //Let the user select the file whose path will be copied to the card variable
                   EdmVault5 vault = default(EdmVault5);
                   vault = (EdmVault5)poCmd.mpoVault;
                   IEdmStrLst5 PathList = default(IEdmStrLst5);
                   PathList = vault.BrowseForFile(poCmd.mlParentWnd, (int)EdmBrowseFlag.EdmBws_ForOpen + (int)EdmBrowseFlag.EdmBws_PermitVaultFiles, "", "", "", "", "Select File for " + VarName);

                   if ((PathList != null))
                   {
                       string path = null;
                       path = PathList.GetNext(PathList.GetHeadPosition());

                       //Store the path in the card variable
                       IEdmEnumeratorVariable5 vars = default(IEdmEnumeratorVariable5);
                       vars = (IEdmEnumeratorVariable5)poCmd.mpoExtra;
                       object VariantPath = null;
                       VariantPath = path;
                       vars.SetVar(VarName, "", VariantPath);
                   }
               }

               return;
        }
  ```
4. Click **Build > Build Solution** to build the add-in.
5. Install the add-in through the SOLIDWORKS PDM Professional Administration tool:
6. Click **Cards > File Cards**.
7. Double-click **Text Card**.
8. Add a button to the card.
9. Click the button.
10. In **Caption**, type **Browse...**.
11. In **Command type**, select **Run Add-in**.
12. In **Name of add-in,** type **MyButton:Title**.
13. Save the card and exit the Card Editor.
14. Open File Explorer on the vault and select a checked-out text file.
15. Click **Browse** in the file's data card.
16. The Select File for Title dialog box pops up.
17. Browse to and select the checked-out text file.
18. Click **Open** to copy the path of the selected file to the **Title** field of the file's data card.

### Remarks

In this example, the value of a variable is set using [IEdmEnumeratorVariable5::SetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~SetVar.html). You can also read values using [IEdmEnumeratorVariable5::GetVar](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmEnumeratorVariable5~GetVar.html).

Using a button handler like this add-in, you can also:

- Retrieve the number of configurations, layouts, or both, in the file by inspecting the [EdmCmdData::mpoExtra](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData~mpoExtra.html) variable, which contains [IEdmStrLst5](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html) of file interfaces.
- Switch the active configuration.
- Set focus to a certain control using the members of [EdmCmdData](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData.html).
- Close the card automatically after the button handler returns by setting the [EdmCmdData::mlLongData1](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCmdData~mlLongData1.html) variable to one of the [EdmCardFlag](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmCardFlag.html) constants.
