---
title: "Context-Sensitive SOLIDWORKS API Help"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/ContextSensitiveHelp.htm"
---

# Context-Sensitive SOLIDWORKS API Help

Context-sensitive SOLIDWORKS API help is available as you edit SOLIDWORKS VBA and .NET macros.

To see context-sensitive SOLIDWORKS API help:

1. Select a SOLIDWORKS API (interface, method, property, or enumerator) in the editor (VBA or VSTA or Visual Studio).
2. Press F1.

As of SOLIDWORKS 2018, if you have Visual Studio 2015 installed, context-sensitive API help for .NET displays in the Microsoft Help Viewer. When you install SOLIDWORKS 2018 or later, SOLIDWORKS API and enumerator helps are registered and integrated with the Help Viewer catalogs of the Visual Studio installed on your machine.

After installing SOLIDWORKS:

- Add Microsoft Help Viewer to Visual Studio (**Tools > Get Tools and Features > Individual Components > Help Viewer**).
- In Visual Studio, select **Help > Set Help Preference > Launch in Help Viewer**.

Please note:

- Help Viewer SOLIDWORKS API help (***.cab** and ***.msha**) for users of Visual Studio 2012, 2013, or 2015 is delivered in `install_dir/`**api/HelpViewer**.
- HTML 2.0 compiled SOLIDWORKS API help for users of VSTA and Visual Studio versions earlier than 2015 is delivered in `install_dir/`**api/HTMLHelp2x**.
- HTML 1.0 compiled SOLIDWORKS API help for users of VBA is delivered in `install_dir`/**api**.

When you press F1 while editing:

- VBA macros, HTML 1.0 compiled help displays.
- VB.NET and C# macros in VSTA 1.0, HTML 2.0 compiled help displays.
- VB.NET and C# programs in Visual Studio (2012, 2013), either Help Viewer help or HTML 2.0 compiled help displays. Configure Visual Studio to launch either the Help Viewer or a browser before using F1.
- VB.NET and C# programs in Visual Studio 2015, only Help Viewer help can display. You must configure Visual Studio 2015 to launch the Help Viewer before using F1.
- VB.NET and C# macros or programs in Visual Studio 2015, example links in the displayed help do not work. You must open local help to see examples.

If after installing SOLIDWORKS, F1 does not display help for SOLIDWORKS APIs in .NET macros, try manually registering the SOLIDWORKS API Help with Help Viewer.

If a previous version of the context-sensitive help is already installed, you must remove it before installing another version. To remove SOLIDWORKS API Help from the Help Viewer:

1. In Visual Studio, select **Help > View Help**.
2. Click the Manage Content tab.
3. In the Action column for the SOLIDWORKS API Help row, click **Remove**.
4. Click **Update** at the bottom of the Manage Content tab.

To register SOLIDWORKS API help with Visual Studio Help Viewer:

1. In Visual Studio, select **Help > View Help**.
2. Click the Manage Content tab.
3. Select **Disk**
4. Select the location of source content by clicking **...** .
5. Navigate to and select `install_dir`**\api\HelpViewer\sldworksapi\helpcontentsetup.msha**.
6. Click **Open**.
7. In the Action column for the SOLIDWORKS API Help row, click **Add**.
8. Click **Update** at the bottom of the Manage Content tab.
9. Click **OK** in the Security dialog box.

To register SOLIDWORKS API enumerator help with Visual Studio Help Viewer:

1. In Visual Studio, select **Help > View Help**.
2. Click the Manage Content tab.
3. Select **Disk**
4. Select the location of source content by clicking **...** .
5. Navigate to and select `install_dir`**\api\HelpViewer\swconst\helpcontentsetup.msha**.
6. Click **Open**.
7. In the Action column for the SOLIDWORKS API Help row, click **Add**.
8. Click **Update** at the bottom of the Manage Content tab.
9. Click **OK** in the Security dialog box.
