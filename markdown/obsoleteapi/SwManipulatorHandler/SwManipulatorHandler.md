---
title: "SwManipulatorHandler"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/SwManipulatorHandler/SwManipulatorHandler.htm"
---

# SwManipulatorHandler

## SwManipulatorHandler Object

This object is obsolete and has been superseded by [SwManipulatorHandler2](sldworksAPI.chm::/SwManipulatorHandler2/SwManipulatorHandler2.htm).

Must be implemented by an add-in application to interact with a manipulator. The add-in application performs such actions as:

- Defining how a manipulator moves. For example, the add-in application has the manipulator follow a surface in order to place an image on that surface.
- Providing any temporary graphics associated with manipulator. For example, to display a temporary body in a part, the add-in application must call Body2::Display2.
- Applying transforms using Body2::ApplyTransform.

To create a manipulator, first create the SwManipulatorHandler object and then create the Manipulator object.
