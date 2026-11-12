---
title: "Distribute SOLIDWORKS Add-in"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Miscellaneous/Create_Setup_Project_to_Distribute_SolidWorks_Add-in.htm"
---

# Distribute SOLIDWORKS Add-in

#### To create a Windows Installer setup project and deployment files:

1. Create, build, save, and close a new add-in using a [SOLIDWORKS API SDK template](../Overview/SolidWorks_API_Add-Ins%2c_Project_Templates%2c_and_Wizards.htm) in Microsoft Visual Studio 2015, 2017, or 2019.
2. If using:

- Microsoft Visual Studio 2015, see [Microsoft Visual Studio 2015 Installer Projects](https://marketplace.visualstudio.com/items?itemName=visualstudioclient.MicrosoftVisualStudio2015InstallerProjects) for information on creating or adding a setup project.
- Microsoft Visual Studio 2017 or 2019, see [Microsoft Visual Studio Installer Projects](https://marketplace.visualstudio.com/items?itemName=visualstudioclient.MicrosoftVisualStudio2017InstallerProjects) for information on creating or adding a setup project.

#### To display your add-in in the SOLIDWORKS Add-ins dialog:

1. In Windows 7, run **regedit**.exe.
2. Expand HKEY_LOCAL_MACHINE.
3. Right-click Software, select New > Key, and type SOLIDWORKS as the new key’s name, if **SOLIDWORKS** does not already exist.
4. Right-click SOLIDWORKS, select New > Key, and type AddIns as the new key’s name, if **AddIns** does not already exist.
5. Right-click AddIns, select New > Key, and type {Your add-in’s GUID} as the new key’s name.

  NOTE: You must enclose your GUID in curly braces.
6. Right-click the GUID key, select New > DWORD Value.
7. Type (Default).
8. Double-click **(Default)** and type the value set by your add-in’s RegisterFunction function in Value data, and click **OK**.
9. Right-click the GUID key, select New > String Value.
10. Type Description.
11. Double-click **Description**, type the value set by your add-in’s RegisterFunction function in Value data (e.g., “MyNewAddin description”), and click **OK**.
12. Right-click the GUID key, select New > String Value.
13. Type Title.
14. Double-click **Title**, type the value set by your add-in’s RegisterFunction function in Value data (e.g., “MyNewAddin”), and click **OK**.
