---
title: "Manipulators"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Manipulators.htm"
---

# Manipulators

You can create a manipulator to use in your part and assembly documents.

Typically to create a manipulator:

1. Create the handler interface, [ISwManipulatorHandler2](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwManipulatorHandler2.html), which your add-in application must implement. Your add-in application:

1. Create the [IManipulator](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IManipulator.html) object using [IModelViewManager::CreateManipulator.](sldworksAPI.chm::/SolidWorks.interop.sldworks~SolidWorks.interop.sldworks.IModelViewManager~CreateManipulator.html)
2. Use the IManipulator methods and properties to:

1. Customize the size and appearance of the specific manipulator using the specific manipulator's methods and properties.
