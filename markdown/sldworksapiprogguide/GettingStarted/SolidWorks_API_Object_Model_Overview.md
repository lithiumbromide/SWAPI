---
title: "SOLIDWORKS API Object Model Overview"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/SolidWorks_API_Object_Model_Overview.htm"
---

# SOLIDWORKS API Object Model Overview

The [ISldWorks](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISldWorks.html) object is the application object; it is the top-level object in the SOLIDWORKS API object hierarchy. All of the other SOLIDWORKS objects are located below the ISldWorks object in the object hierarchy and can be accessed directly or indirectly.

**For compiled help (*.chm):** Each interface's help topic contains an **Access Diagram** section. Click the link in this section to open that interface's access diagram.

**For web help only:** Open the **Access Diagram** by clicking the **ISldWorks > Access Diagram > SldWorks (web help only)** link. Navigate to other objects from there.

If an object can only be accessed indirectly, then you must reference that object from another object higher in the object hierarchy. For example, the [ISketchSpline](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchSpline.html) object can only be accessed indirectly; it cannot exist on its own. You must reference the ISketchSpline object from the [ISketchSegment](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.ISketchSegment.html) object because it exists only within the context of the ISketchSegment object.

Most of the SOLIDWORKS API objects correspond to user-interface functionality; however, several SOLIDWORKS API objects provide functionality only accessible through the SOLIDWORKS API. For example, the [IFeature](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IFeature.html) object lets you access features in the FeatureManager design tree, but the [IAttribute](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IAttribute.html) object is a SOLIDWORKS API-only object because there is no corresponding user-interface functionality.
