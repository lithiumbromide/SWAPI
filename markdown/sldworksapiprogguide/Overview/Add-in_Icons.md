---
title: "Add-in Icons"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Add-in_Icons.htm"
---

# Add-in Icons

An add-in's icon displays next to its name in the SOLIDWORKS Add-in Manager (**Tools > Add-ins...**). As of SOLIDWORKS 2022, the SOLIDWORKS Add-in Manager supports scaled icons for third-party add-ins.

The SOLIDWORKS .NET add-in templates are installed with the SOLIDWORKS API SDK. When you create an add-in project in Visual Studio using one of the add-in templates (SwCSharpAddin or SwVBAddin), default icons of various sizes are added to the same folder as the .NET template project class files. During the add-in's post-build event (Right-click Project in Solution Explorer > Properties > Build Events > Post-build event command line), the scaled icons are renamed to match the DLL name and registered in the same folder where the DLL resides, so that at runtime SOLIDWORKS can select an icon that is appropriately scaled for your resolution and display it next to your add-in's name in the Add-in Manager.

Instead of using the default scaled icons, you can add your own set of scaled icons to your add-in's DLL folder. Provide icons of the following sizes:

- 20 X 20
- 32 X 32
- 40 X 40
- 64 X 64
- 96 X 96
- 128 X 128

SOLIDWORKS loads the add-in icon in the following order of precedence:

1. Icon file at registry-specified location:

  Version-specific: HKEY_LOCAL_MACHINE\SOFTWARE\SOLIDWORKS\SOLIDWORKS `version`\Addins\{CLSID}\**Icon Path `<size>`**
  Version-independent: HKEY_LOCAL_MACHINE\SOFTWARE\SOLIDWORKS\AddIns\{CLSID}\**Icon Path `<size>`** Where <size> is:

  - 20
  - 32
  - 40
  - 64
  - 96
  - 128

  If `<size>` is not specified, then the 16 X 16 icon is registered.

  **NOTE**: You can specify **Icon Path** in the registry-specified location using the icon image's full path name, its UNC path, or the path where your add-in's DLL is located.

  In SOLIDWORKS 2013 SP0, and later, you can specify **Icon Path** using a path relative to the SOLIDWORKS `install_dir` folder (typically **C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS**):

  `subfolder1\subfolder2\image.png`
2. PNG scaled icon files whose names match the DLL name (e.g., MySwAddin.dll) and reside in the DLL folder, e.g., MySwAddin_20.png, MySwAddin_40.png, MySwAddin_64.png, etc.
3. BMP scaled icon files whose names match the DLL name (e.g., MySwAddin.dll) and reside in the DLL folder, e.g., MySwAddin_20.bmp, MySwAddin_40.bmp, MySwAddin_64.bmp, etc.

It is recommended that you add your scaled icons to the add-in project's DLL folder. But if your scaled icons must reside in a folder other than the DLL folder, then you must explicitly register them in **SwAddin.RegisterFunction()** as follows:

```vb
#region SOLIDWORKS Registration

 [ComRegisterFunctionAttribute]

 public static void RegisterFunction(Type t)

 {
      Microsoft.Win32.RegistryKey hklm = Microsoft.Win32.Registry.LocalMachine;

      Microsoft.Win32.RegistryKey hkcu = Microsoft.Win32.Registry.CurrentUser;

      string keyname = "SOFTWARE\\SOLIDWORKS\\Addins\\{" + t.GUID.ToString() + "}";

      Microsoft.Win32.RegistryKey addinkey = hklm.CreateSubKey(keyname);

      addinkey.SetValue(null, 0);

      addinkey.SetValue("Description", SWattr.Description);

      addinkey.SetValue("Title", SWattr.Title);

      #region Extract icon during registration

           BitmapHandler iBmp = new BitmapHandler();

           Assembly thisAssembly;

           thisAssembly = System.Reflection.Assembly.GetExecutingAssembly();

           String tempPath =
           iBmp.CreateFileFromResourceBitmap("_2012_PMP_Interfaces.AddInMgrIcon.bmp",
           thisAssembly);

           // Copy the bitmap to a suitable permanent location with a meaningful filename

           String addInPath = System.IO.Path.GetDirectoryName(thisAssembly.Location);

           String iconPath = System.IO.Path.Combine(addInPath, "AddInMgrIcon.bmp");

           System.IO.File.Copy(tempPath, iconPath, true);

           // Register the icon location

           addinkey.SetValue("Icon Path", iconPath );
          // Repeat steps above for all of your scaled icons

      #endregion

      keyname = "Software\\SOLIDWORKS\\AddInsStartup\\{" + t.GUID.ToString() + "}";

      addinkey = hkcu.CreateSubKey(keyname);

      addinkey.SetValue(null, Convert.ToInt32(SWattr.LoadAtStartup),
      Microsoft.Win32.RegistryValueKind.DWord);

 }
```

Changes to the icon file or registry take effect only after SOLIDWORKS is restarted.

To learn more about add-ins and their menu items and toolbars:

- [Add-in Callbacks](Add-in_Callbacks.htm)
- [Add-in Shortcut Menus](Add-in_Shortcut_Menus.htm)
- [Add-in Toolbars](Add-in_Toolbars.htm)
- [Using SwAddin to Create a SOLIDWORKS Add-in](Using_SwAddin_to_Create_a_SolidWorks_Addin.htm)
- [SOLIDWORKS API Add-in Templates and Wizards](SolidWorks_API_Add-Ins,_Project_Templates,_and_Wizards.htm)
