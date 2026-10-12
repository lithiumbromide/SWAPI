---
title: "ExitUserDLL and Old Style MFC Extension DLLs"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/ExitUserDLL_and_Old_Style_MFC_Extension_DLLs.htm"
---

# ExitUserDLL and Old Style MFC Extension DLLs

In SOLIDWORKS 2006 and later, the return value of the exported function ExitUserDLL() is checked to see if an add-in allows or disallows unloading by SOLIDWORKS. The return value is of type [BOOL](BOOL_and_VARIANT_BOOL_Are_Different_Types.htm), where:

- TRUE means the add-in can safely be unloaded by SOLIDWORKS.
- FALSE means the add-in should not be unloaded by SOLIDWORKS.

Add-ins should typically disallow unloading when there are pending references on automation objects managed by the add-in. Continuing the unload process will typically crash SOLIDWORKS if an attempt to free these objects occurs after the add-in has been unloaded.
