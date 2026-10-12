---
title: "Create Submenus in the CommandManager Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Submenus_in_the_CommandManager_Example_CSharp.htm"
---

# Create Submenus in the CommandManager Example (C#)

This example shows how to create submenus in the CommandManager framework by creating individual CommandGroups for each submenu in your tree. Create a C# addin using the SOLIDWORKS VSTA C# addin template. Set up CommandManager CommandGroups in SwAddin.ConnectToSW():

```vb
public bool ConnectToSW(SldWorks ThisSW, int Cookie)
{
            iApp = ThisSW;
            iCookie = Cookie;

            iApp.SetAddinCallbackInfo2(0, this, iCookie);

            iCommand = iApp.GetCommandManager(iCookie);

            SldWorks.CommandGroup commandGroup = null;
            string title = "CommandGroup1";
            string toolTip = "Command group 1 tip";
            string hint = "Command group 1 hint";
            int position = 6;
            commandGroup = iCommand.CreateCommandGroup(CommandGroupID1, title, toolTip, hint, position);
            if (commandGroup != null)
            {
                   BitmapHandler bitmapHandler = new BitmapHandler();
                   commandGroup.LargeIconList = bitmapHandler.CreateFileFromResource("CommandManager.LargeIconList.bmp");
                   commandGroup.LargeMainIcon = bitmapHandler.CreateFileFromResource("CommandManager.LargeMainIcon.bmp");
                   commandGroup.SmallIconList = bitmapHandler.CreateFileFromResource("CommandManager.SmallIconList.bmp");
                   commandGroup.SmallMainIcon = bitmapHandler.CreateFileFromResource("CommandManager.SmallMainIcon.bmp");
                   commandGroup.ShowInDocumentType = (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeNONE;// |
//                            (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypePART |
//                            (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeASSEMBLY |
//                            (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeDRAWING;

                   commandGroup.AddCommandItem2("Command1", -1, "Command1 hint", "Command1 tool tip", 0, "OnCommand1", "OnMenuUpdate", 0, 1);
                   commandGroup.AddCommandItem2("Command2", -1, "Command2 hint", "Command2 tool tip", 1, "OnCommand2", "OnMenuUpdate", 0, 1);

                   commandGroup.HasMenu = true;
                   commandGroup.HasToolbar = true;

                   commandGroup.Activate();
            }

            commandGroup = null;
            title = "CommandGroup1\\CommandSubGroup1";
            toolTip = "Command sub group 1 tip";
            hint = "Command sub group 1 hint";
            position = -1;
            commandGroup = iCommand.CreateCommandGroup(CommandGroupID2, title, toolTip, hint, position);
            if (commandGroup != null)
            {
                 BitmapHandler bitmapHandler = new BitmapHandler();
                 commandGroup.LargeIconList = bitmapHandler.CreateFileFromResource("CommandManager.LargeIconList.bmp");
                 commandGroup.LargeMainIcon = bitmapHandler.CreateFileFromResource("CommandManager.LargeMainIcon.bmp");
                 commandGroup.SmallIconList = bitmapHandler.CreateFileFromResource("CommandManager.SmallIconList.bmp");
                 commandGroup.SmallMainIcon = bitmapHandler.CreateFileFromResource("CommandManager.SmallMainIcon.bmp");
                 commandGroup.ShowInDocumentType = (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeNONE;// |
//                            (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypePART |
//                            (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeASSEMBLY |
//                            (int)SwConst.swDocTemplateTypes_e.swDocTemplateTypeDRAWING;

                 commandGroup.AddCommandItem2("SubCommand1", -1, "Command1 hint", "Command1 tool tip", 0, "OnCommand1", "OnMenuUpdate", 0, 1);
                 commandGroup.AddCommandItem2("SubCommand2", -1, "Command2 hint", "Command2 tool tip", 1, "OnCommand2", "OnMenuUpdate", 0, 1);

                 commandGroup.HasMenu = true;
                 commandGroup.HasToolbar = true;

                 commandGroup.Activate();
           }

           return true;

}
```
