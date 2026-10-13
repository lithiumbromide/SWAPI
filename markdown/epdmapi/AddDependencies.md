---
title: "Add Dependencies and Safely Pass Arrays of Structures"
project: ""
interface: ""
member: ""
kind: "topic"
source: "epdmapi/AddDependencies.htm"
---

# Add Dependencies and Safely Pass Arrays of Structures

Add references **EPDM.Interop.epdm.dll** and **EPDM.Interop.EPDMResultCode.dll** by:

1. Right-clicking the project name in the Solution Explorer.
2. Selecting **Add > Reference** or **Add > Project Reference** (depending on the project template you selected).
3. Clicking **Browse tab > Browse...** and navigating to the top folder of your SOLIDWORKS PDM Professional installation.
4. Locating and selecting **EPDM.Interop.epdm.dll**.
5. Clicking **Add** and **OK.**
6. Repeating step 3.
7. Locating and selecting **EPDM.Interop.EPDMResultCode.dll**.
8. Repeating step 5.

Prevent failures when calling methods that pass arrays of structures by:

1. Right-clicking **References > EPDM.Interop.epdm** or **Dependencies > Assemblies > EPDM.Interop.epdm** (depending on the project template you selected) in the Solution Explorer and selecting **Properties**.
2. Setting **Embed Interop Types** to **No**.
3. Right-clicking **References > EPDM.Interop.EPDMResultCode** or **Dependencies > Assemblies > EPDM.Inerop.EPDMResultCode (**depending on the project template you selected) in the Solution Explorer and selecting **Properties**.
4. Setting **Embed Interop Types** to **No**.
5. Initializing arrays of structures in your code to:

  - VB.NET: **Nothing**
  - C#: **null**
