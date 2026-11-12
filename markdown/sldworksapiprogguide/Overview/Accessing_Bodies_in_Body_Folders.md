---
title: "Accessing Bodies in Body Folders"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Accessing_Bodies_in_Body_Folders.htm"
---

# Accessing Bodies in Body Folders

The [IBodyFolder](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder.html) interface lets you access bodies in solid, surface, and various weldment body folders.

1. If traversing the FeatureManager design tree, then use [IFeature::GetTypeName](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetTypeName.html) to determine the type of feature. If the feature is any of the following types, then you have a body folder feature:

- or -

If you selected a folder and it is any of the following types of folders, then you have a body folder feature:

- swSelBODYFOLDER
- swSelSUBATOMFOLDER
- swSelSUBWELDFOLDER

NOTE: A top-level folder feature named Cut list is identified as SolidBodyFolder, a solid body folder feature. Any subfolder feature named Cut-List-Item is identified CutListFolder, a cut list subfolder feature.

1. Call [IFeature::GetSpecificFeature2](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetSpecificFeature2.html) to get the BodyFolder interface.
2. Call [IBodyFolder::Type](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder~Type.html) to get the type of body folder.
3. Call [IBodyFolder::GetBodyCount](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder~GetBodyCount.html) to get the number of bodies in the folder and call [IBodyFolder::GetBodies](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder~GetBodies.html) to get the bodies in the folder in the order in which they appear in the FeatureManager design tree.

  NOTE: These methods deal only with the bodies in the folder; they do not include the bodies within any subfolders. You must call [IFeature::GetFirstSubFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetFirstSubFeature.html) and [IFeature::GetNextSubFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature~GetNextSubFeature.html) to traverse through the subfolders.
4. To get the feature for a body, call [IBodyFolder::GetFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IBodyFolder~GetFeature.html).
