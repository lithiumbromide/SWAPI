---
title: "Suspend Automatic Rebuilds"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Suspend_Automatic_Rebuilds.htm"
---

# Suspend Automatic Rebuilds

It is possible to defer automatic rebuilds of all configurations referenced by an assembly when you make a change to any of the configurations. By deferring automatic rebuilds, you can make many changes and then rebuild the assembly.

To suspend automatic rebuilds of an assembly, set [IAssemblyDoc::EnableAssemblyRebuild](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAssemblyDoc~EnableAssemblyRebuild.html)sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAssemlbyDoc~EnableAssemblyRebuild.htmlto true.

If a user or your application requests a rebuild, then all of the referenced configurations are rebuilt.

This setting only applies to the root assembly document. You must reset this property to true whenever you load the assembly document if you want to defer automatic rebuilds.
