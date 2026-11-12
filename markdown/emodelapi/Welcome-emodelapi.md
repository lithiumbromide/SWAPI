---
title: "Welcome"
project: "eDrawings API Help"
interface: ""
member: ""
kind: "topic"
source: "emodelapi/Welcome-emodelapi.html"
---

# Welcome

The eDrawings application gives you the power to create, view, and share your 3D models and 2D drawings. The eDrawings Application Programming Interface (API) is an OLE programming interface to eDrawings and is implemented as a Microsoft ActiveX control. You can use the eDrawings API to:

- customize the eDrawings Viewer.
- create interactive web pages.
- translate files.

The API contains functions that you can call from Visual Basic for Applications (VBA), VB.NET, VBScript, C#, C++ 6.0, C++/CLI, and C. These functions provide direct access to the eDrawings environment. Currently only the [IEModelViewControl](eDrawings.Interop.EModelViewControl~eDrawings.Interop.EModelViewControl.IEModelViewControl.html) and [IEModelMarkupControl](eDrawings.Interop.EModelMarkupControl~eDrawings.Interop.EModelMarkupControl.IEModelMarkupControl.html) interfaces are supported. Any other interface is not supported and should not be used. Use VBScript to create HTML applications for eDrawings.

##### Sample Projects

The eDrawings API sample projects show how to create eDrawings API applications in Microsoft Visual Studio and other types of applications that support ActiveX controls. The eDrawings API SDK contains these eDrawings API sample projects.

If you are a SOLIDWORKS customer and you have installed eDrawings Professional, locate and double-click **eDrawings API SDK.msi**. Sample projects install to `install_dir`**\Program Files(x86)\Common Files\eDrawings20**`nn\api\examples`, where `nn` is the 2-digit release year of the version of eDrawings installed on your computer.

**NOTE:**

All of the sample code and projects supplied are provided on an as-is basis and are only intended to demonstrate ways of using the eDrawings API. No representations or warranties are made regarding these samples. Any licensed user of eDrawings is free to use any or all of these samples in connection with building applications related to eDrawings and is granted a royalty-free, non-exclusive license for these samples or parts thereof. Intellectual property rights of the samples remain with eDrawings. Any confidentiality provisions of the eDrawings license apply to the samples.
